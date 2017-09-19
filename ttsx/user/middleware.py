'''
urlpatterns = [
    url('^reset/$', views.reset),
    url('^reset_psw/$', views.reset_psw),
    url(r'^reset_page(\d+)/$', views.reset_page),
    url(r'^reset_pwd(\d+)/$', views.reset_pwd),
    get_full_path
]

'''
import re


class UserStatus:

    def process_view(self, request, view_func, view_args, view_kwargs):

        no_path = [
            '/user/register/',
            '/user/register_msg/',
            '/user/login/',
            '/user/isexit/',
            '/user/verify_msg/',
            '/user/verify_fail/',
            '/user/verify_code/',
            "/user/r'active(\d+)/'",
            '/user/isexit/',
            '/user/yzm/',
            '/user/top_area/',

        ]
        if request.path not in no_path :
            request.session['prev_page'] = request.get_full_path()



    # def process_response(self, request, response):
    #     return response

