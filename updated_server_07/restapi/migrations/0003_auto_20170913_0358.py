# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 03:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_mem_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mem_details',
            name='house_idm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.House'),
        ),
    ]
