# -*- coding: utf-8 -*-
import logging
import django.utils.log
import logging.handlers
import json
import time
import sys
sys.path.append('...')
from ftcg.models import user


# 查询用户信息
def selectUser(name):
    if name :
        if len(name) > 5:
            try:
                oneUserList = user.objects.filter(name=name)
                if len(oneUserList) == 0:
	   	    return "账号不存在"
		return oneUserList[0]
            except BaseException as e:
                logger = logging.getLogger("django")
                logger.info(str(e))
                return "账号不存在"
        return "账号太短了";
    return "账号为空"


# 注册用户信息
def registerUser(request):
    name = request.GET['name'];
    code = request.GET['code'];
    callBackDict = {}
    if len(name) < 5:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '账号太短了'
        return callBackDict
    if len(code) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '账号密码多错误'
        return callBackDict
    try:
        # 查询用户信息
        userInfo = selectUser(name)
        logger = logging.getLogger("django")
        logger.info(str(userInfo))
	if isinstance(userInfo,user):
            callBackDict['code'] = '0'
            callBackDict['msg'] = '用户账号已存在'
        else:
            # 帐户不存在，进行创建用户信息
            createTime = str(int(time.time()*1000))
            obj = user.objects.create(name=name, code=code, createTime=createTime)
            obj.save()
            callBackDict['code'] = '1'
            dict = {'id':obj.id}
            callBackDict['data'] = dict
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict

# 更新用户信息
def updateUser(request):
    return

def signUser(request):
    callBackDict = {}

    return callBackDict
