# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse

def index(request,route):
    if route == '':
        callBackDict = {}
    else:
         return HttpResponse("no found !!!")
    return HttpResponse(json.dumps(callBackDict))