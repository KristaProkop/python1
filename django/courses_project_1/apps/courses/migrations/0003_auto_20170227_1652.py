# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170227_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default='blank', max_length=1000),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]
