# -*- coding: utf-8 -*-
import logging
import uuid

import django.utils.log
import logging.handlers
import json
import time
import sys

from Crypto.Hash import MD5

sys.path.append('...')
from ftcg.models import user
from ftcg.models import sign

def sign(request):
    name = request.GET['name'];
    code = request.GET['code'];
    callBackDict = {}
    if len(name) < 5:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '账号太短了'
        return callBackDict
    if len(code) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '账号密码错误'
        return callBackDict
    try:
        oneUserList = user.objects.filter(name=name, code=code)
        if len(oneUserList) == 0:
            userObj = oneUserList[0]
            callBackDict['code'] = '1'
            callBackDict['data'] = createSignRecord(userObj.id)
        else:
            callBackDict['code'] = '0'
            callBackDict['msg'] = '账号密码错误'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '账号不存在'
    return callBackDict

# 登出操作
def signOut(request):
    callBackDict = {}
    return callBackDict


# 创建一条的登录记录
def createSignRecord(userId):
    try:
        createTime = int(time.time() * 1000)
        token = MD5(MD5(str(createTime)))
        uid = str(uuid.uuid1())
        obj = sign.objects.create(id=uid, token=token, userId=userId, signTime=createTime)
        obj.save()
        return obj
    except BaseException as e:
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
