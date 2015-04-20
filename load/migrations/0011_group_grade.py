# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0010_auto_20150419_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='grade',
            field=models.CharField(default=b'b', max_length=1, choices=[(b'b', b'bachelor'), (b'm', b'master'), (b's', b'specialist')]),
            preserve_default=True,
        ),
    ]
