# -*- coding: utf-8 -*-
import logging
import django.utils.log
import logging.handlers
import json
import time
import sys
sys.path.append('...')
from ftcg.models import user
from ftcg.models import assessmentType
import django.utils.log
import configAdmin



/**
 * @api {get} config/baseConfigAssessment  [ok]添加考核分类
 * @apiVersion 0.1.0
 * @apiName baseConfigAssessment
 * @apiGroup BaseConfig
 *
 * @apiParam  {String}  token 管理员的token
 * @apiParam  {String}  {"levelTitle":"一级指标","fraction":"分数","levelList":[{"levelTitle":"二级指标","fraction":"分数","info":"具体要求","evaluationCriterionList":[{"criterionTitle":"评价标准1","fraction":"分数"},{"criterionTitle":"评价标准2","fraction":"分数"}]},{"levelTitle":"二级指标","fraction":"分数","info":"具体要求","evaluationCriterionList":[{"criterionTitle":"评价标准1","fraction":"分数"},{"criterionTitle":"评价标准2","fraction":"分数"}]}]}
 * @apiParam  {String}  subordinateType 0是小区的考核，1是学校，2是政府机关的考核
 * @apiParam  {String}  assessmentType  0是基本指标（默认的，是减分项目），1是鼓励指标（加分项）



# 创建问题
def baseConfigAssessment(request):
    callBackDict = {}
    title = request.GET['title']
    subordinateType = int(request.GET['subordinateType'])
    assessmentType = int(request.GET['assessmentType'])
    levelJsonString = request.GET['levelJsonString']
    if subordinateType < 0 or subordinateType > 2:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入小区或学校或机关的考核类型'
        return callBackDict
    if assessmentType < 0 or assessmentType > 1:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入基本指标或鼓励指标'
        return callBackDict
    if  len(levelJsonString) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入考核分类项目'
        return callBackDict
    # 验证token
    if configAdmin.verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        # 解读json数据
        levelJson = json.loads(levelJsonString)
        leveOneIndex = 0
        leveToalfraction = 0
        for leveJson in levelJson['levelList']:
            leveJson['index'] = str(leveOneIndex)
            # 获取考核的标准
            evaluationCriterionList = leveJson['evaluationCriterionList']
            leveTwoIndex = 0
            leveTwofraction = 0
            for evaluationCriterion in evaluationCriterionList:
                evaluationCriterion['index'] = str(leveTwoIndex)
                leveTwofraction = leveTwofraction + int(evaluationCriterion['fraction'])
                leveTwoIndex = leveTwoIndex + 1;
            if leveTwofraction !=  int(leveJson['fraction']) :
                callBackDict['code'] = '0'
                callBackDict['msg'] = '评价标准扣分项不等于二级指标的总分数'
                return callBackDict
            leveToalfraction = leveToalfraction+int(leveJson['fraction'])
            leveOneIndex = leveOneIndex+1;
        if int(levelJson['fraction']) == leveToalfraction :
            newlevelJsonString = json.dumps(levelJson)
            obj = assessmentType.objects.create(subordinateType=subordinateType, assessmentType=assessmentType,levelJsonString=newlevelJsonString)
            obj.save()
            callBackDict['code'] = '1'
            callBackDict['data'] = obj.id
        else:
            callBackDict['code'] = '0'
            callBackDict['msg'] = '二级指标的分数累积不等一级指标的分数'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '添加数据项目异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict


# 删除问题
def deleteConfigAssessment(request):
    callBackDict = {}
    assessmentTypeId = request.GET['id']
    if len(assessmentTypeId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入考核分类的id'
        return callBackDict
    # 验证token
    if configAdmin.verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        assessmentType.objects.get(id=assessmentTypeId).delete()
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
    subordinateType = int(request.GET['subordinateType']) # 0是小区的考核，1是学校考核，2是机关的考核
    assessmentType = int(request.GET['subordinateType']) # 0是基本指标（默认的，是减分项目），1是鼓励指标（加分项）
    if subordinateType < 0 or subordinateType > 2:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入小区或学校或机关的考核类型'
        return callBackDict
    if assessmentType < 0 or assessmentType > 1:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请输入基本指标或鼓励指标'
        return callBackDict
    # 验证token
    if configAdmin.verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        assessmentTypeList = assessmentType.objects.filter(subordinateType=subordinateType,assessmentType=assessmentType)
        list = []
        for oneassessmentType in assessmentTypeList:
            levelJsonString = oneassessmentType.levelJsonString
            levelList = json.loads(levelJsonString)
            list.append({'id': oneassessmentType.id, 'subordinateType': oneassessmentType.subordinateType, 'assessmentType':oneassessmentType.assessmentType,'levelList':levelList})
        callBackDict['code'] = '1'
        callBackDict['data'] = list
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict
