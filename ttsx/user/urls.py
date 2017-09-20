from django.conf.urls import url
from . import views

urlpatterns = [
    url('^register/$', views.register),
    url('^login/$', views.login),
    url('^verify_msg/$', views.verify_msg),
    url('^verify_fail/$', views.verify_fail),
    url('^verify_code/$', views.verify_code),
    url('^yzm/$', views.yzm),
    url('^register_msg/$', views.register_msg),
    url('^isexit/$', views.isexit),
    url(r'^active(\d+)/$', views.active),
    url('^user_center_info/$', views.user_center_info),
    url('^user_center_site/$', views.user_center_site),
    url('^exit/$', views.user_exit),
    url('^edit_addr_msg/$', views.edit_addr_msg),
    url('^top_area/$', views.top_area),
    url('^reset/$', views.reset),
    url('^reset_psw/$', views.reset_psw),
    url(r'^reset_page(\d+)/$', views.reset_page),
    url(r'^reset_pwd(\d+)/$', views.reset_pwd),
    url(r'^addr_del(\d+)/$', views.addr_del),
    url('^delivery_addr/$', views.delivery_addr),


]
