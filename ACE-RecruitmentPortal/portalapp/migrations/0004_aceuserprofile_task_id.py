# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-06 04:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0003_auto_20170806_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='aceuserprofile',
            name='task_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portalapp.Tasks'),
        ),
    ]