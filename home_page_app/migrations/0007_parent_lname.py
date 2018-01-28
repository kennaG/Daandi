# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page_app', '0006_parent_fname'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='lName',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
