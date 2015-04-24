# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0017_auto_20150422_0729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subgroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('group', models.ForeignKey(to='load.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together=set([('caf', 'sem', 'number', 'grade')]),
        ),
        migrations.AlterUniqueTogether(
            name='professors',
            unique_together=set([('first_name', 'last_name', 'middle_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='spread',
            unique_together=set([('loadUnit', 'group')]),
        ),
    ]
