# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-06 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftcg', '0005_auto_20190106_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='qrCodeId',
            field=models.CharField(db_index=True, max_length=512, null=True),
        ),
    ]
