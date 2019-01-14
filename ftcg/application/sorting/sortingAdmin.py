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

from ..user import signAdmin


# 检查一下生成的二维码的袋子的结构
def isCheckErCode(code):
    try:
        if len(code) != 36:
            return False
        mystr = code[0:27]
        index = 0
        checkCode = ''
        for x in mystr:
            if index % 3 == 0:
                checkCode = checkCode + str(x)
            index = index + 1
        if checkCode == code[27:]:
            return True
    except BaseException as e:
        return False
    return False



def upSorting(request):
    token = request.GET['token']
    getstreetId = request.GET['streetId']
    getcommunityId = request.GET['communityId']
    getvillageId = request.GET['villageId']
    getuserId = request.GET['userId']
    try:
        getremarks = request.GET['remarks']
    except BaseException as e:
        getremarks = ''
    try:
        getimgs = request.GET['imgs']
    except BaseException as e:
        getimgs = "[]"
    callBackDict = {}
    getqrCodeId = None
    try:
        getqrCodeId = request.GET['qrCodeId']
        copyqrCodeId = request.GET['qrCodeId']
        if len(getqrCodeId) > 0:
            if isCheckErCode(copyqrCodeId) == False:
                callBackDict['code'] = '0'
                callBackDict['msg'] = '袋子二维码数据校验失败'
                return callBackDict
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
        sortingObj = sorting.objects.create(userId=getuserId, streetId=getstreetId,communityId = getcommunityId,villageId=getvillageId, createTime=createTime)
        sortingObj.imgs = getimgs
        sortingObj.remarks = getremarks
        if getqrCodeId:
            # 校验state的数据是否正确的
            qrCodeList = qrCode.objects.filter(qrCodeId=getqrCodeId)
            if len(qrCodeList) > 0:
                logger = logging.getLogger("django")
                logger.info('二维码的ID:'+str(getqrCodeId))
                sortingObj.qrCodeId = getqrCodeId
                sortingObj.state = 1  # 提交给审核的数据
            else:
                sortingObj.state = -1  # 异常考核的数据-没有找到相关的对应的二维码房号
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
            try:
                if streetIdDict.has_key(str(oneSorting.streetId)) == False:
                    streetObj = street.objects.get(id=oneSorting.streetId)
                    streetIdDict[str(oneSorting.streetId)] = {"id": streetObj.id, "name": streetObj.name}
            except BaseException as e:
                streetIdDict[str(oneSorting.streetId)] = {}
                logger = logging.getLogger("django")
                logger.info("街道ID异常了" + str(e))
            try:
                if communityIdDict.has_key(str(oneSorting.communityId)) == False:
                    communityObj = community.objects.get(id=oneSorting.communityId)
                    communityIdDict[str(oneSorting.communityId)] = {"id": communityObj.id, "name": communityObj.name}
            except BaseException as e:
                communityIdDict[str(oneSorting.communityId)] = {}
                logger = logging.getLogger("django")
                logger.info("社区ID异常了" + str(e))
            try:
                if villageIdDict.has_key(str(oneSorting.villageId)) == False:
                    villageObj = village.objects.get(id=oneSorting.villageId)
                    villageIdDict[str(oneSorting.villageId)] = {"id": villageObj.id, "name": villageObj.name}
            except BaseException as e:
                villageIdDict[str(oneSorting.villageId)] = {}
                logger = logging.getLogger("django")
                logger.info("小区ID异常了" + str(e))
            try:
                if userIdDict.has_key(str(oneSorting.userId)) == False:
                    userObj = user.objects.get(id=oneSorting.userId)
                    userIdDict[str(oneSorting.userId)] = {"id": userObj.id, "name": userObj.name}
            except BaseException as e:
                logger = logging.getLogger("django")
                logger.info("用户ID异常了" + str(e) + "    userid:" +str(oneSorting.userId))
                userIdDict[str(oneSorting.userId)] = {}
            # householdInfo 查询住户的信息，判断是否有二维码信息，以及判断二维码是否已经关联了用户的信息
            oneQrCode = None
            if oneSorting.qrCodeId :
                qrCodeList = qrCode.objects.filter(qrCodeId=oneSorting.qrCodeId)
                if len(qrCodeList) > 0:
                   oneQrCode = qrCodeList[0]

            try :
                imgsJosn = json.loads(oneSorting.imgs)
            except BaseException as e:
                imgsJosn = []
            if oneQrCode != None:
                list.append({"householdInfo":oneQrCode.roomNumberText,"userInfo":userIdDict[str(oneSorting.userId)],"villageInfo":villageIdDict[str(oneSorting.villageId)],"communityInfo":communityIdDict[str(oneSorting.communityId)],"streetInfo":streetIdDict[str(oneSorting.streetId)],"id":oneSorting.id,"remarks":oneSorting.remarks,"state":oneSorting.state,"qrCodeId":oneSorting.qrCodeId,"createTime":oneSorting.createTime,"imgs":imgsJosn})
            else:
                list.append({"householdInfo": "", "userInfo": userIdDict[str(oneSorting.userId)],
                             "villageInfo": villageIdDict[str(oneSorting.villageId)],
                             "communityInfo": communityIdDict[str(oneSorting.communityId)],
                             "streetInfo": streetIdDict[str(oneSorting.streetId)], "id": oneSorting.id,
                             "remarks": oneSorting.remarks, "state": oneSorting.state, "qrCodeId": oneSorting.qrCodeId,
                             "createTime": oneSorting.createTime, "imgs": imgsJosn})
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
    try:
        getpage = int(request.GET['page'])
    except BaseException as e:
        callBackDict['msg'] = '页码为空，默认从0开始'
        callBackDict['code'] = '0'
        return callBackDict
    try:
        getpageSize = int(request.GET['pageSize'])
    except BaseException as e:
        callBackDict['msg'] = 'pageSize为空，默认20页'
        callBackDict['code'] = '0'
        return callBackDict
    getvillageId = request.GET['villageId']
    token = request.GET['token'];
    if signAdmin.verificationToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    try:
        sortingList = sorting.objects.filter(villageId=getvillageId,state__gte=-1).order_by("-createTime")[getpage * getpageSize:getpageSize]
        callBackDict['code'] = '1'
        callBackDict['allPage'] = sorting.objects.filter(villageId=getvillageId,state__gte=-1).count()
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
    try:
        getpage = int(request.GET['page'])
    except BaseException as e:
        callBackDict['msg'] = '页码为空，默认从0开始'
        callBackDict['code'] = '0'
        return callBackDict
    try:
        getpageSize = int(request.GET['pageSize'])
    except BaseException as e:
        callBackDict['msg'] = 'pageSize为空，默认20页'
        callBackDict['code'] = '0'
        return callBackDict
    getcommunityId = request.GET['communityId']
    token = request.GET['token'];
    if signAdmin.verificationToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    try:
        sortingList = sorting.objects.filter(communityId=getcommunityId,state__gte=-1).order_by("-createTime")[
                      getpage * getpageSize:getpageSize]
        callBackDict['code'] = '1'
        callBackDict['allPage'] = sorting.objects.filter(communityId=getcommunityId,state__gte=-1).count()
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
    try:
        getpage = int(request.GET['page'])
    except BaseException as e:
        callBackDict['msg'] = '页码为空，默认从0开始'
        callBackDict['code'] = '0'
        return callBackDict
    try:
        getpageSize = int(request.GET['pageSize'])
    except BaseException as e:
        callBackDict['msg'] = 'pageSize为空，默认20页'
        callBackDict['code'] = '0'
        return callBackDict
    getstreetId = request.GET['streetId']
    token = request.GET['token'];
    if signAdmin.verificationToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    try:
        sortingList = sorting.objects.filter(streetId=getstreetId,state__gte=-1).order_by("-createTime")[
                      getpage * getpageSize:getpageSize]
        callBackDict['code'] = '1'
        callBackDict['allPage'] = sorting.objects.filter(streetId=getstreetId,state__gte=-1).count()
        callBackDict['data'] = makeSortingInfoData(sortingList)
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '分拣数据异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict




# 获取街道的分拣数据
def deleteSortingInfo(request):
    callBackDict = {}
    getSortingId = request.GET['sortingId']
    token = request.GET['token'];
    if signAdmin.verificationToken(token) == False:
        callBackDict['code'] = '9999'
        callBackDict['msg'] = 'token异常，请重新登录'
        return callBackDict
    try:
        sortingObj = sorting.objects.get(id=getSortingId)
        sortingObj.state = -2;
        sortingObj.save()
        callBackDict['code'] = '1'
        callBackDict['msg'] = "删除成功"
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '数据异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict