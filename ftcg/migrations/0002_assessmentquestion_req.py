# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-25 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftcg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentquestion',
            name='req',
            field=models.IntegerField(default=0),
        ),
    ]
