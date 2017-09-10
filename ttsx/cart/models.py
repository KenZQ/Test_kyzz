#coding=utf-8
from django.db import models

# 购物车
class CartInfo(models.Model):
    user=models.ForeignKey('df_user.UserInfo')
    goods=models.ForeignKey('df_goods.GoodsInfo')
    count=models.IntegerField()