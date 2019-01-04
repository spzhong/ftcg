# -*- coding: utf-8 -*-
import json
import assessmentAdmin

from django.http import HttpResponse

def index(request,route):
    if route == 'createAssessment':
        callBackDict = assessmentAdmin.createAssessment(request)
    elif route == 'upAssessmentQuestion':
        callBackDict = assessmentAdmin.upAssessmentQuestion(request)
    elif route == 'deleteAssessment':
        callBackDict = assessmentAdmin.deleteAssessment(request)
    elif route == 'getIsHaveAssessment':
        callBackDict = assessmentAdmin.getIsHaveAssessment(request)
    elif route == 'getAssessmentQuestion':
        callBackDict = assessmentAdmin.getAssessmentQuestion(request)
    elif route == 'finshAssessment':
        callBackDict = assessmentAdmin.finshAssessment(request)
    elif route == 'getAssessmentList':
        callBackDict = assessmentAdmin.getAssessmentList(request)
    elif route == 'getAssessmentDetails':
        callBackDict = assessmentAdmin.getAssessmentDetails(request)
    elif route == 'correctTotalFraction':
        callBackDict = assessmentAdmin.correctTotalFraction(request)
    else:
         return HttpResponse("no found !!!")
    return HttpResponse(json.dumps(callBackDict))


