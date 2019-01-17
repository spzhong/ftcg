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
from ftcg.models import community
from ftcg.models import rsUserVillage


# 创建一条用户和小区的关系
def createUserAndStreetRS(userId,villageId):
    try:
        # 查询小区
        villageObj = village.objects.get(id=villageId)

        # 查询街道的名称
        streetObj = street.objects.get(id=villageObj.streetId)

        # 查查询社区的名称
        communityObj = community.objects.get(id=villageObj.communityId)

        # 创建一条用户和小区的关系
        obj = rsUserVillage.objects.create(userId=userId, rsStreetVillageId=villageId)
        obj.save()
        regionDict = {'villageInfo': {'id': villageId, 'name': villageObj.name, 'type': villageObj.type,
                                      'number': villageObj.number, 'address': villageObj.address,
                                      'personCharge': villageObj.personCharge, 'phone': villageObj.phone,
                                      'remarks': villageObj.remarks,
                                      'managementSubsetNum': villageObj.managementSubsetNum},
                      'communityInfo': {'id': communityObj.id, 'name': communityObj.name, 'number': villageObj.number,
                                        'address': villageObj.address, 'personCharge': villageObj.personCharge,
                                        'phone': villageObj.phone, 'remarks': villageObj.remarks,
                                        'managementSubsetNum': villageObj.managementSubsetNum},
                      'streetInfo': {'id': streetObj.id, 'name': streetObj.name, 'number': villageObj.number,
                                     'address': villageObj.address, 'personCharge': villageObj.personCharge,
                                     'phone': villageObj.phone, 'remarks': villageObj.remarks,
                                     'managementSubsetNum': villageObj.managementSubsetNum}}
        return regionDict
    except BaseException as e:
        logger = logging.getLogger("django")
        logger.info(str(e))
        return None


# 查询用户所在的街道和小区的关系
def selectUserAndStreetRS(userId):
    try:
        # 查询小区-和用户的
        rsUserVillageObj = rsUserVillage.objects.get(userId=userId)

        # 获取用户的城市的ID
        villageId = rsUserVillageObj.rsStreetVillageId

        # 查询小区
        villageObj = village.objects.get(id=villageId)

        # 查询街道的名称
        streetObj = street.objects.get(id=villageObj.streetId)

        # 查询社区的名称
        communityObj = community.objects.get(id=villageObj.communityId)

        regionDict = {'villageInfo': {'id': villageId, 'name': villageObj.name, 'type': villageObj.type,
                                      'number': villageObj.number, 'address': villageObj.address,
                                      'personCharge': villageObj.personCharge, 'phone': villageObj.phone,
                                      'remarks': villageObj.remarks,
                                      'managementSubsetNum': villageObj.managementSubsetNum},
                      'communityInfo': {'id': communityObj.id, 'name': communityObj.name, 'number': villageObj.number,
                                        'address': villageObj.address, 'personCharge': villageObj.personCharge,
                                        'phone': villageObj.phone, 'remarks': villageObj.remarks,
                                        'managementSubsetNum': villageObj.managementSubsetNum},
                      'streetInfo': {'id': streetObj.id, 'name': streetObj.name, 'number': villageObj.number,
                                     'address': villageObj.address, 'personCharge': villageObj.personCharge,
                                     'phone': villageObj.phone, 'remarks': villageObj.remarks,
                                     'managementSubsetNum': villageObj.managementSubsetNum}}
        # 返回用户和小区及街道的关系
        return regionDict
    except BaseException as e:
        logger = logging.getLogger("django")
        logger.info(str(e))
        return None


# 查询用户所在的街道和小区的关系
def selectStreetcommunityvillage(streetId,communityId,villageId):
    try:
        # 查询小区
        villageObj = village.objects.get(id=villageId)

        # 查询街道的名称
        streetObj = street.objects.get(id=streetId)

        # 查询社区的名称
        communityObj = community.objects.get(communityId)

        regionDict = {'villageInfo': {'id': villageId, 'name': villageObj.name, 'type': villageObj.type,
                                      'number': villageObj.number, 'address': villageObj.address,
                                      'personCharge': villageObj.personCharge, 'phone': villageObj.phone,
                                      'remarks': villageObj.remarks,
                                      'managementSubsetNum': villageObj.managementSubsetNum},
                      'communityInfo': {'id': communityObj.id, 'name': communityObj.name, 'number': villageObj.number,
                                        'address': villageObj.address, 'personCharge': villageObj.personCharge,
                                        'phone': villageObj.phone, 'remarks': villageObj.remarks,
                                        'managementSubsetNum': villageObj.managementSubsetNum},
                      'streetInfo': {'id': streetObj.id, 'name': streetObj.name, 'number': villageObj.number,
                                     'address': villageObj.address, 'personCharge': villageObj.personCharge,
                                     'phone': villageObj.phone, 'remarks': villageObj.remarks,
                                     'managementSubsetNum': villageObj.managementSubsetNum}}
        # 返回用户和小区及街道的关系
        return regionDict
    except BaseException as e:
        logger = logging.getLogger("django")
        logger.info(str(e))
        return None