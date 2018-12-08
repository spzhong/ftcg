# -*- coding: utf-8 -*-

from django.db import models


class user(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    code = models.CharField(max_length=32,null=True)
    phone = models.CharField(max_length=15, null=True)
    role = models.IntegerField(default=0)
    createTime = models.CharField(default=0,max_length=30)


class sign(models.Model):
    id = models.UUIDField(primary_key=True)
    token = models.CharField(max_length=32)
    userId = models.IntegerField(db_index =True)
    signTime = models.CharField(default=0,max_length=30)


class sorting (models.Model):
    id = models.UUIDField(primary_key=True)
    villageId = models.IntegerField(default=0)
    streetId = models.IntegerField(default=0)



