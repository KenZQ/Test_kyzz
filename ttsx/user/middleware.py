class UserStatus:
    def process_request(self, request):
        pass
    def process_views(self, request, view_func, view_args, view_kwargs):
        pass

    def process_response(self, request, response):
        try:
            origin_addr = request.META['HTTP_REFERER']
            response.set_cookie('origin_addr', 'http://127.0.0.1:8000/user/user_center_info/')

            if origin_addr != 'http://127.0.0.1:8000/user/login/' and origin_addr != 'http://127.0.0.1:8000/user/register/' and origin_addr != 'http://127.0.0.1:8000/user/active/' and origin_addr != 'http://127.0.0.1:8000/':
                response.set_cookie('origin_addr', origin_addr)
        except:
            pass
        return response
