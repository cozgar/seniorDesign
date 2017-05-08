# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipear', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DispatcherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('first_Name', models.CharField(max_length=40)),
                ('last_Name', models.CharField(max_length=40)),
                ('isDispatcher', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='isDispatcher',
            field=models.BooleanField(default=False),
        ),
    ]