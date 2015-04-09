# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load', '0005_caf_group_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormPass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LoadUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sem', models.IntegerField()),
                ('hours', models.IntegerField()),
                ('caf', models.ForeignKey(to='load.Caf')),
                ('formPass', models.ForeignKey(to='load.FormPass')),
                ('subject', models.ForeignKey(to='load.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Spread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeLoad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='group',
            name='caf',
            field=models.ForeignKey(to='load.Caf'),
        ),
        migrations.AlterField(
            model_name='group',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='group',
            name='sem',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='spread',
            name='group',
            field=models.ForeignKey(to='load.Group'),
        ),
        migrations.AddField(
            model_name='spread',
            name='loadUnit',
            field=models.ForeignKey(to='load.LoadUnit'),
        ),
        migrations.AddField(
            model_name='spread',
            name='prof',
            field=models.ForeignKey(to='load.Professors'),
        ),
        migrations.AddField(
            model_name='loadunit',
            name='typeLoad',
            field=models.ForeignKey(to='load.TypeLoad'),
        ),
    ]
