# -*- coding: utf-8 -*-
import json
import sortingAdmin

from django.http import HttpResponse

from django.db import connections
def close_old_connections():
    for conn in connections.all():
        conn.close_if_unusable_or_obsolete()


def index(request,route):
    close_old_connections()
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
    elif route == 'deleteSortingInfo':
        callBackDict = sortingAdmin.deleteSortingInfo(request)
    elif route == 'sweepcCodeSorting':
        callBackDict = sortingAdmin.sweepcCodeSorting(request)
    else:
         return HttpResponse("no found !!!")
    return HttpResponse(json.dumps(callBackDict))

