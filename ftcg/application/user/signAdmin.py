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
from ftcg.models import user
from ftcg.models import sign
import userConfigAdmin

def signIn(request):
    name = request.GET('name')
    password = request.GET('password')
    callBackDict = {}
    if len(name) < 5:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '账号太短了'
        return callBackDict
    if len(password) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '密码错误'
        return callBackDict
    try:
        userObj = user.objects.get(name=name)
        logger = logging.getLogger("django")
        logger.info(userObj.password)
        logger.info(password)
        if userObj.password == password:
            signObj = createSignRecord(userObj.id)
            if isinstance(signObj, sign):
                callBackDict['code'] = '1'
                # 物业管理员和小区的用户，需要锁定其管理的区域
                if signObj.role == 2 | signObj.role == 3:
                    region = userConfigAdmin.selectUserAndStreetRS(signObj.userId)
                    callBackDict['data'] = {"id": signObj.userId, "token": signObj.token, "role": signObj.role ,"region":region}
                else:
                    callBackDict['data'] = {"id":signObj.userId,"token":signObj.token,"role":signObj.role}
            else:
                callBackDict['code'] = '0'
                callBackDict['msg'] = '登录异常'
        else:
            callBackDict['code'] = '0'
            callBackDict['msg'] = '账号密码错误'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '账号不存在'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict

# 登出操作
def signOut(request):
    callBackDict = {}
    return callBackDict


# 创建一条的登录记录
def createSignRecord(userId):
    try:
        logger = logging.getLogger("django")
        createTime = int(time.time() * 1000)
        # 两次加密
        hash = hashlib.md5()
        hash.update(str(createTime))
        md = hash.hexdigest()
        hash.update(str(md))
        token = str(hash.hexdigest())
        uid = str(uuid.uuid1())
        obj = sign.objects.create(id=uid, token=token, userId=userId, signTime=createTime)
        obj.save()
        return obj
    except BaseException as e:
        logger.info(str(e))
        return "登录异常"


# 验证token
def verificationToken(token):
    nowTime = int(time.time() * 1000)
    try:
        signList = sign.objects.filter(token=token,signTime__lte = (nowTime - 7 * 24 * 3600))
        if len(signList) == 0:
            return False
        return True
    except BaseException as e:
        return False
