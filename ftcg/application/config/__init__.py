# -*- coding: utf-8 -*-
import json
import configAdmin
import assessmentType


from django.http import HttpResponse

def index(request,route):
    if route == 'baseConfigAssessment':
        callBackDict = assessmentType.baseConfigAssessment(request)
    elif route == 'baseConfigStreet':
        callBackDict = configAdmin.baseConfigStreet(request)
    elif route == 'baseConfigVillage':
        callBackDict = configAdmin.baseConfigVillage(request)
    elif route == 'getVillages':
        callBackDict = configAdmin.getVillages(request)
    elif route == 'getStreets':
        callBackDict = configAdmin.getStreets(request)
    elif route == 'deleteStreet':
        callBackDict = configAdmin.deleteStreet(request)
    elif route == 'deleteVillage':
        callBackDict = configAdmin.deleteVillage(request)
    elif route == 'deleteConfigAssessment':
        callBackDict = assessmentType.deleteConfigAssessment(request)
    elif route == 'getConfigAssessment':
        callBackDict = assessmentType.getConfigAssessment(request)
    elif route == 'baseConfigCommunity':
        callBackDict = configAdmin.baseConfigCommunity(request)
    elif route == 'deleteCommunity':
        callBackDict = configAdmin.deleteCommunity(request)
    elif route == 'getCommunitys':
        callBackDict = configAdmin.getCommunitys(request)
    elif route == 'openVillage':
        callBackDict = configAdmin.openVillage(request)
    elif route == 'closeVillage':
        callBackDict = configAdmin.closeVillage(request)
    else:
         return HttpResponse("no found !!!")
    return HttpResponse(json.dumps(callBackDict))





openVillage