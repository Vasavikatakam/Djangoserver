# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 04:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0004_auto_20170913_0404'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('house_idi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.House')),
            ],
        ),
    ]
