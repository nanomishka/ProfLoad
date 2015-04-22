# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0016_auto_20150422_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(unique=True, max_length=127),
            preserve_default=True,
        ),
    ]
