# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-22 06:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='create',
            new_name='created',
        ),
    ]
