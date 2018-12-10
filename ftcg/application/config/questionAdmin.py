# -*- coding: utf-8 -*-
import logging
import django.utils.log
import logging.handlers
import json
import time
import sys
sys.path.append('...')
from ftcg.models import user
from ftcg.models import question
import django.utils.log
import configAdmin


# 创建问题
def baseConfigQuestion(request):
    callBackDict = {}
    title = request.GET['title']
    plusFraction = int(request.GET['plusFraction'])
    minusFraction = int(request.GET['minusFraction'])
    type = int(request.GET['type'])
    if len(title) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入问题的标题'
        return callBackDict
    if  plusFraction < 0 or plusFraction > 100:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入0-100的加分数'
        return callBackDict
    if  minusFraction < 0 or minusFraction > 100:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入0-100的减分数'
        return callBackDict
    if  type < 0 or type > 3:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入正确的问题分类'
        return callBackDict
    # 验证token
    if configAdmin.verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        obj = question.objects.create(title=title,type=type,plusFraction=plusFraction,minusFraction=minusFraction)
        obj.save()
        callBackDict['code'] = '1'
        callBackDict['data'] = obj.id
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '添加数据异常，请重试'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict


# 删除问题
def deleteConfigQuestion(request):
    callBackDict = {}
    questionId = request.GET['id']
    if len(questionId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入问题的id'
        return callBackDict
    # 验证token
    if configAdmin.verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        question.objects.get(id=questionId).delete()
        callBackDict['code'] = '1'
        callBackDict['data'] = '删除成功'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict


# 获取配置的问题
def getConfigQuestion(request):
    callBackDict = {}
    type = int(request.GET['type'])
    if type < 0 or type > 3:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入正确的问题分类'
        return callBackDict
    # 验证token
    if configAdmin.verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        questionList = question.objects.filter(type=type)
        list = []
        for oneQuestion in questionList:
            list.append({'id': oneQuestion.id, 'title': oneQuestion.title, 'plusFraction':oneQuestion.plusFraction,'minusFraction':oneQuestion.minusFraction,'type':oneQuestion.type})
        callBackDict['code'] = '1'
        callBackDict['data'] = list
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict