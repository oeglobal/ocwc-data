# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20150709_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
    ]
