# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=mptt.fields.TreeManyToManyField(to='data.Category', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='merlot_categories',
            field=mptt.fields.TreeManyToManyField(to='data.MerlotCategory', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='merlot_languages',
            field=models.ManyToManyField(to='data.MerlotLanguage'),
        ),
    ]
