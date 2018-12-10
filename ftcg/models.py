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


# 小区的房间号
class roomNumber(models.Model):
    numberText = models.CharField(max_length=1024)
    villageId = models.IntegerField(default=0,db_index=True)


# 小区
class village(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    # 默认0是普通小区，1是学校，2是政府机关
    type = models.IntegerField(default=0)


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


# 二维码的袋子
class qrCode(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(max_length=1024,null=True)
    codeId = models.BigIntegerField(default=0,null=True)
    # 领取用户的id，前期暂时没有
    userId = models.IntegerField(db_index=True,null=True)
    # 用户的房间号
    roomNumber = models.IntegerField(db_index=True,null=True)
    # 袋子领取的时间
    createTime = models.BigIntegerField(default=0)


# 分拣
class sorting(models.Model):
    villageId = models.IntegerField(default=0)
    streetId = models.IntegerField(default=0)
    remarks = models.CharField(max_length=2024,null=True)
    imgs = models.CharField(max_length=2024,null=True)
    # 二维码的id，允许为空
    qrCodeId = models.UUIDField(null=True)
    createTime = models.BigIntegerField(default=0)


# 考核
class assessment(models.Model):
    villageId = models.IntegerField(default=0,db_index=True)
    streetId = models.IntegerField(default=0,db_index=True)
    createTime = models.BigIntegerField(default=0)
    # 考核的状态 0是默认开始，1是结束，2是中断没有提交的
    state = models.IntegerField(default=0)
    # 总积分
    totalIntegral = models.IntegerField(default=0)


# 考核及相关的问题的关系
class assessmentQuestion(models.Model):
    assessmentId = models.IntegerField(default=0,db_index=True)
    questionId = models.IntegerField(default=0,db_index=True)
    remarks = models.CharField(max_length=2024,null=True)
    imgs = models.CharField(max_length=2024,null=True)
    createTime = models.BigIntegerField(default=0)
    # 选中的是加分还是减分（1是加分，2是减分）
    isplusormin = models.IntegerField(default=0)


# 考核的问题
class question(models.Model):
    title = models.CharField(max_length=2024)
    plusFraction = models.IntegerField(default=0)
    minusFraction = models.IntegerField(default=0)
    # 默认0是普通小区，1是学校，2是政府机关
    type = models.IntegerField(default=0)