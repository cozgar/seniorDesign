# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 23:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipear', '0005_auto_20170502_2351'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DispatcherInfo',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
