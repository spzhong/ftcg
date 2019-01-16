# -*- coding: utf-8 -*-
import logging
import django.utils.log
import logging.handlers
import json
from django.db.models import Avg
import sys
sys.path.append('...')

from ftcg.models import userAssessment
from ftcg.models import sorting
from ftcg.models import street

import time
from datetime import datetime


# 获取综述的统计
def getAllStatistics(request):
    callBackDict = {}
    list1 = []
    list2 = []
    cout1 = 0
    cout2 = 0
    listTime = getTimeStatistics()
    endTime = int(time.time() * 1000)
    for dict in listTime:
        countUserAssessment = userAssessment.objects.filter(state__gte=0, createTime__gte=dict["timeStamp"] ,createTime__lt=endTime).count()
        countSorting = sorting.objects.filter(state__gte=-1, createTime__gte=int(dict["timeStamp"]),createTime__lt=endTime).count()
        endTime = dict["timeStamp"]
        list1.append({"date":dict["date"],"num":countUserAssessment})
        list2.append({"date": dict["date"],"num":countSorting})
        cout1 = cout1 + countUserAssessment
        cout2 = cout2 + countSorting
    callBackDict["data"] = {"assessment":{"totalNumber":cout1,"list":list1},"sorting":{"totalNumber":cout2,"list":list2}}
    return callBackDict



# 时间的长度
def getTimeStatistics():
    myear = datetime.now().year
    mmouth = datetime.now().month
    list = []
    for num in range(0, 12):
        if mmouth == 0:
            myear = myear - 1
            mmouth = 12
        strmmouth = str(mmouth)
        if mmouth < 10:
            strmmouth = "0" + strmmouth
        dict = {"timeStamp": "", "date": str(myear) + "-" + strmmouth}
        dict["timeStamp"] = int(time.mktime(time.strptime(dict['date']+"-01", "%Y-%m-%d")))*1000
        list.append(dict)
        mmouth = mmouth - 1;
    return list.reverse()




#获取考核的统计
def getAssessmentStatistics(request):
    type_parm = request.GET['type'];
    businessId_parm = request.GET['businessId'];
    callBackDict = {}
    if len(businessId_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '业务id为空'
        return callBackDict
    list1 = []
    cout1 = 0
    listTime = getTimeStatistics()
    endTime = int(time.time() * 1000)
    if type_parm == "0":
        #街道
        for dict in listTime:
            countUserAssessment = userAssessment.objects.filter(state__gte=0, streetId = businessId_parm, createTime__gte= dict["timeStamp"],
                                                                createTime__lt=endTime).count()
            totalFraction__avg = 0
            if countUserAssessment > 0:
                avgtotalFraction = userAssessment.objects.filter(state__gte=0, streetId = businessId_parm, createTime__gte= dict["timeStamp"],
                                                                createTime__lt=endTime).aggregate(Avg("totalFraction"))
                totalFraction__avg = avgtotalFraction['totalFraction__avg']
            endTime = dict["timeStamp"]
            list1.append({"date": dict["date"], "num": countUserAssessment,"average":totalFraction__avg})
            cout1 = cout1 + countUserAssessment
        callBackDict["data"] = {"totalNumber": cout1, "list": list1}
    elif type_parm == "1":
        # 社区
        for dict in listTime:
            countUserAssessment = userAssessment.objects.filter(state__gte=0, communityId=businessId_parm,
                                                                createTime__gte=dict["timeStamp"],
                                                                createTime__lt=endTime).count()
            totalFraction__avg = 0
            if countUserAssessment > 0:
                avgtotalFraction = userAssessment.objects.filter(state__gte=0, communityId=businessId_parm,
                                                                createTime__gte=dict["timeStamp"],
                                                                createTime__lt=endTime).aggregate(Avg("totalFraction"))
                totalFraction__avg = avgtotalFraction['totalFraction__avg']
            endTime = dict["timeStamp"]
            list1.append({"date": dict["date"], "num": countUserAssessment,"average":totalFraction__avg})
            cout1 = cout1 + countUserAssessment
        callBackDict["data"] = {"totalNumber": cout1, "list": list1}
    elif type_parm == "2":
        # 小区
        for dict in listTime:
            countUserAssessment = userAssessment.objects.filter(state__gte=0, villageId=businessId_parm,
                                                                createTime__gte=int(dict["timeStamp"]),
                                                                createTime__lt=endTime).count()
            totalFraction__avg = 0
            if countUserAssessment > 0:
                avgtotalFraction = userAssessment.objects.filter(state__gte=0, villageId=businessId_parm,
                                                                createTime__gte=int(dict["timeStamp"]),
                                                                createTime__lt=endTime).aggregate(Avg("totalFraction"))
                totalFraction__avg = avgtotalFraction['totalFraction__avg']
            endTime = int(dict["timeStamp"])
            list1.append({"date": dict["date"], "num": countUserAssessment,"average":totalFraction__avg})
            cout1 = cout1 + countUserAssessment
        callBackDict["data"] = {"totalNumber": cout1, "list": list1}
    else:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '业务类型不存在'
        return callBackDict
    return callBackDict




# 获取分拣的统计
def getSortingStatistics(request):
    type_parm = request.GET['type'];
    businessId_parm = request.GET['businessId'];
    callBackDict = {}
    if len(businessId_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '业务id为空'
        return callBackDict
    list2 = []
    cout2 = 0
    listTime = getTimeStatistics()
    endTime = int(time.time() * 1000)
    if type_parm == "0":
        # 街道
        for dict in listTime:
            countSorting = sorting.objects.filter(state__gte=-1, streetId = businessId_parm, createTime__gte=dict["timeStamp"],createTime__lt=endTime).count()
            endTime = dict["timeStamp"]
            list2.append({"date": dict["date"], "num": countSorting})
            cout2 = cout2 + countSorting
        callBackDict["data"] = {"totalNumber": cout2, "list": list2}
    elif type_parm == "1":
        # 社区
        for dict in listTime:
            countSorting = sorting.objects.filter(state__gte=-1, communityId = businessId_parm, createTime__gte=dict["timeStamp"],createTime__lt=endTime).count()
            endTime = dict["timeStamp"]
            list2.append({"date": dict["date"], "num": countSorting})
            cout2 = cout2 + countSorting
        callBackDict["data"] = {"totalNumber": cout2, "list": list2}
    elif type_parm == "2":
        # 小区
        for dict in listTime:
            countSorting = sorting.objects.filter(state__gte=-1, villageId = businessId_parm, createTime__gte=int(dict["timeStamp"]),createTime__lt=endTime).count()
            endTime = dict["timeStamp"]
            list2.append({"date": dict["date"], "num": countSorting})
            cout2 = cout2 + countSorting
        callBackDict["data"] = {"totalNumber": cout2, "list": list2}
    else:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '业务类型不存在'
        return callBackDict
    return callBackDict



# 考核的
def getAllStreetsAssessmentStatistics(request):
    # 获取所有街道的数据
    streetList = street.objects.all()
    streetsList = []
    callBackDict = {}
    for oneStreet in streetList:
        listTime = getTimeStatistics()
        endTime = int(time.time() * 1000)
        # 街道
        list = []
        cout1 = 0
        for dict in listTime:
            countUserAssessment = userAssessment.objects.filter(state__gte=0, streetId=oneStreet.id,createTime__gte=dict["timeStamp"],createTime__lt=endTime).count()
            totalFraction__avg = 0
            if countUserAssessment > 0:
                avgtotalFraction = userAssessment.objects.filter(state__gte=0, streetId=oneStreet.id,
                                                                     createTime__gte=dict["timeStamp"],
                                                                     createTime__lt=endTime).aggregate(Avg("totalFraction"))
                totalFraction__avg = avgtotalFraction['totalFraction__avg']
                endTime = dict["timeStamp"]
            list.append({"date": dict["date"], "num": countUserAssessment, "average": totalFraction__avg})
            cout1 = cout1 + countUserAssessment
        streetsList.append({"streetId": oneStreet.id, "totalNumber": cout1, "list": list})
    callBackDict['code'] = '1'
    callBackDict['data'] = streetsList
    return callBackDict



# 分拣的
def getAllStreetsSortingStatistics(request):
    # 获取所有街道的数据
    streetList = street.objects.all()
    streetsList = []
    callBackDict = {}
    for oneStreet in streetList:
        listTime = getTimeStatistics()
        endTime = int(time.time() * 1000)
        cout2 = 0
        list = []
        for dict in listTime:
            countSorting = sorting.objects.filter(state__gte=-1, streetId = oneStreet.id, createTime__gte=dict["timeStamp"],createTime__lt=endTime).count()
            endTime = dict["timeStamp"]
            list.append({"date": dict["date"], "num": countSorting})
            cout2 = cout2 + countSorting
        streetsList.append({"streetId":oneStreet.id,"totalNumber": cout2, "list": list})
    callBackDict['code'] = '1'
    callBackDict['data'] = streetsList
    return callBackDict
