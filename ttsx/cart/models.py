#coding=utf-8
from django.db import models


# 购物车
class CartInfo(models.Model):
    user=models.ForeignKey('user.UserInfo')
    goods=models.ForeignKey('goods.GoodsInfo')
<<<<<<< HEAD
    count=models.IntegerField()
=======
    count=models.IntegerField()
>>>>>>> eb56ee4ff6af628628001f5376ec6db14738889d
