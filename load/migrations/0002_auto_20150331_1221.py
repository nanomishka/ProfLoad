# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degrees',
            name='name',
            field=models.CharField(unique=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='posts',
            name='name',
            field=models.CharField(unique=True, max_length=20),
            preserve_default=True,
        ),
    ]
