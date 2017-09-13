#couding=utf-8
from _decimal import Decimal

from django.shortcuts import render, redirect
from django.db import transaction

from cart.models import CartInfo
from detail.models import OrderInfo, OrderDetailInfo
from user import views

# Create your views here.
from django.utils.datetime_safe import datetime


# 提交订单视图
@transaction.atomic
@views.islogin
def account(request):
    tran_id = transaction.savepoint()

    cart_ids = request.POST.get('cart_ids')
    try:
        order = OrderInfo()
        now = datetime.now()
        uid = request.session['user_id']
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
            if goods.gkucun >= cart.count:
                # 减去库存
                goods.gkucun = cart.goods.gkucun - cart.count
                goods.save()

                #填写订单信息
                detail.goods_id = goods.id
                detail.price = goods.gprice
                detail.count = cart.count
                detail.save()
                cart.delete()
            else:
                transaction.savepoint_rollback(tran_id)
                return redirect('/cart/')
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print(e)
        transaction.savepoint_rollback(tran_id)

    return redirect('/user/order/')

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
