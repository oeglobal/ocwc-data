# -*- coding: utf-8 -*-
from datetime import datetime
from rfc3339 import rfc3339
import os

from django.core.management.base import BaseCommand
from django.conf import settings

from joomla.models import *
from web.models import *
def main():
	f = open(os.path.join(settings.JOOMLA_PATH,'feeds/ocwcmemberfeeds.opml'),'w')

	f.write('''<?xml version="1.0" encoding="utf-8"?>
<opml xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<head>
		<title>OpenCourseWare Consortium Member Course Feeds</title>
		 <dateCreated>%s</dateCreated>
	</head>
	<body>		
''' % rfc3339(datetime.now())
)

	for feed in CfGetorgs.objects.filter(executed=0):
		f.write(u'''
			<outline type="rss"  title="{feed.source}" text="{feed.source}" url="{feed.url}"/>'''.format(feed=feed).encode('utf-8'))
	f.write('\n</body>\n</opml>')
	f.close()

class Command(BaseCommand):
    help = "generates OPML feed that lives in http://www.ocwconsortium.org/feeds/ocwcmemberfeeds.opml"

    def handle(self, *args, **options):
    	main()
