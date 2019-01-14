# -*- coding: utf-8 -*-
import json
import statisticsAdmin

from django.http import HttpResponse

def index(request,route):
    if route == 'getAllStatistics':
        callBackDict = statisticsAdmin.getAllStatistics(request)
    elif route == 'getAssessmentStatistics':
        callBackDict = statisticsAdmin.getAssessmentStatistics(request)
    elif route == 'getSortingStatistics':
        callBackDict = statisticsAdmin.getSortingStatistics(request)
    else:
         return HttpResponse("no found !!!")
    return HttpResponse(json.dumps(callBackDict))
