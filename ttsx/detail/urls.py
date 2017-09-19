#-*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^order/$',views.order),
    url('^user_center_order/$',views.pay),#展示用户的订单
    url('^handle/$',views.handle),
    url('^buy/$', views.buy),
    url(r'^user_center_order(\d*)/$', views.user_center_order),
]
