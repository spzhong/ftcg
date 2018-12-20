# -*- coding: utf-8 -*-
import logging
import django.utils.log
import logging.handlers
import json
import time
import sys
sys.path.append('...')
from ftcg.models import user
from ftcg.models import userAssessment
from ftcg.models import assessment
from ftcg.models import assessmentType
from ftcg.models import village


from ..user import signAdmin

# 创建考核
def createAssessment(request):
    token = request.GET['token'];
    getstreetId = request.GET['streetId'];
    getvillageId = request.GET['villageId'];
    getuserId = request.GET['userId'];
    callBackDict = {}
    if len(getuserId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '用户的id为空'
        return callBackDict
    if len(getstreetId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '街道id为空'
        return callBackDict
    if len(getvillageId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '小区id为空'
        return callBackDict
    if signAdmin.verificationAppToken(token) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        createTime = int(time.time() * 1000)
        obj = userAssessment.objects.create(streetId=getstreetId, villageId=getvillageId, type=0, createTime=createTime)
        # 查询出小区的类型
        villageobj = village.objects.get(id=getvillageId)
        obj.save()
        # 创建当前的考核的问题
        assessmentTypeList = assessmentType.objects.filter(subordinateType=villageobj.type)
        for oneassessmentType in assessmentTypeList:
            levelJsonString = oneassessmentType.levelJsonString
            oenAssessmentObj = assessment.objects.create(assessmentTypeId=oneassessmentType.id,assessmentId = obj.id,levelJsonString=levelJsonString)
            oenAssessmentObj.save()
        callBackDict['data'] = obj.id
        callBackDict['code'] = '1'
        callBackDict['msg'] = '创建考核成功'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '创建考核失败'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 提交问题
def upAssessment(request):
    token = request.GET['token'];
    callBackDict = {}
    getassessment = request.GET['assessment'];
    getassessmentType = request.GET['assessmentType'];
    gettotalFraction = request.GET['totalFraction'];
    isLast = request.GET['isLast'];
    try:
        getinfo = request.GET['info'];
    except BaseException as e:
        getinfo = "";
    try:
        getimgs = request.GET['imgs'];
    except BaseException as e:
        getimgs = "";
    levelJsonString = request.GET['levelJsonString'];
    if len(getassessment) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '考核id为空'
        return callBackDict
    if len(getassessmentType) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '考核的问题id为空'
        return callBackDict
    if len(gettotalFraction) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '当前考核的总分为空'
        return callBackDict
    if len(levelJsonString) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '当前考核的问题的具体分数为空'
        return callBackDict
    if len(isLast) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '标记是否已结束为空'
        return callBackDict
    # 验证token
    if signAdmin.verificationAppToken(token) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        createTime = int(time.time() * 1000)
        assessmentOne = assessment.objects.get(assessmentTypeId=getassessmentType,assessmentId = getassessment)
        if assessmentOne :
            assessmentOne.info = getinfo
            assessmentOne.imgs = getimgs
            assessmentOne.levelJsonString = getassessmentType;
            assessmentOne.createTime = createTime
            assessmentOne.save()
            # 保存和更新上面的内容
            if isLast == 1:
                userAssessmentObj = userAssessment.objects.get(id=getassessment)
                if userAssessmentObj:
                    userAssessmentObj.type = 1;
                    userAssessmentObj.save()
                    callBackDict['msg'] = '此次考核已完成'
                else:
                    callBackDict['code'] = '0'
                    callBackDict['msg'] = '当前考核提交的最后一条问题异常'
                    return callBackDict
            else:
                callBackDict['code'] = '1'
                callBackDict['msg'] = '考核问题提交成功'
        else:
            callBackDict['code'] = '0'
            callBackDict['msg'] = '尚未查询到考核的内容'
            return callBackDict
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '提交考核问题失败'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 删除此次的考核
def deleteAssessment(request):
    token = request.GET['token'];
    callBackDict = {}
    getassessment = request.GET['assessment'];
    getUserId = request.GET['userId'];
    if len(getUserId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '当前的用户id为空'
        return callBackDict
    if len(getassessment) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '考核id为空'
        return callBackDict
    # 验证token
    if signAdmin.verificationAppToken(token) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        userAssessmentObj = userAssessment.objects.get(id=getassessment,userId = getUserId)
        if userAssessmentObj:
            userAssessmentObj.type = 2;
            userAssessmentObj.save()
            callBackDict['msg'] = '删除成功'
            callBackDict['code'] = '1'
        else:
            callBackDict['msg'] = '删除失败'
            callBackDict['code'] = '0'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 判断是否拥有正在考核的数据(部分数据)
def getIsHaveAssessment(request):
    token = request.GET['token'];
    callBackDict = {}
    getUserId = request.GET['userId'];
    if len(getUserId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '当前的用户id为空'
        return callBackDict
    # 验证token
    if signAdmin.verificationAppToken(token) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        userAssessmentlist = userAssessment.objects.filter(userId = getUserId, type = 0)
        if len(userAssessmentlist) == 0:
            callBackDict['msg'] = '暂无正在进行中的考核'
            callBackDict['code'] = '0'
        else:
            callBackDict['msg'] = '有无正在进行中的考核'
            callBackDict['code'] = '1'
            # 查询出来一些数据--默认取出第一条的数据
            userAssessmentObj = userAssessmentlist[0]
            # 得到第一条的考核的id
            assessmentObjList = assessment.objects.filter(id=userAssessmentObj.assessmentId)
            list = []
            for oneassessment in assessmentObjList:
                isAnswer = 0
                levelList = None
                imgsList = None
                # 说明了用户已答完题目了
                if oneassessment.createTime == 0:
                    isAnswer = 1
                    levelList = json.loads(oneassessment.levelJsonString)
                if len(oneassessment.imgs) > 0:
                    imgsList = json.loads(oneassessment.imgs)
                list.append({'id': oneassessment.id, 'isAnswer':isAnswer,'totalFraction':oneassessment.totalFraction,'createTime':str(oneassessment.createTime)})
                callBackDict['data'] = list
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 获取考核的问题
def getAssessmentQuestion(request):
    token = request.GET['token'];
    callBackDict = {}
    assessmentQuestionId = request.GET['id'];
    if len(assessmentQuestionId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '考核的问题id为空'
        return callBackDict
    # 验证token
    if signAdmin.verificationAppToken(token) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        assessmentObj = assessment.objects.get(id=assessmentQuestionId)
        isAnswer = 0
        levelList = None
        imgsList = None
        # 说明了用户已答完题目了
        if assessmentObj.createTime == 0:
            isAnswer = 1
            levelList = json.loads(assessmentObj.levelJsonString)
        if len(assessmentObj.imgs) > 0:
            imgsList = json.loads(assessmentObj.imgs)
        callBackDict['data'] = {'id': assessmentObj.id, 'isAnswer': isAnswer, 'totalFraction': assessmentObj.totalFraction,
                         'createTime': str(assessmentObj.createTime),'levelList':levelList,'imgsList':imgsList,'info':assessmentObj.info}
        callBackDict['code'] = '1'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict