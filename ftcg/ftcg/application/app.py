# -*- coding: utf-8 -*-

from django.http import HttpResponse
import json
from .logicApp import userAdmin


def index(request,route):
    if route == 'sign':
        callBackDict = userAdmin.signUser(request)
    elif route == 'register':
        callBackDict = userAdmin.registerUser(request)
    elif route == 'updateUser':
        callBackDict = userAdmin.updateUser(request)
    else:
         return HttpResponse("Hello world ! ")
    return HttpResponse(json.dumps(callBackDict))
