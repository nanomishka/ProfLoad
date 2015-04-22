# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0013_loadunit_hours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spread',
            name='hours',
        ),
    ]
