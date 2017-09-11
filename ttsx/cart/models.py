#coding=utf-8
from django.db import models

# 购物车
class CartInfo(models.Model):
    user=models.ForeignKey('user.UserInfo')
    goods=models.ForeignKey('goods.GoodsInfo')
    count=models.IntegerField()
