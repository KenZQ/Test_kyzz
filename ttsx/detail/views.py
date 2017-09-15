#couding=utf-8
from _decimal import Decimal

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

    context = {'carts':carts, 'user':user_addr}

    return render(request,'detail/order.html',context)




'''
事物：一旦操作失败则全部回退
1、创建订单对象
2、判断商品的库存
3、创建详单对象
4、修改商品库存
5、删除购物车
'''
# 处理订单视图
@transaction.atomic
@views.islogin
def handle(request):
    tran_id = transaction.savepoint()
    cart_ids = request.POST.get('cart_ids')
    try:
        order = OrderInfo()
        now = datetime.now()
        uid = request.session['pid']
        order_id = '%s%d'%(now.strftime('%Y%m%d%H%M%S'),uid)
        order.user_id = uid
        order.odate = now
        order.ototal = Decimal(request.POST.get('total'))
        order.save()

        # 创建订单对象
        cart_ids1 = [int(item) for item in cart_ids.split(',')]
        for id1 in cart_ids1:
            detail = OrderDetailInfo()
            detail.order = order
            #查询购物车信息
            cart = CartInfo.objects.get(id = id1)
            goods = cart.goods
            # 判断库存
            if goods.gkucun >= cart.count:#库存大于等于购买数量，可以下单成功
                # 减去库存
                goods.gkucun = cart.goods.gkucun - cart.count
                goods.save()
                #填写订单信息
                detail.goods_id = goods.id
                detail.price = goods.gprice
                detail.count = cart.count
                detail.save()
                # 删除购物车
                cart.delete()
            else:#库存小于购买数量，不能购买成功
                transaction.savepoint_rollback(tran_id)
                return redirect('/cart/')
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print(e)
        transaction.savepoint_rollback(tran_id)

    return redirect('/detail/order/')



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
    return render(request,'detail/account.html',context)
"""










# 订单查询
def orderQuery(request):

    pass
