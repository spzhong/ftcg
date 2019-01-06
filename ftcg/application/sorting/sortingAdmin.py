# -*- coding: utf-8 -*-
import logging
import django.utils.log
import logging.handlers
import json
import time
import sys
sys.path.append('...')

from ftcg.models import sorting
from ftcg.models import village
from ftcg.models import user
from ftcg.models import street
from ftcg.models import community
from ftcg.models import qrCode
from ftcg.models import roomNumber


from ..user import signAdmin


def upSorting(request):
    token = request.GET['token']
    getstreetId = request.GET['streetId']
    getcommunityId = request.GET['communityId']
    getvillageId = request.GET['villageId']
    getuserId = request.GET['userId']
    getremarks = request.GET['remarks']
    getimgs = request.GET['imgs']
    callBackDict = {}
    try:
        getqrCodeId = request.GET['qrCodeId']
    except BaseException as e:
        getqrCodeId = None
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
    if len(getremarks) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '分拣的描述不能为空'
        return callBackDict
    if len(getimgs) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '分拣的图片不能为空'
        return callBackDict
    if signAdmin.verificationAppToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    try:
        createTime = int(time.time() * 1000)
        sortingObj = sorting.objects.create(userId=getuserId, streetId=getstreetId,communityId = getcommunityId,villageId=getvillageId, state=1, createTime=createTime)
        sortingObj.imgs = getimgs
        sortingObj.remarks = getremarks
        if getqrCodeId:
            sorting.qrCodeId = getqrCodeId
        sortingObj.save()
        callBackDict['code'] = '1'
        callBackDict['data'] = sortingObj.id
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '分拣数据异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 组装考核的数据信息
def makeSortingInfoData(sortingList):
    list = []
    streetIdDict = {}
    communityIdDict = {}
    villageIdDict = {}
    userIdDict = {}
    for oneSorting in sortingList:
        if streetIdDict[oneSorting.streetId]== None:
            streetObj = street.objects.get(id=oneSorting.streetId)
            streetIdDict[oneSorting.streetId] = {"id":streetObj.id,"name":streetObj.name}
        if communityIdDict[oneSorting.communityId]== None:
            communityObj = community.objects.get(id=oneSorting.communityId)
            communityIdDict[oneSorting.communityId] = {"id":communityObj.id,"name":communityObj.name}
        if villageIdDict[oneSorting.villageId] == None:
            villageObj = village.objects.get(id=oneSorting.villageId)
            villageIdDict[oneSorting.villageId] = {"id": villageObj.id, "name": villageObj.name}
        if userIdDict[oneSorting.userId] == None:
            userObj = user.objects.get(id=oneSorting.userId)
            villageIdDict[oneSorting.userId] = {"id": userObj.id, "name": userObj.name}
        # householdInfo 查询住户的信息，判断是否有二维码信息，以及判断二维码是否已经关联了用户的信息
        householdInfo = {}
        if oneSorting.qrCodeId:
            qrCodeList = qrCode.objects.filter(qrCodeId=oneSorting.qrCodeId)
            if len(qrCodeList) > 0:
                oneQrCode = qrCodeList[0]
                roomNumberObj = roomNumber.objects.get(id=oneQrCode.roomNumberId)
                householdInfo['id'] = roomNumberObj.id
                householdInfo['numberText'] = roomNumberObj.numberText
                householdInfo['personCharge'] = roomNumberObj.personCharge
        list.append({"householdInfo":householdInfo,"userInfo":villageIdDict[userIdDict.userId],"villageInfo":villageIdDict[oneSorting.villageId],"communityInfo":communityIdDict[oneSorting.communityId],"streetInfo":streetIdDict[oneSorting.streetId],"id":oneSorting.id,"remarks":oneSorting.remarks,"qrCodeId":oneSorting.qrCodeId,"createTime":oneSorting.createTime,"imgs":json.loads(oneSorting.imgs)})
    return list




# 获取所有的分拣数据
def getAllSortingInfo(request):
    callBackDict = {}
    getpage = int(request.GET['page'])
    getpageSize = int(request.GET['pageSize'])
    token = request.GET['token'];
    if signAdmin.verificationToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    try:
        sortingList = sorting.objects.all().order_by("-createTime")[getpage*getpageSize:getpageSize]
        callBackDict['code'] = '1'
        callBackDict['allPage'] = sorting.objects.all().count()
        callBackDict['data'] = makeSortingInfoData(sortingList)
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '分拣数据异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict




# 获取小区的分拣数据
def getSortingVillage(request):
    callBackDict = {}
    getpage = int(request.GET['page'])
    getpageSize = int(request.GET['pageSize'])
    getvillageId = request.GET['villageId']
    token = request.GET['token'];
    if signAdmin.verificationToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    try:
        sortingList = sorting.objects.filter(villageId=getvillageId).order_by("-createTime")[getpage * getpageSize:getpageSize]
        callBackDict['code'] = '1'
        callBackDict['allPage'] = sorting.objects.filter(villageId=getvillageId).count()
        callBackDict['data'] = makeSortingInfoData(sortingList)
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '分拣数据异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 获取社区的分拣数据
def getSortingcommunity(request):
    callBackDict = {}
    getpage = int(request.GET['page'])
    getpageSize = int(request.GET['pageSize'])
    getcommunityId = request.GET['communityId']
    token = request.GET['token'];
    if signAdmin.verificationToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    try:
        sortingList = sorting.objects.filter(communityId=getcommunityId).order_by("-createTime")[
                      getpage * getpageSize:getpageSize]
        callBackDict['code'] = '1'
        callBackDict['allPage'] = sorting.objects.filter(communityId=getcommunityId).count()
        callBackDict['data'] = makeSortingInfoData(sortingList)
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '分拣数据异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 获取街道的分拣数据
def getSortingStreet(request):
    callBackDict = {}
    getpage = int(request.GET['page'])
    getpageSize = int(request.GET['pageSize'])
    getstreetId = request.GET['streetId']
    token = request.GET['token'];
    if signAdmin.verificationToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    try:
        sortingList = sorting.objects.filter(streetId=getstreetId).order_by("-createTime")[
                      getpage * getpageSize:getpageSize]
        callBackDict['code'] = '1'
        callBackDict['allPage'] = sorting.objects.filter(streetId=getstreetId).count()
        callBackDict['data'] = makeSortingInfoData(sortingList)
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '分拣数据异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict