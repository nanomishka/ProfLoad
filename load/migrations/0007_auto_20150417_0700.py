# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0006_auto_20150409_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spread',
            name='group',
            field=models.ForeignKey(to='load.Group', blank=True),
            preserve_default=True,
        ),
    ]
