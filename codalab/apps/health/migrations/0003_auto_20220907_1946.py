# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-09-07 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_storagedatapoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitionStorageDataPoint',
            fields=[
                ('competition_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('creator', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('submissions', models.BigIntegerField(default=0)),
                ('datasets', models.BigIntegerField(default=0)),
                ('dumps', models.BigIntegerField(default=0)),
                ('bundle', models.BigIntegerField(default=0)),
                ('total', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StorageSnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bucket_name', models.CharField(max_length=255)),
                ('total_use', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StorageUsageHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bucket_name', models.CharField(max_length=255)),
                ('at_date', models.DateTimeField()),
                ('usage', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserStorageDataPoint',
            fields=[
                ('user_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('competitions_total', models.BigIntegerField(default=0)),
                ('datasets_total', models.BigIntegerField(default=0)),
                ('submissions_total', models.BigIntegerField(default=0)),
                ('total', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='StorageDataPoint',
        ),
    ]
