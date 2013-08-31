from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=255)
    external_id = models.TextField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

SOURCE_KIND_CHOICES = (
    ('rss', 'RSS feed'),
    ('scraper', 'Gatherer scraper'),
    ('manual', 'Manual importer')
)

class Source(models.Model):
    provider = models.ForeignKey(Provider)
    kind = models.CharField(choices=SOURCE_KIND_CHOICES, default='rss', max_length=50)
    url  = models.TextField(blank=True, default='')
    update_speed = models.IntegerField(default=0, help_text='Update speed in days, 0 to disable')

    def __unicode__(self):
        return u"%s (%s)" % (self.provider.name, self.kind)

class Course(models.Model):
    title = models.TextField()
    linkhash = models.CharField(max_length=96, unique=True)
    linkurl = models.TextField()

    provider = models.ForeignKey(Provider)
    source = models.ForeignKey(Source)
    
    description = models.TextField()
    tags = models.TextField()

    language = models.CharField(max_length=300)
    author = models.CharField(max_length=765, default='')
    rights = models.TextField(default='')
    contributors = models.CharField(max_length=765, blank=True, default='')
    license = models.TextField(blank=True, default='')
    
    date_published = models.DateTimeField(auto_now_add=True)
    date_indexed = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

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