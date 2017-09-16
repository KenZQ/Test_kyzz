from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *

# Create your views here.
from user.views import islogin
from cart.models import CartInfo
from goods.models import *


@islogin
def cart(request):
    uid = request.session['pid']
    carts = CartInfo.objects.filter(user_id=uid)
    count = carts.count
    context = {
        'title': '购物车',
        'name': 1,
        'carts': carts,
        'count':count,
    }
    return render(request, 'cart/cart.html', context)


@islogin
def add(request, gid, count):
    uid = request.session['pid']
    gid = int(gid)
    count = int(count)

    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)
    if len(carts) >= 1:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    cart.save()

    if request.is_ajax():
         count = CartInfo.objects.filter(user_id=request.session['pid']).count()
         return JsonResponse({'count': count})

    return render(request)


@islogin
def buy(request):
    dict = request.POST
    uid = request.session['pid']
    good_id = dict.get('good_id')
    good_count = dict.get('good_count')
    good = GoodsInfo.objects.get(id=good_id)
    if int(good_count) > int(good.gkucun):
        return HttpResponse("库存不足<a href='http://127.0.0.1:8000/good_detail%s/'>返回</a>" % good_id)
    cart = CartInfo()
    cart.user_id = uid
    cart.count = good_count
    cart.goods_id = good_id
    cart.save()
    request.session['cart_id'] = cart.id
    return redirect('/detail/buy/')


@islogin
def edit(request, cart_id, count):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        count1 = cart.count = int(count)
        cart.save()
        data = {'ok': 0}
    except Exception as e:
        data = {'ok': count1}
    return JsonResponse(data)


@islogin
def delete(request, cart_id):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data = {'ok': 1}
    except Exception as e:
        data = {'ok': 0}
    return JsonResponse(data)
