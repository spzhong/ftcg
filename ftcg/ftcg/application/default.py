# -*- coding: utf-8 -*-

from django.http import HttpResponse
import json
from django.shortcuts import render

def index(request):
     #return HttpResponse('hello1')
     return render(request, 'index.html')
