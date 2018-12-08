# -*- coding: utf-8 -*-
import logging
import django.utils.log
import logging.handlers
import json
import time
import sys
sys.path.append('...')
from ftcg.models import street
from ftcg.models import village
from ftcg.models import rsStreetVillage
from django.db import IntegrityError, transaction
from django.db import transaction

def baseConfigQuestion(request):
    callBackDict = {}
    return callBackDict

def baseConfigStreet(request):
    name = request.GET['name'];
    callBackDict = {}
    if len(name) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '街道名称为空'
        return callBackDict
    try:
        obj = street.objects.create(name=name)
        obj.save()
        callBackDict['code'] = '1'
        callBackDict['data'] = obj.id
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
    return callBackDict


def baseConfigVillage(request):
    streetId = request.GET['streetId'];
    name = request.GET['name'];
    callBackDict = {}
    if len(streetId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '所属街道ID为空'
        return callBackDict
    if len(name) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '小区名称为空'
        return callBackDict
    # 开启一个事物
    try:
        #创建一个小区
        obj = village.objects.create(name=name)
        obj.save()
        # 小区和街道的关系
        rsStreetVillageObj = rsStreetVillage.objects.create(streetId=streetId,villageId=obj.id)
        rsStreetVillageObj.save()
        callBackDict['code'] = '1'
        callBackDict['data'] = obj.id
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
    return callBackDict