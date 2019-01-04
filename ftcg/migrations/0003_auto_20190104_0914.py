# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-04 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftcg', '0002_assessmentquestion_req'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userassessment',
            name='assessmentId',
        ),
        migrations.AddField(
            model_name='assessment',
            name='userAssessmentId',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='userassessment',
            name='correctTotalFraction',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userassessment',
            name='state',
            field=models.IntegerField(default=0),
        ),
    ]