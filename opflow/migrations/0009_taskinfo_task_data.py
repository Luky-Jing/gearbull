# -*- coding: utf-8 -*-
"""
# Generated by Django 1.10.6 on 2017-05-02 09:49
"""
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):
    """ Migration """

    dependencies = [
        ('zhongjing', '0008_taskinfo_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskinfo',
            name='task_data',
            field=jsonfield.fields.JSONField(default={}),
        ),
    ]