from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import  *

# Create your views here.
def cart(request):
    uid=request.session['pid']
    carts=CartInfo.objects.filter(user_id=uid)
    context={
        'title':'购物车',
        'page_name':1,
        'carts':carts
    }
    return render(request, 'cart/cart.html',context)

def add(request,gid,count):
    uid=request.session['pid']
    gid=int(gid)
    count=int(count)

    carts=CartInfo.objects.filter(user_id=uid,goods_id=gid)
    if len(carts)>=1:
        cart=carts[0]
        cart.count=cart.count+count
    else:
        cart=CartInfo()
        cart.user_id=uid
        cart.goods_id=gid
        cart.count=count
    cart.save()

    if request.is_ajax():
        count=CartInfo.objects.filter(user_id=request.session['pid']).count()
        return JsonResponse({'count':count})
    else:
        return credits('/cart/')

def edit(request,cart_id,count):
    try:
        cart=CartInfo.objects.get(pk=int(cart_id))
        count1=cart.count=int(count)
        cart.save()
        data={'ok':0}
    except Exception as e:
        data={'ok':count1}
    return JsonResponse(data)

def delete(request,cart_id):
    try:
        cart=CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data={'ok':1}
    except Exception as e:
        data={'ok':0}
    return JsonResponse(data)