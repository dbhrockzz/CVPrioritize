# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-06 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_auto_20180803_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='file',
            field=models.FileField(upload_to='resume/'),
        ),
    ]
