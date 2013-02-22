# -*- coding: utf-8 -*-
from django.db import models

class CourseFeed(models.Model):
    source = models.CharField(max_length=255)
    crmid = models.IntegerField(blank=True, null=True, db_column='crm_id')
    url = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    last_index = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True)
    reviewed = models.BooleanField(default=False)
    # comment = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.source

LOG_TYPES = (
    ('0', 'Download feed log'),
)

LOG_STATUS_TYPES = (
    ('0', 'Success'),
    ('1', 'Failure'),
)

class Log(models.Model):
    log_type = models.IntegerField(choices=LOG_TYPES, default=0)
    result = models.TextField(blank=True, null=True)
    status = models.IntegerField(default=0, choices=LOG_STATUS_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

class Course(models.Model):
    source = models.ForeignKey(CourseFeed)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    retrieved = models.DateTimeField(auto_now_add=True)
    permalink = models.TextField()

# class OcvbEntries(models.Model):
#     start_time = models.DateTimeField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     author_url = models.CharField(max_length=255, blank=True, null=True)
#     institution = models.CharField(max_length=255, blank=True, null=True)
#     institution_url = models.CharField(max_length=255, blank=True, null=True)
#     video_url = models.CharField(max_length=255, blank=True, null=True)
#     language = models.CharField(max_length=255, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)