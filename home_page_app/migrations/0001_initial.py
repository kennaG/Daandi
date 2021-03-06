# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-10 04:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='parent',
            fields=[
                ('ParentID', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('UserName', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('password', models.IntegerField(blank=True, default=None, null=True)),
                ('ParentCode', models.IntegerField(blank=True, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('student_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('studentCode', models.IntegerField(default=None)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
