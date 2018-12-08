# -*- coding: utf-8 -*-
import logging
import uuid

import django.utils.log
import logging.handlers
import json
import time
import sys

import hashlib

sys.path.append('...')
from ftcg.models import village
from ftcg.models import street
from ftcg.models import rsStreetVillage
from ftcg.models import rsUserVillage


# 创建一条用户和小区的关系
def createUserAndStreetRS(userId,villageId):
    try:
        # 查询小区
        villageObj = village.objects.get(id=villageId)

        # 查询小区-和街道的关系
        rsStreetVillageObj = rsStreetVillage.objects.get(villageId=villageId)
        streetId = rsStreetVillageObj.streetId

        # 查询街道的名称
        streetObj = street.objects.get(id=streetId)

        # 创建一条用户和小区的关系
        obj = rsUserVillage.objects.create(userId=userId, villageId=villageId)
        obj.save()
        regionDict = {'villageId':villageId,'villageName':villageObj.name,'streetId':streetId,'streetName':streetObj.name}
        return regionDict
    except BaseException as e:
        logger = logging.getLogger("django")
        logger.info(str(e))
        return None


# 查询用户所在的街道和小区的关系
def selectUserAndStreetRS(userId):
    try:
        # 查询小区-和街道的关系
        rsStreetVillageObj = rsStreetVillage.objects.get(userId=userId)
        streetId = rsStreetVillageObj.streetId
        villageId = rsStreetVillageObj.villageId

        # 查询街道和小区的关系
        streetObj = street.objects.get(id=streetId)
        villageObj = village.objects.get(id=villageId)

        # 返回用户和小区及街道的关系
        return {'villageId':villageId,'villageName':villageObj.name,'streetId':streetId,'streetName':streetObj.name}
    except BaseException as e:
        logger = logging.getLogger("django")
        logger.info(str(e))
        return None



