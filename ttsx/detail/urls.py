#-*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url('^order/$',views.order),
    url('^$',views.handle)
]
