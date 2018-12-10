# -*- coding: utf-8 -*-
import logging
import django.utils.log
import logging.handlers
import json
import time
import sys
sys.path.append('...')
from ftcg.models import user
from ftcg.models import roomNumber
import django.utils.log
import configAdmin


# 关联小区和房间号
def addRoomNum(request):
    callBackDict = {}
    numberText = request.GET['numberText']
    villageId = request.GET['villageId']
    if len(numberText) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入具体房间号'
        return callBackDict
    if len(villageId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入小区的id'
        return callBackDict
    # 验证token
    if configAdmin.verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        obj = roomNumber.objects.create(numberText=numberText,villageId=villageId)
        obj.save()
        callBackDict['code'] = '1'
        callBackDict['data'] = obj.id
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '添加房间异常，请重试'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict


# 删除关联小区和房间号
def deleteRoomNum(request):
    callBackDict = {}
    roomId = request.GET['id']
    if len(roomId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入房间的id'
        return callBackDict
    # 验证token
    if configAdmin.verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        roomNumber.objects.get(id=roomId).delete()
        callBackDict['code'] = '1'
        callBackDict['data'] = '删除成功'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '已经删除'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 获取关联小区和房间号
def getRoomNumList(request):
    callBackDict = {}
    villageId = request.GET['villageId']
    if len(villageId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入小区的id'
        return callBackDict
    # 验证token
    if configAdmin.verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        roomNumList = roomNumber.objects.filter(villageId=villageId)
        list = []
        for oneRoom in roomNumList:
            list.append({'id': oneRoom.id, 'numberText': oneRoom.numberText, 'villageId': oneRoom.villageId})
        callBackDict['code'] = '1'
        callBackDict['data'] = list
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '获取数据异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict
