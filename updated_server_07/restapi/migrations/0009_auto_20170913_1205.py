# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0008_farmpoints'),
    ]

    operations = [
        migrations.CreateModel(
            name='farmcroptable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_id', models.IntegerField()),
                ('year', models.IntegerField()),
                ('crop', models.CharField(max_length=35)),
                ('farm_idc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.FarmTable')),
            ],
        ),
        migrations.CreateModel(
            name='wellinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yield1', models.FloatField()),
                ('welldatetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='welltable',
            fields=[
                ('well_id', models.IntegerField(primary_key=True, serialize=False)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('depth', models.FloatField()),
                ('farm_idw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.FarmTable')),
            ],
        ),
        migrations.AddField(
            model_name='wellinfo',
            name='well_idf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.welltable'),
        ),
    ]
