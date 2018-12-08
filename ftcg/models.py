# -*- coding: utf-8 -*-

from django.db import models


class user(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    password = models.CharField(max_length=64,null=True)
    phone = models.CharField(max_length=15, null=True)
    role = models.IntegerField(default=0)
    createTime = models.BigIntegerField(default=0)


class sign(models.Model):
    id = models.UUIDField(primary_key=True)
    token = models.CharField(max_length=32)
    userId = models.IntegerField(db_index =True)
    signTime = models.BigIntegerField(default=0)


class sorting(models.Model):
    id = models.UUIDField(primary_key=True)
    villageId = models.IntegerField(default=0)
    streetId = models.IntegerField(default=0)


# 小区
class village(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)

# 街道
class street(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)

# 小区和街道的关系
class rsStreetVillage(models.Model):
    streetId = models.IntegerField(db_index=True)
    villageId = models.IntegerField(db_index=True)

# 用户和小区的关系
class rsUserVillage(models.Model):
    userId = models.IntegerField(db_index=True)
    villageId = models.IntegerField(db_index=True)


# 基础数据
obj1 = street.objects.create(name='福田街道')
obj1.save()

obj2 = village.objects.create(name='福田小区')
obj2.save()

obj3 = rsStreetVillage.objects.create(streetId=1,village=1)
obj3.save()