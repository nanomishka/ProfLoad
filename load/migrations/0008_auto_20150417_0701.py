# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0007_auto_20150417_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spread',
            name='group',
            field=models.ForeignKey(blank=True, to='load.Group', null=True),
            preserve_default=True,
        ),
    ]
