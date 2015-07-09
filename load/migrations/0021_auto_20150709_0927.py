# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0020_typeload_sort'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeload',
            name='name',
            field=models.CharField(unique=True, max_length=40),
            preserve_default=True,
        ),
    ]
