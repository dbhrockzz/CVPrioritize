# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-30 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruiter_HM', '0003_auto_20180730_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='updated_timestamp',
            field=models.DateField(null=True),
        ),
    ]
