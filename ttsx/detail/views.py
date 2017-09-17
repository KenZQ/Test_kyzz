#couding=utf-8
from _decimal import Decimal

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.db import transaction

from cart.models import CartInfo
from detail.models import OrderInfo, OrderDetailInfo
from user import views

# Create your views here.
from django.utils.datetime_safe import datetime

# 显示订单
from user.models import *

@views.islogin
def order(request):
    user_addr = UserAddressInfo.objects.filter(user_id=request.session['pid'])
    cart_ids = request.GET.getlist('cart_id')
    carts = []
    for cart_id in cart_ids:
        carts.append(CartInfo.objects.get(id=cart_id))

    context = {'carts':carts, 'user':user_addr, 'title':'订单提交'}

    return render(request,'detail/order.html',context)

@views.islogin
def buy(request):
    user_addr = UserAddressInfo.objects.filter(user_id=request.session['pid'])
    cart_id = request.session['cart_id']
    cart = CartInfo.objects.get(id=cart_id)
    carts = [cart]
    context = {'carts':carts, 'user':user_addr}

    return render(request,'detail/order.html',context)



'''
事物：一旦操作失败则全部回退
1、创建订单对象
2、判断商品的库存  库存小于购买数量，不能购买成功
3、创建详单对象
4、修改商品库存
5、删除购物车


'''
# 处理订单视图
@transaction.atomic
@views.islogin
def handle(request):
    tran_id = transaction.savepoint()
    uid = request.session['pid']
    dict = request.POST
    cart_id = dict.getlist('cart_id')

    now = datetime.now()
    order_id = '%s%d' % (now.strftime('%Y%m%d%H%M%S'), uid)
    carts = []
    for cpk in cart_id:
       carts.append(CartInfo.objects.get(id=cpk))


    order = OrderInfo()
    order.oid = order_id
    order.user = UserInfo.objects.get(id=uid)
    order.ototal = dict.get('pay')
    order.oaddress = dict.get('addr')
    order.save()
    for c in carts:
        if c.count > c.goods.gkucun:
            transaction.savepoint_rollback(tran_id)
            return redirect('/cart/')


        order_detail = OrderDetailInfo()
        order_detail.goods= c.goods
        order_detail.count = c.count
        order_detail.price = int(c.goods.gprice) * int(c.count)
        order_detail.order_id = order_id
        order_detail.save()
        c.delete()
    transaction.savepoint_commit(tran_id)
    return redirect('/detail/user_center_order1/')



def user_center_order(request,pindex):

    uid = request.session['pid']
    orders = OrderInfo.objects.filter(user_id=uid).order_by('-oid')
    if pindex == '':
        pindex = 1
    p = Paginator(orders,3)
    pIndex = int(pindex)
    list2 = p.page(pIndex)
    context = {'list': list2,'prange':p.page_range,'title':'个人订单'}
    return render(request, 'detail/user_center_order.html', context)






@views.islogin
def pay(request,oid):
    order = OrderInfo.objects.get(oid=oid)
    order.oIsPay = True
    order.save()
    context = {'oder':order}
    return render(request,'detail/pay.html',context)




















"""
   # 获取订单

    # 获取地址
    address = request.POST.get()['uaddress']
    # 获取姓名
    uName = request.POST.get()['uName']

    # 获取联系方式
    uPhone = request.POST.get()['uphone']

    # 获取支付方式
    num = request.POST.get()['way']
    if num == 0:
        wayOfPay = '货到付款'

    elif num == 1:
        wayOfPay = '微信支付'

    elif num == 2:
        wayOfPay = '支付宝支付'

    else:
        wayOfPay = '银联支付'


    # 获取商品信息

    #获取商品名称
    goods = request.POST.get()['gtitle'] #按名称
    goods_name =[]
    for good in goods:
        goods_name.append(good)

    #获得商品价格
    goods_price = request.POST['gprice']
    #获得商品数量
    goods_count = request.POST['count']
    #生成订单号 = 当前时间 + 用户编号-->order_id
    time = datetime.time()
    user_id = request.POST['user_id']
    order_id = '' + time
    order_id += user_id

    context = {
        'address':address,
        'uname':uName,
        'uphone':uPhone,
        'gtitle':goods_name,
        'gprice':goods_price,
        'gcount':goods_count,
        'order_id':order_id
    }
    return render(request,'detail/user_center_order.html',context)
"""










# 订单查询
def orderQuery(request):

    pass
