from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from cart.models import *
from goods.models import *


# 首页视图
def index(request):
    types = TypeInfo.objects.all()
    typelist = []
    for gtype in types:
        hot = gtype.goodsinfo_set.order_by('gclick')[0:3]
        new = gtype.goodsinfo_set.order_by('-id')[0:4]
        typelist.append({'type':gtype,'hot':hot, 'new':new})

    # 购物车的商品数量
    try:
        uid = request.session['pid']
        carts = CartInfo.objects.filter(user_id=uid)
    except:
        carts = []
    count = len(carts)
    context = {'typelist': typelist, 'count': count,'title':'首页'}

    return render(request, 'goods/index.html', context)


def list(request, tid, sid, pindex):
    gtype = TypeInfo.objects.get(pk=int(tid))
    news = gtype.goodsinfo_set.order_by('-id')[0:2]
    if sid == '1':
        good_list = gtype.goodsinfo_set.order_by('-id')
    if sid == '2':
        good_list = gtype.goodsinfo_set.order_by('-gprice')
    if sid == '3':
        good_list = gtype.goodsinfo_set.order_by('-gclick')
    # 创建paginator分页对象,根据上面的分类显示，每页显示10个
    paginator = Paginator(good_list, 10)
    # 返回page对象，包含商品信息
    page = paginator.page(int(pindex))

    # 购物车的商品数量
    try:
        uid = request.session['pid']
        carts = CartInfo.objects.filter(user_id=uid)
    except:
        carts = []
    count = len(carts)

    context = {'page': page, 'paginator': paginator, 'typeinfo': gtype, 'sort': sid,
               'news': news, 'type_id': tid, 'count': count, 'title':'商品列表'}
    return render(request, 'goods/list.html', context)


def detail(request, id):
    # 购物车的商品数量
    try:
        uid = request.session['pid']
        carts = CartInfo.objects.filter(user_id=uid)
    except:
        carts = []

    count = len(carts)

    try:
        good = GoodsInfo.objects.get(id=id)
        good.gclick += 1
        good.save()
        newgoods = good.gtype.goodsinfo_set.order_by('-id')[0:2]
        context = {'good': good, 'news': newgoods, 'count':count, 'title':'商品详细'}
        response=  render(request, 'goods/detail.html', context)

        gid = '%s' % good.id
        if 'ghistory' not in request.COOKIES:
            alist = [gid,]
        else:
            a= request.COOKIES['ghistory']
            alist = a.split('+')
            if gid in alist:
                alist.remove(gid)

            alist.insert(0, gid)
            if len(alist)>5:
                alist.pop()
        response.set_cookie('ghistory', '+'.join(alist), expires=86400 * 8)
        return response

    except:
        return HttpResponse('您的网络可能有问题')


from haystack.views import SearchView


class MySearchView(SearchView):
    def extra_context(self):
        context = super(MySearchView, self).extra_context()
        context['title'] = '商品搜索'
        uid = self.request.session['pid']
        context['count'] = len(CartInfo.objects.filter(user_id=uid))
        return context
