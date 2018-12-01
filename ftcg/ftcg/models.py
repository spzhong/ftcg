# -*- coding: utf-8 -*-

from django.db import models


class user(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    code = models.CharField(max_length=32)
    phone = models.CharField(max_length=15, null=True)
    createTime = models.CharField(null=True, max_length=20)


class sign(models.Model):
    id = models.UUIDField(primary_key=True)
    token = models.CharField(max_length=32)
    userId = models.IntegerField(db_index =True)
    signTime = models.CharField(null=True,max_length=20)
