import calendar
from datetime import datetime
import json
import logging
import time
import types
import urllib
import urllib2
import urlparse
import pytz

SOLR_ADD_BATCH = 200 # Number of documents to send in batch when adding
logger = logging.getLogger(__name__)

def to_solr_date(date):
    """
    Solr demands ISO8601 time format in UTC timezone. This converts TZ and formats to compatible format.
    """
    utc_date = date.astimezone(pytz.utc)
    return utc_date.strftime("%Y-%m-%dT%H:%M:%SZ")

def from_solr_date(date):
     return datetime.fromtimestamp(calendar.timegm(time.strptime(date, "%Y-%m-%dT%H:%M:%SZ")), tz=pytz.utc)

class SolrResults:
    def __init__(self):
        self.query_time = None      # Time the query took
        self.results_count = None   # Number of found results
        self.start_index = None     # Index of start
        self.documents = []      # Found results
        self.facets = {}         # Found facet counts
        self.highlights = {}     # Highligts for found documents

class SolrInterface(object):
    _add_batch = []
    _shards = None

    endpoints = []
    default_endpoint = None

    def __init__(self, endpoints, default_endpoint):
        if endpoints is None or default_endpoint is None:
            logger.warning("Faulty Solr configuration, SOLR will not be available!")
        self.endpoints = endpoints
        self.default_endpoint = default_endpoint

    def _send_solr_command(self, core_url, json_command):
        """
        Sends JSON string to Solr instance
        """

        # Check document language and dispatch to correct core
        # url = urlparse.urljoin(core_url, "update/json/")]
        update_url = 'update/json'
        url = '/'.join([core_url.rstrip('/'), update_url.lstrip('/')])
        try:
            request = urllib2.Request(url, json_command, {'Content-Type':'application/json'})
            response = urllib2.urlopen(request).read()
        except urllib2.HTTPError as e:
            logger.error("Failed to send update to Solr endpoint [%s]: %s", core_url, e, exc_info=True)
            # return False
            print json_command
        return True

    def add(self, documents):
        """
        Adds documents to Solr index
        documents - Single item or list of items to add
        """

        if isinstance(documents, types.ListType):
            self._add_batch.extend(documents)
        else:
            self._add_batch.append(documents)

        if len(self._add_batch) > SOLR_ADD_BATCH:
            self._addFlushBatch()

    def _addFlushBatch(self):
        """
        Sends all waiting documents to Solr
        """
        if len(self._add_batch) > 0:
            language_batches = {}
            # Create command JSONs for each of language endpoints
            for lang in self.endpoints:
                # Append documents with languages without endpoint to default endpoint
                document_jsons = ["\"add\":{\"doc\": " + json.dumps(data) + "}" for data in self._add_batch
                                  if data.get("language", self.default_endpoint) == lang or (lang == self.default_endpoint and not self.endpoints.has_key(data.get("language")))]
                command_json = "{" + ",".join(document_jsons) + "}"
                language_batches[lang] = command_json
            # Solr requires for documents to be sent in { "add" : { "doc" : {...} }, "add": { "doc" : { ... }, ... }
            # format which isn't possible with python dictionaries
            for lang in language_batches:
                self._send_solr_command(self.endpoints[lang], language_batches[lang])
                self._add_batch = []

    def deleteAll(self):
        """
        Deletes whole Solr index. Use with care.
        """
        for core in self.endpoints:
            self._send_solr_command(self.endpoints[core], "{\"delete\": { \"query\" : \"*:*\"}}")

    def delete(self, id):
        """
        Deletes document with ID on all Solr cores
        """
        for core in self.endpoints:
            self._send_solr_command(self.endpoints[core], "{\"delete\" : { \"id\" : \"%s\"}}" % (id,))

    def commit(self):
        """
        Flushes all pending changes and commits Solr changes
        """
        self._addFlushBatch()
        for core in self.endpoints:
            self._send_solr_command(self.endpoints[core], "{ \"commit\":{} }")

    def optimize(self):
        for core in self.endpoints:
            self._send_solr_command(self.endpoints[core], "{ \"optimize\": {} }")


    def _get_shards(self):
        """
        Returns comma separated list of configured Solr cores
        """
        if self._shards is None:
            endpoints = []
            for endpoint in self.endpoints:
                # We need to remove and http:// prefixes from URLs
                url = urlparse.urlparse(self.endpoints[endpoint])
                endpoints.append("/".join([url.netloc, url.path]))
            self._shards = ",".join(endpoints)
        return self._shards

    def query(self, query, filters=None, sort=None, start=0, rows=30):
        """
        Queries Solr and returns results

        query - Text query to search for
        filters - dictionary of filters to apply when searching in form of { "field":"filter_value" }
        sort - list of fields to sort on in format of ["field asc", "field desc", ... ]
        start - start number of first result (used in pagination)
        rows - number of rows to return (used for pagination, defaults to 30)
        """

        fields = [("q", query),
              ("json.nl", "map"), # Return facets as JSON objects
              ("wt", "json"),
              ("fl", "*,score"), # Return score along with results
              ("start", str(start)),
              ("rows", str(rows))
             ]

        # Use shards parameter only if there are several cores active
        if len(self.endpoints) > 1:
            fields.append(("shards", self._get_shards()))

        # Prepare filters
        if not filters is None:
            for filter,value in filters.items():
                fields.append(("fq", ":".join([filter, value])))

        # Append sorting parameters
        if not sort is None:
            fields.append(("sort", ",".join(sort)))

        # Do request to Solr server to default endpoint (other cores will be queried over distributed shard functionality)
        assert self.default_endpoint in self.endpoints
        request_url = "/".join([self.endpoints[self.default_endpoint], "select/"])
        request_url.replace('//', '/')
        data = urllib.urlencode([(k,v.encode('utf-8')) for k,v in fields])

        try:
            request = urllib2.Request(request_url, data=data, headers={'Content-Type':'application/x-www-form-urlencoded; charset=utf-8'})
            response = urllib2.urlopen(request).read()
        except (urllib2.HTTPError, urllib2.URLError) as e:
            logger.error("Failed to connect to Solr server: %s!", e, exc_info=True)
            return None

        try:
            results = json.loads(response)
        except Exception as e:
            logger.error("Failed to parse JSON response: %s!", e, exc_info=True)
            return None

        assert "responseHeader" in results
        # Check for response status
        if not results.get("responseHeader").get("status") == 0:
            logger.error("Server error while retrieving results: %s", response.data)
            return None

        assert "response" in results
        dict_response = results.get("response")

        result_obj = SolrResults()
        result_obj.query_time = results.get("responseHeader").get("QTime", None)
        result_obj.results_count = dict_response.get("numFound", 0)
        result_obj.start_index = dict_response.get("start", 0)

        for doc in dict_response.get("docs", []):
            result_obj.documents.append(doc)

        # Process facets
        if "facet_counts" in results:
            assert "facet_fields" in results.get("facet_counts")
            facet_types = ["facet_fields", "facet_dates", "facet_queries"]
            for type in facet_types:
                assert type in results.get("facet_counts")
                items = results.get("facet_counts").get(type)
                for field,values in items.items():
                    result_obj.facets[field] = []
                    for facet,value in values.items():
                        result_obj.facets[field].append((facet, value))

        # Process highlights
        if "highlighting" in results:
            for key,value in results.get("highlighting").items():
                result_obj.highlights[key] = value

        return result_obj
