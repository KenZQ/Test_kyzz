from django.conf.urls import include, url

from goods import views

urlpatterns = [
    url('^$',views.index),
    url(r'^list(\d+)(\d+)(\d+)/$', views.list),
    url(r'^good_detail(\d+)/$',views.detail),
 ]