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
    # 负责人（就是住户的信息）
    personCharge = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    # 备注
    remarks = models.CharField(max_length=1024, null=True)


# 小区
class village(models.Model):
    # 街道的id
    streetId = models.IntegerField(default=0, db_index=True)
    # 社区的id
    communityId = models.IntegerField(default=0, db_index=True)
    name = models.CharField(max_length=255)
    # 默认0是普通小区，1是学校，2是政府机关,3是收储运公司
    type = models.IntegerField(default=0)
    # 编号
    number = models.CharField(null=True,max_length=100)
    address = models.CharField(max_length=1024,null=True)
    # 负责人
    personCharge = models.CharField(max_length=100,null=True)
    phone  = models.CharField(max_length=20,null=True)
    # 备注
    remarks = models.CharField(max_length=1024,null=True)
    # 管理子目录数（管理多少户）
    managementSubsetNum = models.CharField(null=True,max_length=100)
    # 是否启用（0是开始，1是关闭）
    isOpen = models.IntegerField(default=0)


# 社区
class community(models.Model):
    streetId = models.IntegerField(default=0,db_index=True)
    name = models.CharField(max_length=255)
    # 编号
    number = models.CharField(null=True,max_length=100)
    address = models.CharField(max_length=1024,null=True)
    # 负责人
    personCharge = models.CharField(max_length=100,null=True)
    phone  = models.CharField(max_length=20,null=True)
    # 备注
    remarks = models.CharField(max_length=1024,null=True)
    # 管理子目录数（管理多少户）
    managementSubsetNum = models.CharField(null=True,max_length=100)


# 街道
class street(models.Model):
    name = models.CharField(max_length=255)
    # 编号
    number = models.CharField(null=True,max_length=100)
    address = models.CharField(max_length=1024,null=True)
    # 负责人
    personCharge = models.CharField(max_length=100,null=True)
    phone  = models.CharField(max_length=20,null=True)
    # 备注
    remarks = models.CharField(max_length=1024,null=True)
    # 管理子目录数（管理多少户）
    managementSubsetNum = models.CharField(null=True,max_length=100)



# 用户和小区的关系
class rsUserVillage(models.Model):
    userId = models.IntegerField(db_index=True)
    # 小区和用户的对应关系
    rsStreetVillageId = models.IntegerField(db_index=True)

# 二维码的袋子
class qrCode(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(max_length=1024,null=True)
    codeId = models.BigIntegerField(default=0,null=True)
    # 领取用户的id，前期暂时没有
    userId = models.IntegerField(db_index=True,null=True)
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


# 考核配置的问题
class assessmentQuestion(models.Model):
    # 一级指标的名称
    oneLevelName = models.CharField(max_length=30,db_index=True)
    # 简称
    shortName = models.CharField(max_length=512)
    # 描述
    info  = models.CharField(max_length=2024,null=True)
    # 分数
    fraction = models.IntegerField(default=0)
    # 答案-jsonListString
    answerJson = models.CharField(max_length=20240,null=True)
    # 默认0是普通小区，1是学校，2是政府机关，3是收储运公司
    subordinateType = models.IntegerField(default=0)
    # 0是基本指标（默认的，是减分项目），1是鼓励指标（加分项）
    assessmentType = models.IntegerField(default=0)


# 当前考核的问题聚合
class assessment(models.Model):
    # 此次考核所选的问题ID
    assessmentQuestionId = models.IntegerField(default=0, db_index=True)
    # 描述
    info = models.CharField(max_length=2024,null=True)
    # 图片
    imgs = models.CharField(max_length=2024, null=True)
    # 当前问题分数
    fraction = models.IntegerField(default=0)
    # 创建的时间
    createTime = models.BigIntegerField(default=0)


# 分拣员考核问题
class userAssessment(models.Model):
    # 考核的问题id
    assessmentId = models.IntegerField(default=0, db_index=True)
    userId = models.IntegerField(default=0, db_index=True)
    # 街道，社区，小区
    streetId = models.IntegerField(default=0,db_index=True)
    community = models.IntegerField(default=0,db_index=True)
    villageId = models.IntegerField(default=0,db_index=True)
    # 默认0是普通小区，1是学校，2是政府机关，3是收储运公司
    type = models.IntegerField(default=0)
    # 总积分
    totalFraction = models.IntegerField(default=0)
    # 是否是考核结束(0是进行中，1是已结束，2是已经删除)
    type = models.IntegerField(default=0)
    # 创建时间
    createTime = models.BigIntegerField(default=0)

