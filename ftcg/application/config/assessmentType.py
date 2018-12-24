# -*- coding: utf-8 -*-
import logging
import django.utils.log
import logging.handlers
import json
import time
import sys
sys.path.append('...')
from ftcg.models import user
from ftcg.models import assessmentQuestion
import django.utils.log
import configAdmin


# 验证为空的Parm信息
def verificationNullParm(request,parm):
    try:
        return request.GET[parm]
    except BaseException as e:
        return None


# 创建问题
def baseConfigAssessment(request):
    callBackDict = {}
    # 默认0是普通小区，1是学校，2是政府机关，3是收储运公司
    subordinateTypeInt = int(request.GET['subordinateType'])
    # 0是基本指标（默认的，是减分项目），1是鼓励指标（加分项）
    assessmentTypeInt = int(request.GET['assessmentType'])
    oneLevelName_parm = request.GET['oneLevelName']
    shortName_parm = request.GET['shortName']
    info_parm = request.GET['info']
    fraction_parm = int(request.GET['fraction'])
    answerJson_parm = request.GET['answerJson']
    if subordinateTypeInt < 0 or subordinateTypeInt > 3:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入小区或学校或机关的考核类型'
        return callBackDict
    if assessmentTypeInt < 0 or assessmentTypeInt > 1:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入基本指标或鼓励指标'
        return callBackDict
    if len(oneLevelName_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入一级考核标题'
        return callBackDict
    if len(shortName_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入二级考核标题'
        return callBackDict
    if len(info_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入考核的问题'
        return callBackDict
    if fraction_parm < 0 or fraction_parm > 99:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请正确输入考核分数的1-99分'
        return callBackDict
    if len(answerJson_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入考核问题的答案'
        return callBackDict
    try:
        answerJsonList = json.loads(answerJson_parm)
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '考核问题答json结构异常'
        return callBackDict
    # 验证token
    if configAdmin.verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        # 给问题附加索引
        leveOneIndex = 0
        for oneAnswer in answerJsonList:
            oneAnswer['index'] = str(leveTwoIndex)
            leveTwoIndex = leveOneIndex + 1;
        newAnswerJsonList = json.dumps(answerJsonList)
        obj = assessmentQuestion.objects.create(fraction=fraction_parm,info=info_parm,shortName=shortName_parm,oneLevelName=oneLevelName_parm,subordinateType=subordinateTypeInt, assessmentType=assessmentTypeInt,
                                                answerJson=newAnswerJsonList)
        obj.save()
        callBackDict['code'] = '1'
        callBackDict['data'] = obj.id
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict


# 编辑问题
def editConfigAssessment(request):
    callBackDict = {}
    assessmentQuestionId = request.GET['id']
    if len(assessmentQuestionId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入考核的问题id'
        return callBackDict
    oneLevelName_parm = verificationNullParm(request,'oneLevelName')
    shortName_parm = verificationNullParm(request, 'shortName')
    info_parm = verificationNullParm(request, 'info')
    fraction_parm = verificationNullParm(request, 'fraction')
    answerIndex_parm = verificationNullParm(request, 'answerIndex')
    answerDes_parm = verificationNullParm(request, 'answerDes')
    # 验证token
    if configAdmin.verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        assessmentQuestionobj = assessmentQuestion.objects.get(id = assessmentQuestionId)
        if oneLevelName_parm:
            assessmentQuestionobj.oneLevelName = oneLevelName_parm
        if shortName_parm:
            assessmentQuestionobj.shortName = shortName_parm
        if info_parm:
            assessmentQuestionobj.info = info_parm
        if fraction_parm:
            assessmentQuestionobj.fraction = fraction_parm
        if answerIndex_parm:
            answerJsonList = json.loads(assessmentQuestionobj.answerJson)
            dicOneAnser = answerJsonList[answerIndex_parm]
            dicOneAnser.des = answerDes_parm
        assessmentQuestionobj.save()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '更新成功'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict


# 删除问题
def deleteConfigAssessment(request):
    callBackDict = {}
    assessmentTypeId = request.GET['id']
    if len(assessmentTypeId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入考核的问题id'
        return callBackDict
    # 验证token
    if configAdmin.verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        assessmentQuestion.objects.get(id=assessmentTypeId).delete()
        callBackDict['code'] = '1'
        callBackDict['data'] = '删除成功'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '已经删除'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 获取配置的问题
def getConfigAssessment(request):
    callBackDict = {}
    subordinateTypeInt = int(request.GET['subordinateType']) # 0是小区的考核，1是学校考核，2是机关的考核，3是收储运公司
    if subordinateTypeInt < 0 or subordinateTypeInt > 3:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入小区或学校或机关的考核类型'
        return callBackDict
    try:
        assessmentTypeList = assessmentQuestion.objects.filter(subordinateType=subordinateTypeInt)
        list = []
        for oneassessmentType in assessmentTypeList:
            levelJsonString = oneassessmentType.answerJson
            anserList = json.loads(levelJsonString)
            list.append({'id': oneassessmentType.id, 'subordinateType': oneassessmentType.subordinateType, 'assessmentType':oneassessmentType.assessmentType,'fraction':oneassessmentType.fraction,'info':oneassessmentType.info,'shortName':oneassessmentType.shortName,'oneLevelName':oneassessmentType.oneLevelName,'answerJson':anserList})
        callBackDict['code'] = '1'
        callBackDict['data'] = list
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict
