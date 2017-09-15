#-*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url('^order/$',views.order),
    url('^$',views.order),
    url('^user_center_order/$',views.pay),#展示用户的订单
]
