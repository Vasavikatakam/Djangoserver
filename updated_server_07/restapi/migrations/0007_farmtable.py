# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0006_videotable'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmTable',
            fields=[
                ('farm_id', models.IntegerField(primary_key=True, serialize=False)),
                ('area', models.FloatField()),
                ('house_farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.House')),
            ],
        ),
    ]
