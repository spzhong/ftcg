# -*- coding: utf-8 -*-
import json
import assessmentAdmin

from django.http import HttpResponse

def index(request,route):
    if route == 'upAssessment':
        callBackDict = assessmentAdmin.upAssessment(request)
    elif route == 'assessmentVillage':
        callBackDict = assessmentAdmin.assessmentVillage(request)
    elif route == 'assessmentInfo':
        callBackDict = assessmentAdmin.assessmentInfo(request)
    else:
         return HttpResponse("no found !!!")
    return HttpResponse(json.dumps(callBackDict))