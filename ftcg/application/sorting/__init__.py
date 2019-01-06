# -*- coding: utf-8 -*-
import json
import sortingAdmin


from django.http import HttpResponse

def index(request,route):
    if route == 'upSorting':
        callBackDict = sortingAdmin.upSorting(request)
    elif route == 'getAllSortingInfo':
        callBackDict = sortingAdmin.getAllSortingInfo(request)
    elif route == 'getSortingVillage':
        callBackDict = sortingAdmin.getSortingVillage(request)
    elif route == 'getSortingcommunity':
        callBackDict = sortingAdmin.getSortingcommunity(request)
    elif route == 'getSortingStreet':
        callBackDict = sortingAdmin.getSortingStreet(request)
    else:
         return HttpResponse("no found !!!")
    return HttpResponse(json.dumps(callBackDict))

