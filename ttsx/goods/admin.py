from django.contrib import admin

# Register your models here.
from goods.models import TypeInfo, GoodsInfo

admin.site.register(TypeInfo)
admin.site.register(GoodsInfo)