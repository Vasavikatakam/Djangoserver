# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0007_farmtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='farmpoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('farm_idp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.FarmTable')),
            ],
        ),
    ]
