# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from joomla.models import *

template = '''<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/" xmlns:content="http://purl.org/rss/1.0/modules/content/"
    xmlns:wfw="http://wellformedweb.org/CommentAPI/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:wp="http://wordpress.org/export/1.2/">

<channel>
    <title>OpenCourseWare Consortium</title>
    <link>http://mainsite.fey</link>
    <wp:wxr_version>1.2</wp:wxr_version>
    <wp:author><wp:author_id>1</wp:author_id><wp:author_login>gandalf</wp:author_login><wp:author_email>jure@ocwconsortium.org</wp:author_email><wp:author_display_name><![CDATA[gandalf]]></wp:author_display_name><wp:author_first_name><![CDATA[]]></wp:author_first_name><wp:author_last_name><![CDATA[]]></wp:author_last_name></wp:author>

'''

def main(filename):
    f = open(filename, 'w')
    f.write(template)

    for link in JosNewslinks.objects.all():
        item = u'''
        <item>
            <title>{link.title}</title>
            
            <pubDate>{link.pubdate}</pubDate>
            <dc:creator>gandalf</dc:creator>
            <description></description>
            <content:encoded><![CDATA[]]></content:encoded>
            <excerpt:encoded><![CDATA[]]></excerpt:encoded>
            <wp:post_date>{link.pubdate}</wp:post_date>
            <wp:comment_status>closed</wp:comment_status>
            <wp:ping_status>closed</wp:ping_status>
            <wp:post_name>opening-the-books</wp:post_name>
            <wp:status>publish</wp:status>
            <wp:post_parent>0</wp:post_parent>
            <wp:menu_order>0</wp:menu_order>
            <wp:post_type>newslink</wp:post_type>
            <wp:post_password></wp:post_password>
            <wp:is_sticky>0</wp:is_sticky>
            <wp:postmeta>
                <wp:meta_key>_edit_last</wp:meta_key>
                <wp:meta_value><![CDATA[1]]></wp:meta_value>
            </wp:postmeta>
            <wp:postmeta>
                <wp:meta_key>newslink_url</wp:meta_key>
                <wp:meta_value><![CDATA[{link.url}]]></wp:meta_value>
            </wp:postmeta>
            <wp:postmeta>
                <wp:meta_key>_newslink_url</wp:meta_key>
                <wp:meta_value><![CDATA[field_51f50f9c459fb]]></wp:meta_value>
            </wp:postmeta>
            <wp:postmeta>
                <wp:meta_key>newslink_alias</wp:meta_key>
                <wp:meta_value><![CDATA[{link.linkalias}]]></wp:meta_value>
            </wp:postmeta>
            <wp:postmeta>
                <wp:meta_key>_newslink_alias</wp:meta_key>
                <wp:meta_value><![CDATA[field_51f5104ddcda2]]></wp:meta_value>
            </wp:postmeta>
        </item>
        '''.format(link=link)
        f.write(item.encode('utf-8'))

    f.write('</channel></rss>')
    f.close()

class Command(BaseCommand):
    args = "newslinks.wxr"
    help = "export newslinks as wxr file"

    def handle(self, *args, **options):
        for filename in args:
            main(filename)
