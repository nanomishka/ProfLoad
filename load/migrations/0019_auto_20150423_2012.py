# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0018_auto_20150423_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subgroup',
            name='group',
            field=models.ForeignKey(to='load.Group', unique=True),
            preserve_default=True,
        ),
    ]
