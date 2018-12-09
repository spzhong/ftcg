# -*- coding: utf-8 -*-

from django.http import HttpResponse
import json
import signAdmin
import userAdmin

def index(request,route):
    if route == 'sign':
        callBackDict = signAdmin.signIn(request)
    elif route == 'signOut':
        callBackDict = signAdmin.signOut(request)
    elif route == 'register':
        callBackDict = userAdmin.registerUser(request)
    elif route == 'changePassword':
        callBackDict = userAdmin.changePassword(request)
    elif route == 'firstPassword':
        callBackDict = userAdmin.firstPassword(request)
    elif route == 'info':
        callBackDict = userAdmin.info(request)
    elif route == 'getAllUserList':
        callBackDict = userAdmin.getAllUserList(request)
    else:
         return HttpResponse("no found !!!")
    return HttpResponse(json.dumps(callBackDict))

