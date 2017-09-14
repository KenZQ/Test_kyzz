from django.conf.urls import include, url

from . import views
from .views import *

urlpatterns = [
    url('^$',views.index),
    url(r'^list(\d+)(\d+)(\d+)/$', views.list),
    url(r'^good_detail(\d+)/$',views.detail),
    url('^search/$', MySearchView())
 ]