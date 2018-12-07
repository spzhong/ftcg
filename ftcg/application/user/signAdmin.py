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

def signIn(request):
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
        logger = logging.getLogger("django")
        createTime = int(time.time() * 1000)
        m2 = hashlib.md5()
        # 两次计算MD5
        m2.update(str(createTime).encode('utf-8'))
        token = m2.update(str(m2.hexdigest()))

        logger.info('token:'+token);
        uid = str(uuid.uuid1())
        logger.info('uid:' + uid);
        logger.info('userId:' + userId);
        logger.info('signTime:' + str(createTime));

        obj = sign.objects.create(id=uid, token=token, userId=userId, signTime=createTime)
        obj.save()
        logger.info("插入正常")
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
