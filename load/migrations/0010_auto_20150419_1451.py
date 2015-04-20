# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0009_auto_20150417_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together=set([('caf', 'sem', 'number')]),
        ),
    ]
