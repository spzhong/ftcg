# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-08 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftcg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(max_length=64, null=True),
        ),
    ]