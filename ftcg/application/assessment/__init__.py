# -*- coding: utf-8 -*-


from django.http import HttpResponse

def index(request,route):
    if route == '':
        callBackDict = {}
    else:
         return HttpResponse("no found !!!")

