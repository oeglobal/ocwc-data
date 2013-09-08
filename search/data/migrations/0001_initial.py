# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Provider'
        db.create_table(u'data_provider', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('external_id', self.gf('django.db.models.fields.TextField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'data', ['Provider'])

        # Adding model 'Source'
        db.create_table(u'data_source', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('provider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Provider'])),
            ('kind', self.gf('django.db.models.fields.CharField')(default='rss', max_length=50)),
            ('url', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('update_speed', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'data', ['Source'])

        # Adding model 'Course'
        db.create_table(u'data_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('linkhash', self.gf('django.db.models.fields.CharField')(unique=True, max_length=96)),
            ('linkurl', self.gf('django.db.models.fields.TextField')()),
            ('provider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Provider'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Source'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('tags', self.gf('django.db.models.fields.TextField')()),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('author', self.gf('django.db.models.fields.CharField')(default='', max_length=765)),
            ('rights', self.gf('django.db.models.fields.TextField')(default='')),
            ('contributors', self.gf('django.db.models.fields.CharField')(default='', max_length=765, blank=True)),
            ('license', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_indexed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'data', ['Course'])

        # Adding model 'Log'
        db.create_table(u'data_log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Source'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'data', ['Log'])

        # Adding M2M table for field processed_courses on 'Log'
        db.create_table(u'data_log_processed_courses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('log', models.ForeignKey(orm[u'data.log'], null=False)),
            ('course', models.ForeignKey(orm[u'data.course'], null=False))
        ))
        db.create_unique(u'data_log_processed_courses', ['log_id', 'course_id'])

        # Adding M2M table for field new_courses on 'Log'
        db.create_table(u'data_log_new_courses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('log', models.ForeignKey(orm[u'data.log'], null=False)),
            ('course', models.ForeignKey(orm[u'data.course'], null=False))
        ))
        db.create_unique(u'data_log_new_courses', ['log_id', 'course_id'])


    def backwards(self, orm):
        
        # Deleting model 'Provider'
        db.delete_table(u'data_provider')

        # Deleting model 'Source'
        db.delete_table(u'data_source')

        # Deleting model 'Course'
        db.delete_table(u'data_course')

        # Deleting model 'Log'
        db.delete_table(u'data_log')

        # Removing M2M table for field processed_courses on 'Log'
        db.delete_table('data_log_processed_courses')

        # Removing M2M table for field new_courses on 'Log'
        db.delete_table('data_log_new_courses')


    models = {
        u'data.course': {
            'Meta': {'object_name': 'Course'},
            'author': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '765'}),
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
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Provider']"}),
            'rights': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Source']"}),
            'tags': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {})
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
        u'data.provider': {
            'Meta': {'object_name': 'Provider'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'external_id': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'data.source': {
            'Meta': {'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'default': "'rss'", 'max_length': '50'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Provider']"}),
            'update_speed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        }
    }

    complete_apps = ['data']
