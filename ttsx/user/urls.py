from django.conf.urls import url
from . import views

urlpatterns = [
    url('^register/$', views.register),
    url('^login/$', views.login),
    url('^verify_msg/$', views.verify_msg),
    url('^register_msg/$', views.register_msg),
    url('^isexit/$', views.isexit),
    url(r'^active(\d+)/$', views.active),
    url('^user_center_info/$', views.user_center_info),
    url('^user_center_site/$', views.user_center_site),
    url('^exit/$', views.user_exit),
    url('^edit_addr_msg/$', views.edit_addr_msg),
    url('^getmsg/$', views.getmsg),
    url('^top_area/$', views.top_area)

]
