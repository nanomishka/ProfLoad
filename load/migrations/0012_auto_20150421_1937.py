# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0011_group_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loadunit',
            name='hours',
        ),
        migrations.AddField(
            model_name='loadunit',
            name='grade',
            field=models.CharField(default=b'b', max_length=1, choices=[(b'b', b'b'), (b'm', b'm'), (b's', b's')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spread',
            name='hours',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='grade',
            field=models.CharField(default=b'b', max_length=1, choices=[(b'b', b'b'), (b'm', b'm'), (b's', b's')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spread',
            name='group',
            field=models.ForeignKey(to='load.Group', null=True),
            preserve_default=True,
        ),
    ]
