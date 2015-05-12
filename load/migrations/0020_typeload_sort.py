# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0019_auto_20150423_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeload',
            name='sort',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
