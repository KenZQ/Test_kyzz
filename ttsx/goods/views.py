from django.core.paginator import Paginator
from django.shortcuts import render

from cart.models import *
from goods.models import *


# 首页视图
def index(request):
    # 获得最新火的4个商品
    hot = GoodsInfo.objects.all().order_by('gclick')[0:4]
    context = {'guest_cart': 1, 'title': '首页', 'hot': hot}
    # 获得分类下的点击商品,下面拿出来的是一个装有字典的列表，就是各个对象
    typelist = TypeInfo.objects.all()
    for i in range(len(typelist)):
        type = typelist[i]
        # 加上负号，就是倒序排序，order_by默认升序排列，按照id倒序排序
        goods1 = type.goodsinfo_set.order_by('-id')[0:4]
        # 按照点击量倒序排序
        goods2 = type.goodsinfo_set.order_by('-glick')[0:4]
        key1 = 'type' + str(i)
        key2 = 'type' + str(i) + str(i)
        context.setdefault(key1, goods1)
        context.setdefault(key2, goods2)
    return render(request, 'goods/index.html', context)


def list(request, tid, sid, pindex):
    type = TypeInfo.objects.get(pk=int(tid))
    news = type.goodsinfo_set.order_by('-id')[0:2]
    # 按照id降序排列
    if sid == '1':
        good_list = type.goodsinfo_set.order_by('-id')
    # 按价格
    if sid == '2':
        good_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    # 按照点击量
    if sid == '3':
        good_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    # 创建paginator分页对象,根据上面的分类显示，每页显示10个
    paginator = Paginator(good_list, 10)
    # 返回page对象，包含商品信息
    page = paginator.page(int(pindex))
    context = {'title': '商品列表', 'guest_cart': 1, 'page': page, 'paginator': paginator, 'typeinfo': type, 'sort': sid,
               'news': news}
    return render(request, 'goods/model01.html')
    # def list(request):


#     value=request.POST.get('s1')
def model01(request):
    return render(request, 'goods/model01.html')


def model02(request):
    return render(request, 'goods/model02.html')


def model03(request):
    return render(request, 'goods/model03.html')


def model04(request):
    return render(request, 'goods/model04.html')


def model05(request):
    return render(request, 'goods/model05.html')


def model06(request):
    return render(request, 'goods/model06.html')


# def count(request):
#     sum=models.objects.all().values('count')
def detail(request):
    return render(request, 'goods/detail.html')
