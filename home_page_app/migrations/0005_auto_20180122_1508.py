# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 23:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_page_app', '0004_auto_20180120_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='parent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home_page_app.student'),
        ),
    ]
