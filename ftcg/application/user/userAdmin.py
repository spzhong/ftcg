# -*- coding: utf-8 -*-
import logging
import django.utils.log
import logging.handlers
import json
import time
import sys
sys.path.append('...')
from ftcg.models import user
from ftcg.models import sign
from ftcg.models import village

import signAdmin
import userConfigAdmin


# 查询用户信息
def selectUser(name):
    if name :
        if len(name) > 4:
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



# 注册用户
def registerUser(request):
    name = request.GET['name'];
    token = request.GET['token'];
    roles = request.GET['role'];
    role = int(roles)
    callBackDict = {}
    if len(name) < 5:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '账号太短了'
        return callBackDict
    if len(token) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token验证失败'
        return callBackDict
    if len(token) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token验证失败'
        return callBackDict
    if role < 0 or role > 3:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '注册用户类型不存在'
        return callBackDict
    if role == 2 or role == 3:
        villageId = request.GET['villageId']
        if len(villageId) == 0:
            callBackDict['code'] = '0'
            callBackDict['msg'] = '用户所在小区不存在'
            return callBackDict
    else:
        password = request.GET['password'];
        if len(password) != 32:
            callBackDict['code'] = '0'
            callBackDict['msg'] = '账号密码错误'
            return callBackDict
    try:
        # 查看登录的token
        if signAdmin.verificationToken(token) == False:
            callBackDict['code'] = '0'
            callBackDict['msg'] = 'token异常，无法注册'
            return callBackDict
        # 查询用户信息
        userInfo = selectUser(name)
        logger = logging.getLogger("django")
        logger.info(str(userInfo))
    	if isinstance(userInfo,user):
            callBackDict['code'] = '0'
            callBackDict['msg'] = '用户账号已存在'
        else:
            # 帐户不存在，进行创建用户信息
            createTime = int(time.time()*1000)
            if password:
                obj = user.objects.create(name=name, password=password, createTime=createTime,role=role)
            else:
                obj = user.objects.create(name=name, createTime=createTime, role=role)
            obj.save()
            callBackDict['code'] = '1'
            dict = {'id':obj.id}
            #创建一条关联的用户和城市之间的关系
            if role == 2 or role == 3:
                #返回用户的区域信息
                regionDict = userConfigAdmin.createUserAndStreetRS(obj.id,villageId)
                if regionDict :
                    dict['region'] = regionDict
            # 插入一条的登录记录
            signObj = signAdmin.createSignRecord(obj.id)
            if isinstance(signObj, sign):
                dict['token'] = signObj.token
            callBackDict['data'] = dict
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
    return callBackDict



# 获取用户信息
def info(request):
    token = request.GET['token'];
    callBackDict = {}
    if len(token) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token错误'
        return callBackDict
    # 验证token
    try:
        signObj = sign.objects.get(token=token)
        userObj = user.objects.get(id=signObj.userId)
        callBackDict['code'] = '1'
        callBackDict['data'] = {"id": userObj.id,"name":userObj.name,"phone":userObj.phone,"role": userObj.role}
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
    return callBackDict



# 第一次修改密码
def firstPassword(request):
    token = request.GET['token'];
    password = request.GET['password'];
    callBackDict = {}
    if len(token) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token错误'
        return callBackDict
    if len(password) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '密码错误'
        return callBackDict
    try:
        # 更新密码
        signObj = sign.objects.get(token=token)
        obj = user.objects.get(id=signObj.userId)
        if obj.password :
            obj.password = password
            obj.save()
            callBackDict['code'] = '1'
            callBackDict['msg'] = '设置成功'
        else:
            callBackDict['code'] = '0'
            callBackDict['msg'] = '密码已经存在'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
    return callBackDict




# 重置成功
def adminResetPassword(request):
    token = request.GET['token'];
    callBackDict = {}
    if len(token) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token错误'
        return callBackDict
    try:
        # 更新密码
        signObj = sign.objects.get(token=token)
        obj = user.objects.get(id=signObj.userId)
        obj.password = None
        obj.save()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '设置成功'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '重置成功'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 管理员获取所有用户
def getAllUserList(request):
    token = request.GET['token'];
    callBackDict = {}
    if len(token) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token错误'
        return callBackDict
    # 验证token
    try:
        userList = user.objects.all()
        list = []
        for oneUser in userList:
            list.append({'id': oneUser.id, 'name': oneUser.name, 'role': oneUser.role, 'phone':oneUser.phone})
        callBackDict['code'] = '1'
        callBackDict['msg'] = list
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict
