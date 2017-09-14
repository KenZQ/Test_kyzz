from django.conf.urls import include, url

from . import views

urlpatterns = [
    url('^$',views.index),
    url('^detail/$',views.detail),
    url('^cart.html',views.detail),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^list(\d+)(\d+)(\d+)/$', views.list),
    url(r'^good_detail(\d+)/$',views.detail),

 ]