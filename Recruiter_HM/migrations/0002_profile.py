# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-30 08:26
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Recruiter_HM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AID', models.CharField(max_length=7, validators=[django.core.validators.MinLengthValidator(7)])),
                ('role', models.CharField(max_length=17, validators=[django.core.validators.MinLengthValidator(9)])),
                ('updated_timestamp', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
