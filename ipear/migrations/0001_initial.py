# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('email_Address', models.CharField(max_length=100)),
                ('first_Name', models.CharField(max_length=40)),
                ('last_Name', models.CharField(max_length=40)),
                ('age', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('phone_Number', models.CharField(max_length=11)),
                ('pets', models.TextField()),
                ('allergies', models.TextField()),
                ('existing_Conditions', models.TextField()),
                ('firearms', models.TextField()),
            ],
        ),
    ]
