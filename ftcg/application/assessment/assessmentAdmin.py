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
from ftcg.models import assessmentQuestion
from ftcg.models import village
from ..user import signAdmin

# 创建考核
def createAssessment(request):
    token = request.GET['token'];
    getstreetId = request.GET['streetId'];
    getcommunityId = request.GET['communityId'];
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
    if len(getcommunityId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '社区id为空'
        return callBackDict
    if signAdmin.verificationAppToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    try:
        createTime = int(time.time() * 1000)
        villageobj = village.objects.get(id=getvillageId)
        obj = userAssessment.objects.create(userId=getuserId, streetId=getstreetId,communityId = getcommunityId,villageId=getvillageId, type=villageobj.type,state=0, createTime=createTime)
        # 查询出小区的类型
        obj.save()
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
def upAssessmentQuestion(request):
    token = request.GET['token'];
    callBackDict = {}
    getuserAssessmentId = request.GET['userAssessmentId'];
    getquestionId = request.GET['questionId'];
    try:
        getinfo = request.GET['info'];
    except BaseException as e:
        getinfo = "";
    try:
        getimgs = request.GET['jsonImgs'];
    except BaseException as e:
        getimgs = "[]";
    getfraction = int(request.GET['fraction'])
    if len(getuserAssessmentId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '考核id为空'
        return callBackDict
    if len(getquestionId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '考核的问题id为空'
        return callBackDict
    if getfraction < 0 or getfraction>100:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '考核的分数异常'
        return callBackDict
    # 验证token
    if signAdmin.verificationAppToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    try:
        assessmentQuestionObj = assessmentQuestion.objects.get(id=getquestionId)
        if getfraction > assessmentQuestionObj.fraction :
            callBackDict['code'] = '0'
            callBackDict['msg'] = '考核的分数大于总分'
            return callBackDict
        assessmentOneList = assessment.objects.filter(userAssessmentId=getuserAssessmentId)
        allfraction = 100
        isHaveCurQuestionId = 0
        logger = logging.getLogger("django")
        logger.info('考核数据的长度------' + str(len(assessmentOneList)))
        for assess in assessmentOneList:
            logger = logging.getLogger("django")
            logger.info('------'+str(assess.assessmentQuestionId))
            if assess.assessmentQuestionId == int(getquestionId):
                logger = logging.getLogger("django")
                logger.info('找到当前的问题了------')
                isHaveCurQuestionId = 1
                # 更新操作
                assess.fraction = getfraction  #扣分项
                assess.info = getinfo
                assess.imgs = getimgs
                assess.save()
                # 判断是否是加分项
                if assessmentQuestionObj.assessmentType == 1:
                    allfraction = allfraction + assess.fraction
                else:
                    allfraction = allfraction - assess.fraction
            else:
                allfraction = allfraction - assess.fraction
        # 创建一条新的数据
        if isHaveCurQuestionId == 0:
            getcreateTime = int(time.time() * 1000)
            assessmentOne = assessment.objects.create(fraction=getfraction,assessmentQuestionId=getquestionId,userAssessmentId=getuserAssessmentId,info=getinfo,imgs=getimgs,createTime=getcreateTime)
            assessmentOne.save()
        logger = logging.getLogger("django")
        logger.info('最终得分------'+str(allfraction))
        # 重新计算一下总分数
        userAssessmentObj = userAssessment.objects.get(id=getuserAssessmentId)
        userAssessmentObj.totalFraction = allfraction
        userAssessmentObj.save()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '考核问题提交成功'
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
    getassessmentId = request.GET['userAssessmentId'];
    if len(getassessmentId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '考核id为空'
        return callBackDict
    # 验证token
    if signAdmin.verificationAppToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    try:
        userAssessmentObj = userAssessment.objects.get(id=getassessmentId)
        if userAssessmentObj:
            userAssessmentObj.state = -1;
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
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    try:
        userAssessmentlist = userAssessment.objects.filter(userId=getUserId, state=0)
        if len(userAssessmentlist) == 0:
            callBackDict['msg'] = '无进行中的考核'
            callBackDict['code'] = '0'
        else:
            callBackDict['msg'] = '有正在进行中的考核'
            callBackDict['code'] = '1'
            list = []
            for oneUserAssess in userAssessmentlist:
                oneVillage = village.objects.get(id= oneUserAssess.villageId)
                list.append({"totalFraction":oneUserAssess.totalFraction,"state":"0","id":oneUserAssess.id,"createTime":oneUserAssess.createTime,"village":{'id': oneVillage.id, 'name': oneVillage.name, 'type': oneVillage.type, 'number': oneVillage.number,
                 'address': oneVillage.address, 'personCharge': oneVillage.personCharge,
                 'phone': oneVillage.phone, 'remarks': oneVillage.remarks,
                 'managementSubsetNum': oneVillage.managementSubsetNum}})
            callBackDict['code'] = '1'
            callBackDict['data'] = list
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict





# 获取考核的所有问题
def getAssessmentQuestion(request):
    token = request.GET['token'];
    callBackDict = {}
    getserAssessmentId = request.GET['userAssessmentId'];
    getUserId = request.GET['userId'];
    if len(getserAssessmentId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '考核的id为空'
        return callBackDict
    if len(getUserId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '用户的ID为空'
        return callBackDict
    # 验证token
    if signAdmin.verificationAppToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    try:
        # 查找此次考核的数据
        userAssessmentObj = userAssessment.objects.get(id=getserAssessmentId,userId=getUserId)
        # 查询对应的小区类型
        oneVillage = village.objects.get(id=userAssessmentObj.villageId)
        # 查询小区对应的问题
        questionList = assessmentQuestion.objects.filter(subordinateType=userAssessmentObj.type)
        list = []
        for onequestion in questionList:
            dict = {"id": onequestion.id, "assessmentType":onequestion.assessmentType,"req": onequestion.req, "oneLevelName": onequestion.oneLevelName,
                    "shortName": onequestion.shortName,"fraction":onequestion.fraction, "info": onequestion.info,
                    "assessmentType": onequestion.assessmentType,
                    "answerJson": json.loads(onequestion.answerJson)}
            try:
                assessmentObj = assessment.objects.get(userAssessmentId=getserAssessmentId,assessmentQuestionId=onequestion.id)
                if assessmentObj:
                    dict["answerInfo"] = {"info": assessmentObj.info, "fraction": assessmentObj.fraction,
                                      "createTime": assessmentObj.createTime, "imgs": json.loads(assessmentObj.imgs)}
                    list.append(dict)
            except BaseException as e:
                list.append(dict)
        callBackDict['code'] = '1'
        callBackDict['data'] = {"totalFraction": userAssessmentObj.totalFraction,"correctTotalFraction":userAssessmentObj.correctTotalFraction,"state": userAssessmentObj.state, "id": userAssessmentObj.id,
                     "createTime": userAssessmentObj.createTime,"questionList":list,
                     "village": {'id': oneVillage.id, 'name': oneVillage.name, 'type': oneVillage.type,
                                 'number': oneVillage.number,
                                 'address': oneVillage.address, 'personCharge': oneVillage.personCharge,
                                 'phone': oneVillage.phone, 'remarks': oneVillage.remarks,
                                 'managementSubsetNum': oneVillage.managementSubsetNum}}
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 完成提交审核
def finshAssessment(request):
    token = request.GET['token'];
    callBackDict = {}
    getUserAssessmentId = request.GET['userAssessmentId'];
    getuserId = request.GET['userId'];
    if len(getUserAssessmentId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '考核的ID为空'
        return callBackDict
    if len(getuserId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '用户的ID为空'
        return callBackDict
    # 验证token
    if signAdmin.verificationAppToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    try:
        assessmentObj = userAssessment.objects.get(id=getUserAssessmentId,userId=getuserId)
        assessmentObj.state = 1
        assessmentObj.save()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '已经提交审核'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict


# 获取考核
def getAssessmentList(request):
    callBackDict = {}
    try:
        token = request.GET['token'];
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token为空'
        return callBackDict
    try:
        getstreetId = request.GET['streetId']
        if len(getstreetId) == 0:
            callBackDict['code'] = '0'
            callBackDict['msg'] = '街道Id为空'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '街道Id为空'
        return callBackDict
    try:
        getpage = int(request.GET['page'])
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '页码数据为空'
        return callBackDict
    try:
        getpageSize = int(request.GET['pageSize'])
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'pageSize为空'
        return callBackDict
    # 验证token
    if signAdmin.verificationToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    if getpageSize == 0 :
        getpageSize = 20;
    # 社区的ID和小区的ID
    getcommunityId = None
    getvillageId = None
    try:
        getcommunityId = request.GET['communityId']
        getvillageId = request.GET['villageId']
    except BaseException as e:
        logger = logging.getLogger("django")
        logger.info(str(e))
    assessmentUserList = None
    try:
        if getcommunityId:
            if getvillageId:
                assessmentUserList = userAssessment.objects.filter(streetId=getstreetId, villageId = getvillageId, communityId = getcommunityId).order_by("-createTime")[getpage*getpageSize:getpageSize]
                allPage = userAssessment.objects.filter(streetId=getstreetId, villageId = getvillageId, communityId = getcommunityId).count()
            else :
                assessmentUserList = userAssessment.objects.filter(streetId=getstreetId, communityId = getcommunityId).order_by("-createTime")[getpage*getpageSize:getpageSize]
                allPage = userAssessment.objects.filter(streetId=getstreetId, communityId = getcommunityId).count()
        else :
            if getvillageId:
                assessmentUserList = userAssessment.objects.filter(streetId=getstreetId, villageId = getvillageId).order_by("-createTime")[getpage*getpageSize:getpageSize]
                allPage = userAssessment.objects.filter(streetId=getstreetId, villageId = getvillageId).count()
            else :
                assessmentUserList = userAssessment.objects.filter(streetId=getstreetId).order_by("-createTime")[getpage*getpageSize:getpageSize]
                allPage = userAssessment.objects.filter(streetId=getstreetId).count()
        if len(assessmentUserList) > 0:
            list = []
            for userAssessmentObj in assessmentUserList:
                # 查询出来审核员
                userObj = user.objects.get(id=userAssessmentObj.userId)
                list.append({"id":userAssessmentObj.id,"state":userAssessmentObj.state,"totalFraction":userAssessmentObj.totalFraction,"createTime":userAssessmentObj.createTime,"correctTotalFraction":userAssessmentObj.correctTotalFraction,"type":userAssessmentObj.type,"userInfo":{"id":userObj.id,"name":userObj.name,"phone":userObj.phone,"role":userObj.role}})
            callBackDict['code'] = '1'
            callBackDict['totalNum'] = allPage
            callBackDict['data'] = list
        else:
            callBackDict['code'] = '0'
            callBackDict['msg'] = '暂无数据'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 查询考核的详情
def getAssessmentDetails(request):
    callBackDict = {}
    try:
        token = request.GET['token'];
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token为空'
        return callBackDict
    try:
        getUserAssessmentId = request.GET['userAssessmentId'];
        if len(getUserAssessmentId) == 0:
            callBackDict['code'] = '0'
            callBackDict['msg'] = '考核的ID为空'
            return callBackDict
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '考核的ID为空'
        return callBackDict
    # 验证token
    if signAdmin.verificationAppToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        # 查找此次考核的数据
        userAssessmentObj = userAssessment.objects.get(id=getUserAssessmentId)
        # 查询出来审核员
        userObj = user.objects.get(id=userAssessmentObj.userId)
        # 查询对应的小区类型
        oneVillage = village.objects.get(id=userAssessmentObj.villageId)
        # 查询小区对应的问题
        questionList = assessmentQuestion.objects.filter(subordinateType=userAssessmentObj.type)
        list = []
        for onequestion in questionList:
            dict = {"id": onequestion.id,"assessmentType":onequestion.assessmentType,"req": onequestion.req, "oneLevelName": onequestion.oneLevelName,
                    "shortName": onequestion.shortName, "info": onequestion.info,"fraction":onequestion.fraction,
                    "assessmentType": onequestion.assessmentType,
                    "answerJson": json.loads(onequestion.answerJson)}
            try:
                assessmentObj = assessment.objects.get(userAssessmentId=getUserAssessmentId,assessmentQuestionId=onequestion.id)
                if assessmentObj:
                    dict["answerInfo"] = {"info": assessmentObj.info, "fraction": assessmentObj.fraction,
                                      "createTime": assessmentObj.createTime, "imgs": json.loads(assessmentObj.imgs)}
                    list.append(dict)
            except BaseException as e:
                list.append(dict)
        callBackDict['code'] = '1'
        callBackDict['data'] = {"totalFraction": userAssessmentObj.totalFraction,"correctTotalFraction":userAssessmentObj.correctTotalFraction,"state": userAssessmentObj.state, "id": userAssessmentObj.id,
                     "createTime": userAssessmentObj.createTime,"questionList":list,
                                "userInfo":{"id":userObj.id,"name":userObj.name,"phone":userObj.phone,"role":userObj.role},
                     "village": {'id': oneVillage.id, 'name': oneVillage.name, 'type': oneVillage.type,
                                 'number': oneVillage.number,
                                 'address': oneVillage.address, 'personCharge': oneVillage.personCharge,
                                 'phone': oneVillage.phone, 'remarks': oneVillage.remarks,
                                 'managementSubsetNum': oneVillage.managementSubsetNum}}
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 最终修改后的分数
def correctTotalFraction(request):
    token = request.GET['token'];
    callBackDict = {}
    getUserAssessmentId = request.GET['userAssessmentId'];
    try:
        getcorrectTotalFraction = int(request.GET['correctTotalFraction'])
    except BaseException as e:
        getcorrectTotalFraction = -1
    if len(getUserAssessmentId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '考核的ID为空'
        return callBackDict
    if getcorrectTotalFraction < 0 or getcorrectTotalFraction > 100:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '考核的分数异常'
        return callBackDict
    # 验证token
    if signAdmin.verificationToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        assessmentObj = userAssessment.objects.get(id=getUserAssessmentId)
        if getcorrectTotalFraction >= 0 :
            assessmentObj.correctTotalFraction = getcorrectTotalFraction
        assessmentObj.state = 3 #审核通过
        assessmentObj.save()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '修改最终的考核分数成功'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict