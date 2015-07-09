# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0022_spread_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spread',
            name='hours',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
