# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-14 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parsedresume',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='parsedresume',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='parsedresume',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
