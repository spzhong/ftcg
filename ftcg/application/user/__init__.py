# -*- coding: utf-8 -*-

from django.http import HttpResponse
import json
import signAdmin
import userAdmin

from django.db import connections

def close_old_connections():
    for conn in connections.all():
        conn.close_if_unusable_or_obsolete()

def index(request,route):
    close_old_connections()
    if route == 'sign':
        callBackDict = signAdmin.signIn(request)
    elif route == 'autoSign':
        callBackDict = signAdmin.autoSign(request)
    elif route == 'signOut':
        callBackDict = signAdmin.signOut(request)
    elif route == 'register':
        callBackDict = userAdmin.registerUser(request)
    elif route == 'adminResetPassword':
        callBackDict = userAdmin.adminResetPassword(request)
    elif route == 'resetPassword':
        callBackDict = userAdmin.resetPassword(request)
    elif route == 'info':
        callBackDict = userAdmin.info(request)
    elif route == 'getAllUserList':
        callBackDict = userAdmin.getAllUserList(request)
    elif route == 'adminDeleteUser':
        callBackDict = userAdmin.adminDeleteUser(request)
    elif route == 'updateInfo':
        callBackDict = userAdmin.updateInfo(request)
    elif route == 'upandexchangeUserInfo':
        callBackDict = userAdmin.upandexchangeUserInfo(request)
    else:
         return HttpResponse("no found !!!")
    return HttpResponse(json.dumps(callBackDict))

