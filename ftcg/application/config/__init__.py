# -*- coding: utf-8 -*-
import json
import assessmentType
import configAdmin

from django.db import connections
from django.http import HttpResponse

def close_old_connections():
    for conn in connections.all():
        conn.close_if_unusable_or_obsolete()


def index(request,route):
    close_old_connections()
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
    elif route == 'editConfigAssessment':
        callBackDict = assessmentType.editConfigAssessment(request)
    elif route == 'editBaseConfigVillage':
        callBackDict = configAdmin.editBaseConfigVillage(request)
    elif route == 'editBaseConfigCommunity':
        callBackDict = configAdmin.editBaseConfigCommunity(request)
    elif route == 'editBaseConfigStreet':
        callBackDict = configAdmin.editBaseConfigStreet(request)
    elif route == 'addAssessmentQuestion':
        callBackDict = assessmentType.addAssessmentQuestion(request)
    elif route == 'delAssessmentQuestion':
        callBackDict = assessmentType.delAssessmentQuestion(request)
    elif route == 'adminGetVillages':
        callBackDict = configAdmin.adminGetVillages(request)
    elif route == 'searchVillage':
        callBackDict = configAdmin.searchVillage(request)
    elif route == 'createErCodeInfo':
        callBackDict = configAdmin.createErCodeInfo(request)
    elif route == 'propertySendBags':
        callBackDict = configAdmin.propertySendBags(request)
    elif route == 'getPropertySendList':
        callBackDict = configAdmin.getPropertySendList(request)
    elif route == 'adminGetBagSendList':
        callBackDict = configAdmin.adminGetBagSendList(request)
    else:
         return HttpResponse("no found !!!")
    return HttpResponse(json.dumps(callBackDict))

