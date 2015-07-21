# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0025_auto_20150721_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subgroup',
            name='group',
            field=models.OneToOneField(to='load.Group'),
        ),
    ]
