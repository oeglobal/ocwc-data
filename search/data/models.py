from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from django.core.urlresolvers import reverse

import hashlib
import uuid

class Provider(models.Model):
    name = models.CharField(max_length=255)
    external_id = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

SOURCE_KIND_CHOICES = (
    ('rss', 'RSS feed'),
    ('scraper', 'Gatherer scraper'),
    ('manual', 'Manual importer'),
    ('form', 'Online form'),
)

class Source(models.Model):
    provider = models.ForeignKey(Provider)
    kind = models.CharField(choices=SOURCE_KIND_CHOICES, default='rss', max_length=50)
    url  = models.TextField(blank=True, default='')
    update_speed = models.IntegerField(default=0, help_text='Update speed in days, 0 to disable')

    edit_key = models.CharField(max_length=255, blank=True)

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.edit_key:
            self.edit_key = uuid.uuid4().get_hex()
        super(Source, self).save(force_insert=force_insert, force_update=force_update, using=using)

    def get_absolute_url(self):
        return reverse('dashboard:source-course-list', kwargs={'pk':self.id})

    def __unicode__(self):
        return u"%s (%s)" % (self.provider.name, self.kind)

CONTENT_MEDIUM_CHOICES = (
    ('text', 'Text'),
    ('textbook', 'Textbook'),
    ('video', 'Video'),
    ('audio', 'Audio')
)

LANGUAGE_CHOICES = (
    ('Catalan', 'Catalan'),
    ('Chinese', 'Chinese'),
    ('Dutch', 'Dutch'),
    ('English', 'English'),
    ('Finnish', 'Finnish'),
    ('French', 'French'),
    ('Galician', 'Galician'),
    ('German', 'German'),
    ('Hebrew', 'Hebrew'),
    ('Indonesian', 'Indonesian'),
    ('Italian', 'Italian'),
    ('Japanese', 'Japanese'),
    ('Korean', 'Korean'),
    ('Malay', 'Malay'),
    ('Persian', 'Persian'),
    ('Polish', 'Polish'),
    ('Portuguese', 'Portuguese'),
    ('Russian', 'Russian'),
    ('Slovenian', 'Slovenian'),
    ('Spanish', 'Spanish'),
    ('Turkish', 'Turkish'),
)

class Course(models.Model):
    title = models.TextField()
    linkhash = models.CharField(max_length=96, unique=True)
    linkurl = models.TextField(verbose_name=u'URL')

    provider = models.ForeignKey(Provider)
    source = models.ForeignKey(Source)
    
    description = models.TextField()
    tags = models.TextField()

    language = models.CharField(max_length=300, choices=LANGUAGE_CHOICES)
    author = models.CharField(max_length=765, default='')
    rights = models.TextField(default='')
    contributors = models.CharField(max_length=765, blank=True, default='')
    license = models.TextField(blank=True, default='')
    
    date_published = models.DateTimeField(auto_now_add=True)
    date_indexed = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    content_medium = models.CharField(max_length=100, choices=CONTENT_MEDIUM_CHOICES, default='text', verbose_name=u'Content type')

    translated_text = models.TextField(blank=True)
    calais_socialtags = models.TextField(blank=True)
    calais_topics = models.TextField(blank=True)
    opencalais_response = models.TextField(blank=True)

    categories = TreeManyToManyField('Category', blank=True, null=True)

    def save(self, update_linkhash=False, force_insert=False, force_update=False, using=None):
        if not self.linkhash or update_linkhash:
            self.linkhash = hashlib.md5(self.linkurl.encode('utf-8')).hexdigest()

        super(Course, self).save(force_insert=force_insert, force_update=force_update, using=using)

    def get_next(self):
        try:
            return Course.objects.filter(source=self.source, id__gt=self.pk).order_by('id')[0]
        except IndexError:
            pass

LOG_STATUS_CHOICES = (
    (0, 'Failed'),
    (1, 'Success')
)

class Log(models.Model):
    source = models.ForeignKey(Source)
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)

    processed_courses = models.ManyToManyField(Course, related_name='processed_courses')
    new_courses = models.ManyToManyField(Course, related_name='new_courses')

class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return self.name