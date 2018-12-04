# -*- coding: utf-8 -*-

from django.http import HttpResponse
import json
from django.shortcuts import render

def index(request):
     return render(request, 'index.html')

def api(request):
    return render(request, '/api/index.html')
