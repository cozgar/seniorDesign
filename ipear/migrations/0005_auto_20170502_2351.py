# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipear', '0004_remove_profile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.PositiveIntegerField(null=True),
        ),
    ]