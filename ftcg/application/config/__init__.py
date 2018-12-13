# -*- coding: utf-8 -*-
import json
import configAdmin
import assessmentType
import roomAdmin

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
    elif route == 'deleteConfigQuestion':
        callBackDict = assessmentType.deleteConfigAssessment(request)
    elif route == 'getConfigQuestion':
        callBackDict = assessmentType.getConfigAssessment(request)
    elif route == 'addRoomNum':
        callBackDict = roomAdmin.addRoomNum(request)
    elif route == 'deleteRoomNum':
        callBackDict = roomAdmin.deleteRoomNum(request)
    elif route == 'getRoomNumList':
        callBackDict = roomAdmin.getRoomNumList(request)
    else:
         return HttpResponse("no found !!!")
    return HttpResponse(json.dumps(callBackDict))





