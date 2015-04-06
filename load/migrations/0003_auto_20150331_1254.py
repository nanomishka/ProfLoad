# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0002_auto_20150331_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professors',
            name='degree',
        ),
        migrations.DeleteModel(
            name='Degrees',
        ),
        migrations.RemoveField(
            model_name='professors',
            name='post',
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
        migrations.DeleteModel(
            name='Professors',
        ),
    ]
