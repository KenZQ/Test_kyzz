from django.conf.urls import include, url

from goods import views

urlpatterns = [
    url('^$',views.index),
    url('^model01/$',views.model01),
    url('^model01/$',views.model02),
    url('^model02/$',views.model03),
    url('^model03/$',views.model04),
    url('^model04/$',views.model05),
    url('^model05/$',views.model06),

 ]