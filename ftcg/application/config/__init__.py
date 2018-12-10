# -*- coding: utf-8 -*-
import json
import configAdmin
import questionAdmin
import roomAdmin

from django.http import HttpResponse

def index(request,route):
    if route == 'baseConfigQuestion':
        callBackDict = questionAdmin.baseConfigQuestion(request)
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
        callBackDict = questionAdmin.deleteConfigQuestion(request)
    elif route == 'getConfigQuestion':
        callBackDict = questionAdmin.getConfigQuestion(request)
    elif route == 'addRoomNum':
        callBackDict = roomAdmin.addRoomNum(request)
    elif route == 'deleteRoomNum':
        callBackDict = questionAdmin.deleteRoomNum(request)
    else:
         return HttpResponse("no found !!!")
    return HttpResponse(json.dumps(callBackDict))





