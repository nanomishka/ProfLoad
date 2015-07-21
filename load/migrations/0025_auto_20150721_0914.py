# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0024_merge'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='spread',
            unique_together=set([]),
        ),
    ]
