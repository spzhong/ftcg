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
    token = models.CharField(max_length=32,db_index=True)
    userId = models.IntegerField(db_index =True)
    signTime = models.BigIntegerField(default=0)



class sorting(models.Model):
    id = models.UUIDField(primary_key=True)
    villageId = models.IntegerField(default=0)
    streetId = models.IntegerField(default=0)


# 小区
class village(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    # 默认0是普通小区，1是学校，2是政府机关
    type = models.IntegerField(default=0)

# 街道
class street(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255, db_index=True, unique=True)

# 小区和街道的关系
class rsStreetVillage(models.Model):
    streetId = models.IntegerField(db_index=True)
    villageId = models.IntegerField(db_index=True)

# 用户和小区的关系
class rsUserVillage(models.Model):
    userId = models.IntegerField(db_index=True)
    villageId = models.IntegerField(db_index=True)