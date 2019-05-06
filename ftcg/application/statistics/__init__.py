# -*- coding: utf-8 -*-
import json
import statisticsAdmin

from django.http import HttpResponse
from django.db import connections

def close_old_connections():
    for conn in connections.all():
        conn.close_if_unusable_or_obsolete()


def index(request,route):
    close_old_connections()
    if route == 'getAllStatistics':
        callBackDict = statisticsAdmin.getAllStatistics(request)
    elif route == 'getAssessmentStatistics':
        callBackDict = statisticsAdmin.getAssessmentStatistics(request)
    elif route == 'getSortingStatistics':
        callBackDict = statisticsAdmin.getSortingStatistics(request)
    elif route == 'getAllStreetsAssessmentStatistics':
        callBackDict = statisticsAdmin.getAllStreetsAssessmentStatistics(request)
    elif route == 'getAllStreetsSortingStatistics':
        callBackDict = statisticsAdmin.getAllStreetsSortingStatistics(request)
    elif route == 'getCommunitySortingStatistics':
        callBackDict = statisticsAdmin.getCommunitySortingStatistics(request)
    elif route == 'getVillageSortingStatistics':
        callBackDict = statisticsAdmin.getVillageSortingStatistics(request)
    elif route == 'getCommunityAssessmentStatistics':
        callBackDict = statisticsAdmin.getCommunityAssessmentStatistics(request)
    elif route == 'getVillageIdAssessmentStatistics':
        callBackDict = statisticsAdmin.getVillageIdAssessmentStatistics(request)
    else:
         return HttpResponse("no found !!!")
    return HttpResponse(json.dumps(callBackDict))




