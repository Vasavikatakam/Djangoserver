# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0009_auto_20170913_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetable',
            name='image',
            field=models.ImageField(upload_to=b''),
        ),
    ]