# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0015_typeload_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typeload',
            name='grade',
        ),
        migrations.AddField(
            model_name='typeload',
            name='typeTL',
            field=models.CharField(default=b'non', max_length=3, choices=[(b'all', b'all'), (b'sub', b'subgroup'), (b'non', b'usual')]),
            preserve_default=True,
        ),
    ]
