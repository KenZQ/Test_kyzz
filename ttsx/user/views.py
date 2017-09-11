from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from . import task
from .models import *

from hashlib import sha1


# Create your views here.
def register(request):
    return render(request, 'user/register.html')


# 注册
def register_msg(request):
    dict = request.POST
    new_user_name = dict.get('user_name')

    try:
        if UserInfo.objects.get(uname=new_user_name):
            return HttpResponse('用户已经存在')
    except:
        pass

    new_user_email = dict.get('email')
    pwd2 = dict.get('pwd')
    pwd = pwd2.encode('utf-8')
    new_user_pwd = sha1(pwd).hexdigest()

    new_user = UserInfo()
    new_user.uname = new_user_name
    new_user.upwd = new_user_pwd
    new_user.uemail = new_user_email
    request.session['user_name'] = new_user_name
    request.session['email'] = new_user_email
    new_user.save()
    # return redirect('/user/send/?email=%s'%new_user_email)
    # request.session['passwd'] = new_user_pwd
    # return redirect('/login2/?user_name=%s&pwd=%s'%(new_user_name,new_user_pwd))
    return redirect('/user/send/')


def send(request):
    task.send(request)
    return render(request, 'user/login.html')


# 登录
def login(request):
    return render(request, 'user/login.html')


# 登录验证
def verify_msg(request):
    dict = request.POST
    # if dict.get('test').upper() != request.session['verifycode'].upper():
    #     return HttpResponse('验证码错误')
    user_name = dict.get('username')
    try:
        document = UserInfo.objects.filter(isValid=True).get(uname=user_name)
    except:
        return HttpResponse('用户名不存在')

    upwd = dict.get('pwd').encode('utf-8')
    user_pwd = sha1(upwd).hexdigest()

    if user_pwd != document.upwd:
        return HttpResponse('密码错误')

    if not document.isActive:
        return HttpResponse('未激活')
    request.session.set_expiry(600)
    request.session['pid'] = document.id
    # referer_web = request.META['HTTP_REFERER']
    try:
        referer_web = request.COOKIES['origin_addr']
        return redirect(referer_web)
    except:
        pass

    return redirect('/user/user_center_info/')


# 注册后提示激活
def active(request):
    try:
        uname = request.session['user_name']
    except:
        return
    user = UserInfo.objects.filter(isValid=True).get(uname=uname)
    user.isActive = True
    user.save()
    return HttpResponse('成功激活')


# 判断是否已经登录
def islogin(fn):
    def inner(request):
        try:
            if request.session['pid']:
                pass
        except:
            return render(request, 'user/login.html')
        return fn(request)

    return inner


@islogin
def user_center_info(request):
    return render(request, 'user/user_center_info.html')


@islogin
def user_center_site(request):
    return render(request, 'user/user_center_site.html')


# 用户中心，个人信息
def get_user_msg(request):
    try:
        usermsg = UserAddressInfo.objects.get(user_id=request.session['pid'])
        name = usermsg.uname
        addr = usermsg.uaddress
        phone = usermsg.uphone
        ulist = {'name': name, 'addr': addr, 'phone': phone}
    except:
        ulist = {}
    return JsonResponse(ulist)


# 点击退出，清除ｓｅｓｓｉｏｎ
def user_exit(request):
    request.session.flush()
    return redirect('/')


# 编辑个人信息，如收货地址
def edit_addr_msg(request):
    dict = request.POST
    user_id = request.session['pid']
    try:
        usermsg = UserAddressInfo.objects.get(user_id=user_id)
    except:
        usermsg = UserAddressInfo()
    usermsg.uname = dict.get('recipients')
    usermsg.uaddress = dict.get('addr')
    usermsg.uphone = dict.get('phone')
    usermsg.user_id = user_id

    usermsg.save()

    return render(request, 'user/user_center_site.html')


# 获取个人地址信息
def getmsg(request):
    try:
        usermsg = UserAddressInfo.objects.get(user_id=request.session['pid'])
        name = usermsg.uname
        addr = usermsg.uaddress
        phone = usermsg.uphone
        ulist = {'name': name, 'addr': addr, 'phone': phone}
    except:
        ulist = {}
    return JsonResponse(ulist)


# 页面顶部是否登录的信息
def top_area(request):
    try:
        id = request.session['pid']
    except:
        return JsonResponse()

    user = UserAddressInfo.objects.get(user_id=id)
    context = {'uname': user.uname}
    return JsonResponse(context)
