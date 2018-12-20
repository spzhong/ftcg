# -*- coding: utf-8 -*-
import json
import assessmentAdmin

from django.http import HttpResponse

def index(request,route):
    if route == 'createAssessment':
        callBackDict = assessmentAdmin.createAssessment(request)
    elif route == 'upAssessment':
        callBackDict = assessmentAdmin.upAssessment(request)
    elif route == 'deleteAssessment':
        callBackDict = assessmentAdmin.deleteAssessment(request)
    elif route == 'getIsHaveAssessment':
        callBackDict = assessmentAdmin.getIsHaveAssessment(request)
    elif route == 'getAssessmentQuestion':
        callBackDict = assessmentAdmin.getAssessmentQuestion(request)
    else:
         return HttpResponse("no found !!!")
    return HttpResponse(json.dumps(callBackDict))