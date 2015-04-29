# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0008_auto_20150417_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spread',
            name='group',
            field=models.ForeignKey(to='load.Group'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spread',
            name='prof',
            field=models.ForeignKey(to='load.Professors', null=True),
            preserve_default=True,
        ),
    ]
