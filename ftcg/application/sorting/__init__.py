# -*- coding: utf-8 -*-
import json
import sortingAdmin


from django.http import HttpResponse

def index(request,route):
    if route == 'upSorting':
        callBackDict = sortingAdmin.upSorting(request)
    elif route == 'sortingInfo':
        callBackDict = sortingAdmin.sortingInfo(request)
    elif route == 'sortingVillageInfo':
        callBackDict = sortingAdmin.sortingVillageInfo(request)
    elif route == 'sortingStreetInfo':
        callBackDict = sortingAdmin.sortingVillageInfo(request)
    else:
         return HttpResponse("no found !!!")
    return HttpResponse(json.dumps(callBackDict))