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
from ..user import signAdmin


# 验证token
def verificationToken(request):
    token = request.GET['token'];
    if len(token) == 32:
        return signAdmin.verificationToken(token)
    return False


def baseConfigQuestion(request):
    callBackDict = {}
    return callBackDict


# 创建街道的数据
def baseConfigStreet(request):
    name = request.GET['name'];
    callBackDict = {}
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return
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


# 创建小区的数据
def baseConfigVillage(request):
    streetId = request.GET['streetId'];
    name = request.GET['name'];
    callBackDict = {}
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return
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


# 获取所有街道的数据
def getStreets(request):
    callBackDict = {}
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return
    try:
        streetList = street.objects.all()
        list = []
        for oneStreet in streetList:
            list.append({'id':oneStreet.id,'name':oneStreet.name})
        callBackDict['code'] = '1'
        callBackDict['msg'] = list
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
    return callBackDict


# 获取指定街道的小区数据
def getVillages(request):
    callBackDict = {}
    streetId = request.GET['streetId']
    if len(streetId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '所属街道ID为空'
        return callBackDict
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return
    try:
        villageList = village.objects.all()
        list = []
        for onevillage in villageList:
            list.append({'id': onevillage.id, 'name': onevillage.name})
        callBackDict['code'] = '1'
        callBackDict['msg'] = list
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
    return callBackDict


# 删除街道
def deleteStreet(request):
    callBackDict = {}
    streetId = request.GET['streetId']
    if len(streetId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '所属街道ID为空'
        return callBackDict
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return
    try:
        # 执行删除数据及关系
        street.objects.filter(id=streetId).delete()
        rsStreetVillage.objects.filter(streetId=streetId).delete()
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
    return callBackDict


# 删除小区
def deleteVillage(request):
    callBackDict = {}
    villageId = request.GET['villageId']
    if len(villageId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '删除的小区ID为空'
        return callBackDict
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return
    try:
        # 执行删除数据及关系
        village.objects.filter(id=villageId).delete()
        rsStreetVillage.objects.filter(villageId=villageId).delete()
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
    return callBackDict

