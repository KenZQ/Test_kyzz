class UserStatus:

    def process_request(self, request):
        pass
        # if request.GET.get('Referring'):
        #     # request.session['referer'] = request.META['HTTP_REFERER']
        #     request.session['referer'] = request.GET.get('Referring')

    def process_views(self, request, view_func, view_args, view_kwargs):
        origin_addr = request.META['HTTP_REFERER']
        if origin_addr != 'http://127.0.0.1:8000/user/login/' or origin_addr != 'http://127.0.0.1:8000/user/register/' or origin_addr != 'http://127.0.0.1:8000/user/active/' :
            request.COOKIES['origin_addr']

