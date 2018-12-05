"""testFtcg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin

from .application import config
from .application import user
from .application import assessment
from .application import sorting
from .application import statistics


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^testftcg/config/([a-z,A-Z]+)$', config.index),
    url(r'^testftcg/user/([a-z,A-Z]+)$', user.index),
    url(r'^testftcg/assessment/([a-z,A-Z]+)$', assessment.index),
    url(r'^testftcg/sorting/([a-z,A-Z]+)$', sorting.index),
    url(r'^testftcg/statistics/([a-z,A-Z]+)$', statistics.index),
]
