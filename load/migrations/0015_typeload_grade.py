# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0014_remove_spread_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeload',
            name='grade',
            field=models.CharField(default=b'non', max_length=3, choices=[(b'all', b'all'), (b'sub', b'subgroup'), (b'non', b'usual')]),
            preserve_default=True,
        ),
    ]
