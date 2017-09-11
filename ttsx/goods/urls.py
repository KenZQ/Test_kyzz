from django.conf.urls import include, url

from goods import views

urlpatterns = [
    url('^$',views.index),
    url(r'^model(\d+)/$',views.model_show),
    url(r'^list(\d+)(\d+)(\d+)/$', views.list),
    url('^detail/$',views.detail),
 ]