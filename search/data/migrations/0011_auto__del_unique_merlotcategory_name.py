# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'MerlotCategory', fields ['name']
        db.delete_unique(u'data_merlotcategory', ['name'])


    def backwards(self, orm):
        
        # Adding unique constraint on 'MerlotCategory', fields ['name']
        db.create_unique(u'data_merlotcategory', ['name'])


    models = {
        u'data.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['data.Category']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'data.course': {
            'Meta': {'object_name': 'Course'},
            'author': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '765'}),
            'calais_socialtags': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'calais_topics': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'categories': ('mptt.fields.TreeManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['data.Category']", 'null': 'True', 'blank': 'True'}),
            'content_medium': ('django.db.models.fields.CharField', [], {'default': "'text'", 'max_length': '100'}),
            'contributors': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '765', 'blank': 'True'}),
            'date_indexed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'license': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'linkhash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '96'}),
            'linkurl': ('django.db.models.fields.TextField', [], {}),
            'merlot_categories': ('mptt.fields.TreeManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['data.MerlotCategory']", 'null': 'True', 'blank': 'True'}),
            'merlot_present': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'merlot_synced': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'opencalais_response': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Provider']"}),
            'rights': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Source']"}),
            'tags': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'translated_text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'data.log': {
            'Meta': {'object_name': 'Log'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_courses': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'new_courses'", 'symmetrical': 'False', 'to': u"orm['data.Course']"}),
            'processed_courses': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'processed_courses'", 'symmetrical': 'False', 'to': u"orm['data.Course']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Source']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'data.merlotcategory': {
            'Meta': {'object_name': 'MerlotCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'merlot_id': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['data.MerlotCategory']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'data.provider': {
            'Meta': {'object_name': 'Provider'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'external_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'data.source': {
            'Meta': {'object_name': 'Source'},
            'edit_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'default': "'rss'", 'max_length': '50'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Provider']"}),
            'update_speed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        }
    }

    complete_apps = ['data']
