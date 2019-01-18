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
import re
import hashlib


# 查询用户信息
def selectUser(name):
    if name :
        if len(name) >= 2:
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
    phone = request.GET['phone'];
    role = int(roles)
    callBackDict = {}
    if len(name) < 2:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '账号太短了'
        return callBackDict
    if len(token) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token验证失败'
        return callBackDict
    if len(phone) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '手机电话号码为空'
        return callBackDict
    # 匹配手机号
    # ret = re.match(r"^1[35678]\d{9}$", phone)
    # if ret is None:
    #     callBackDict['code'] = '0'
    #     callBackDict['msg'] = '手机号码验证失败'
    #     return callBackDict
    if role < 0 or role > 3:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '注册用户类型不存在'
        return callBackDict
    if role == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '管理员用户不支持注册'
        return callBackDict
    # 默认密码就是他的手机号
    hash = hashlib.md5()
    hash.update(str(phone).encode("utf-8"))
    md = hash.hexdigest()
    hash2 = hashlib.md5()
    hash2.update(str(md).encode("utf-8"))
    password = str(hash2.hexdigest())
    if role == 2 or role == 3:
        villageId = request.GET['villageId']
        if len(villageId) == 0:
            callBackDict['code'] = '0'
            callBackDict['msg'] = '用户所在小区不存在'
            return callBackDict
    try:
        # 查看登录的token
        if signAdmin.verificationToken(token) == False:
            callBackDict['code'] = '9999'
            callBackDict['msg'] = 'token异常，无法注册'
            return callBackDict
        # 查询用户信息
        userInfo = selectUser(name)
    	if isinstance(userInfo,user):
            callBackDict['code'] = '0'
            callBackDict['msg'] = '用户账号已存在'
        else:
            # 帐户不存在，进行创建用户信息
            createTime = int(time.time()*1000)
            obj = user.objects.create(name=name, password=password, createTime=createTime, role=role, phone=phone)
            obj.save()
            callBackDict['code'] = '1'
            dict = {'id':obj.id,'name':name,'phone':phone,'role':role}
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
        logger = logging.getLogger("django")
        logger.info(str(e))
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
        # 判断获取用户的信息
        if userObj.role == 2 or userObj.role == 3:
            callBackDict['code'] = '1'
            region = userConfigAdmin.selectUserAndStreetRS(signObj.userId)
            callBackDict['data'] = {"id": signObj.userId, "token": signObj.token, "name": userObj.name,
                                    "phone": userObj.phone, "role": userObj.role, "region": region}
        else:
            callBackDict['data'] = {"id": signObj.userId, "token": signObj.token, "name": userObj.name,
                                    "phone": userObj.phone, "role": userObj.role}
    except BaseException as e:
        logger = logging.getLogger("django")
        logger.info(str(e))
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
    return callBackDict



# 用户重置密码
def resetPassword(request):
    token = request.GET['token'];
    password = request.GET['password']
    oldPassword = request.GET['oldPassword']
    callBackDict = {}
    if len(token) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token错误'
        return callBackDict
    if len(password) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '新的密码错误'
        return callBackDict
    if len(oldPassword) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '老的密码错误'
        return callBackDict
    try:
        # 更新密码
        signObj = sign.objects.get(token=token)
        obj = user.objects.get(id=signObj.userId,password=oldPassword)
        obj.password = password
        obj.save()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '设置成功'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '密码错误'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 重置成功
def adminResetPassword(request):
    token = request.GET['token'];
    userId = request.GET['userId'];
    callBackDict = {}
    if len(userId) == 0 :
        callBackDict['code'] = '0'
        callBackDict['msg'] = '用户的id为空'
        return callBackDict
    if len(token) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token错误'
        return callBackDict
    try:
        # 查看管理员登录的token
        if signAdmin.verificationToken(token) == False:
            callBackDict['code'] = '9999'
            callBackDict['msg'] = 'token异常'
            return callBackDict
        # 查询出用户的信息
        obj = user.objects.get(id=userId)
        if obj.role == 0:
            callBackDict['code'] = '0'
            callBackDict['msg'] = '管理员账户无法重置'
            return callBackDict
        # 默认密码就是他的手机号
        hash = hashlib.md5()
        hash.update(str(obj.phone).encode("utf-8"))
        md = hash.hexdigest()
        # 两次加密
        hash2 = hashlib.md5()
        hash2.update(md.encode("utf-8"))
        password = str(hash2.hexdigest())
        obj.password = password
        obj.save()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '已重置为手机号为登录密码'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '重置失败'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 管理员获取所有用户
def getAllUserList(request):
    token = request.GET['token'];
    getpage = int(request.GET['page'])
    getpageSize = int(request.GET['pageSize'])
    callBackDict = {}
    if len(token) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token错误'
        return callBackDict
    # 验证token
    if signAdmin.verificationToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        userList = user.objects.all()[getpage*getpageSize:(getpage*getpageSize+getpageSize)]
        list = []
        for oneUser in userList:
            region = None
            if oneUser.role == 2:
                region = userConfigAdmin.selectUserAndStreetRS(oneUser.id)
            list.append({'id': oneUser.id, 'name': oneUser.name, 'role': oneUser.role, 'phone':oneUser.phone,"region":region})
        callBackDict['code'] = '1'
        callBackDict['data'] = list
        callBackDict['allPage'] = user.objects.all().count()
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 管理员删除用户
def adminDeleteUser(request):
    callBackDict = {}
    callBackDict['code'] = '0'
    callBackDict['msg'] = '请联系管理员进行删除'
    return callBackDict
    token = request.GET['token'];
    userId = request.GET['userId'];
    callBackDict = {}
    if len(token) != 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token错误'
        return callBackDict
    if len(userId) == 32:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'userId为空'
        return callBackDict
    # 验证token
    if signAdmin.verificationToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        user.objects.get(id=userId).delete()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '删除用户成功'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict


