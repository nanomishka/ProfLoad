# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0012_auto_20150421_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='loadunit',
            name='hours',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
