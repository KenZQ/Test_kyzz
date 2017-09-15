#-*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url('^order/$',views.order),
    url('^handle/$',views.handle),
    url(r'^user_center_order(\d*)/$', views.user_center_order)
]
