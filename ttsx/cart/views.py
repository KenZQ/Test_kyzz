from django.shortcuts import render

# Create your views here.
import user
from cart.models import CartInfo



def cart(request):
    uid = request.session.get('uid')
    carts = CartInfo.objects.filter(user_id=uid)
    context = {
        'title':'购物车',
        'name':1,
        'carts':carts,
               }
    return render(request,'cart/cart.html',context)

