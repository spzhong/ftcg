# -*- coding: utf-8 -*-
import logging
import django.utils.log
import logging.handlers
import json

import sys
sys.path.append('...')

from ftcg.models import userAssessment
from ftcg.models import sorting
import time
from datetime import datetime


# 获取综述的统计
def getAllStatistics(request):
    callBackDict = {}
    list1 = []
    list2 = []
    cout1 = 0
    cout2 = 0
    listTime = getAllStatistics()
    endTime = int(time.time() * 1000)
    for dict in listTime:
        countUserAssessment = userAssessment.objects.filter(state__gte=0, createTime__gte=int(dict["timeStamp"]) ,createTime__lt=endTime).count()
        countSorting = sorting.objects.filter(state__gte=0, createTime__gte=int(dict["timeStamp"]),createTime__lt=endTime).count()
        endTime = int(dict["timeStamp"])
        list1.append({"date":dict["date"],"num":countUserAssessment})
        list2.append({"date": dict["date"],"num":countSorting})
        cout1 = cout1 + countUserAssessment
        cout2 = cout2 + countSorting
    callBackDict["data"] = {"assessment":{"totalNumber":cout1,"list":list1},"sorting":{"totalNumber":cout2,"list":list2}}
    return callBackDict



# 时间的长度
def getAllStatistics():
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
        dict["timeStamp"] = str(time.mktime(time.strptime(dict['date']+"-01", "%Y-%m-%d"))*1000)
        list.append(dict)
        mmouth = mmouth - 1;
    return list




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
    listTime = getAllStatistics()
    endTime = int(time.time() * 1000)
    if type_parm == "0":
        #街道
        for dict in listTime:
            countUserAssessment = userAssessment.objects.filter(state__gte=0, streetId = businessId_parm, createTime__gte=int(dict["timeStamp"]),
                                                                createTime__lt=endTime).count()
            endTime = int(dict["timeStamp"])
            list1.append({"date": dict["date"], "num": countUserAssessment})
            cout1 = cout1 + countUserAssessment
        callBackDict["data"] = {"totalNumber": cout1, "list": list1}
    elif type_parm == "1":
        # 社区
        for dict in listTime:
            countUserAssessment = userAssessment.objects.filter(state__gte=0, communityId=businessId_parm,
                                                                createTime__gte=int(dict["timeStamp"]),
                                                                createTime__lt=endTime).count()
            endTime = int(dict["timeStamp"])
            list1.append({"date": dict["date"], "num": countUserAssessment})
            cout1 = cout1 + countUserAssessment
        callBackDict["data"] = {"totalNumber": cout1, "list": list1}
    elif type_parm == "2":
        # 小区
        for dict in listTime:
            countUserAssessment = userAssessment.objects.filter(state__gte=0, villageId=businessId_parm,
                                                                createTime__gte=int(dict["timeStamp"]),
                                                                createTime__lt=endTime).count()
            endTime = int(dict["timeStamp"])
            list1.append({"date": dict["date"], "num": countUserAssessment})
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
    listTime = getAllStatistics()
    endTime = int(time.time() * 1000)
    if type_parm == "0":
        # 街道
        for dict in listTime:
            countSorting = sorting.objects.filter(state__gte=0, streetId = businessId_parm, createTime__gte=int(dict["timeStamp"]),createTime__lt=endTime).count()
            avgtotalFraction = sorting.objects.filter(state__gte=0, streetId=businessId_parm, createTime__gte=int(dict["timeStamp"]),createTime__lt=endTime).Avg("totalFraction")

            endTime = int(dict["timeStamp"])
            list2.append({"date": dict["date"], "num": countSorting,"average":avgtotalFraction})
            cout2 = cout2 + countSorting
        callBackDict["data"] = {"totalNumber": cout2, "list": list2}
    elif type_parm == "1":
        # 社区
        for dict in listTime:
            countSorting = sorting.objects.filter(state__gte=0, communityId = businessId_parm, createTime__gte=int(dict["timeStamp"]),createTime__lt=endTime).count()
            avgtotalFraction = sorting.objects.filter(state__gte=0, communityId=businessId_parm,
                                                      createTime__gte=int(dict["timeStamp"]),
                                                      createTime__lt=endTime).Avg("totalFraction")
            endTime = int(dict["timeStamp"])
            list2.append({"date": dict["date"], "num": countSorting, "average": avgtotalFraction})
            cout2 = cout2 + countSorting
        callBackDict["data"] = {"totalNumber": cout2, "list": list2}
    elif type_parm == "2":
        # 小区
        for dict in listTime:
            countSorting = sorting.objects.filter(state__gte=0, villageId = businessId_parm, createTime__gte=int(dict["timeStamp"]),createTime__lt=endTime).count()
            avgtotalFraction = sorting.objects.filter(state__gte=0, communityId=businessId_parm,
                                                      createTime__gte=int(dict["timeStamp"]),
                                                      createTime__lt=endTime).Avg("totalFraction")
            endTime = int(dict["timeStamp"])
            list2.append({"date": dict["date"], "num": countSorting, "average": avgtotalFraction})
            cout2 = cout2 + countSorting
        callBackDict["data"] = {"totalNumber": cout2, "list": list2}
    else:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '业务类型不存在'
        return callBackDict
    return callBackDict

