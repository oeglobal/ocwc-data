# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='data.Category', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('linkhash', models.CharField(unique=True, max_length=96)),
                ('linkurl', models.TextField(verbose_name='URL')),
                ('description', models.TextField()),
                ('tags', models.TextField(blank=True)),
                ('language', models.CharField(max_length=300, choices=[(b'Catalan', b'Catalan'), (b'Chinese', b'Chinese'), (b'Dutch', b'Dutch'), (b'English', b'English'), (b'Finnish', b'Finnish'), (b'French', b'French'), (b'Galician', b'Galician'), (b'German', b'German'), (b'Hebrew', b'Hebrew'), (b'Indonesian', b'Indonesian'), (b'Italian', b'Italian'), (b'Japanese', b'Japanese'), (b'Korean', b'Korean'), (b'Malay', b'Malay'), (b'Persian', b'Persian'), (b'Polish', b'Polish'), (b'Portuguese', b'Portuguese'), (b'Russian', b'Russian'), (b'Slovenian', b'Slovenian'), (b'Spanish', b'Spanish'), (b'Turkish', b'Turkish')])),
                ('author', models.CharField(default=b'', max_length=765)),
                ('author_organization', models.TextField(default=b'', blank=True)),
                ('rights', models.TextField(default=b'', blank=True)),
                ('contributors', models.CharField(default=b'', max_length=765, blank=True)),
                ('license', models.TextField(default=b'', blank=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('date_indexed', models.DateTimeField(auto_now=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('content_medium', models.CharField(default=b'text', max_length=100, verbose_name='Content type', choices=[(b'text', b'Text'), (b'textbook', b'Textbook'), (b'video', b'Video'), (b'audio', b'Audio')])),
                ('translated_text', models.TextField(blank=True)),
                ('calais_socialtags', models.TextField(blank=True)),
                ('calais_topics', models.TextField(blank=True)),
                ('opencalais_response', models.TextField(blank=True)),
                ('merlot_present', models.BooleanField(default=False)),
                ('merlot_synced', models.BooleanField(default=False)),
                ('merlot_synced_date', models.DateTimeField(null=True)),
                ('merlot_id', models.IntegerField(null=True)),
                ('merlot_ignore', models.BooleanField(default=False)),
                ('merlot_material_type', models.CharField(default=b'', max_length=100, blank=True)),
                ('merlot_url', models.TextField(default=b'', blank=True)),
                ('merlot_xml', models.TextField(default=b'', blank=True)),
                ('image_url', models.TextField(default=b'', blank=True)),
                ('audience', models.IntegerField(null=True, choices=[(1, b'Grade School'), (2, b'Middle School'), (3, b'High School'), (4, b'College General Ed'), (5, b'College Lower Division'), (6, b'College Upper Division'), (7, b'Graduate School'), (8, b'Professional')])),
                ('creative_commons', models.CharField(default=b'Unsure', max_length=30, verbose_name='Is CC Licensed?', choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Unsure', b'Unsure')])),
                ('creative_commons_commercial', models.CharField(default=b'', max_length=30, verbose_name='Is CC Commercial allowed?', blank=True, choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Unsure', b'Unsure')])),
                ('creative_commons_derivatives', models.CharField(default=b'', max_length=30, verbose_name='Is CC Derative work allowed or Share-Alike?', blank=True, choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Sa', b'Share-Alike')])),
                ('is_404', models.BooleanField(default=False)),
                ('categories', mptt.fields.TreeManyToManyField(to='data.Category', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
                ('new_courses', models.ManyToManyField(related_name='new_courses', to='data.Course')),
                ('processed_courses', models.ManyToManyField(related_name='processed_courses', to='data.Course')),
            ],
        ),
        migrations.CreateModel(
            name='MerlotCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('merlot_id', models.IntegerField()),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='data.MerlotCategory', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MerlotLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('external_id', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchQuery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query', models.TextField()),
                ('language', models.CharField(max_length=150, blank=True)),
                ('count', models.IntegerField(default=1)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('processed', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.CharField(default=b'rss', max_length=50, choices=[(b'rss', b'RSS feed'), (b'scraper', b'Gatherer scraper'), (b'manual', b'Manual importer'), (b'form', b'Online form')])),
                ('url', models.TextField(default=b'', blank=True)),
                ('update_speed', models.IntegerField(default=0, help_text=b'Update speed in days, 0 to disable')),
                ('edit_key', models.CharField(max_length=255, blank=True)),
                ('provider', models.ForeignKey(to='data.Provider')),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='source',
            field=models.ForeignKey(to='data.Source'),
        ),
        migrations.AddField(
            model_name='course',
            name='merlot_categories',
            field=mptt.fields.TreeManyToManyField(to='data.MerlotCategory', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='merlot_languages',
            field=models.ManyToManyField(to='data.MerlotLanguage', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='provider',
            field=models.ForeignKey(to='data.Provider', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='source',
            field=models.ForeignKey(to='data.Source', null=True),
        ),
    ]
