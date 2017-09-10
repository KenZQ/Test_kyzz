from django.conf.urls import include, url

from goods import views

urlpatterns = [
    url('^$',views.index)
 ]