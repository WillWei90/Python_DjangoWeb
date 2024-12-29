from django.contrib import admin

from webapp.models import Product, Cart, Order

# Register your models here.
# 註冊 Prodcut 由後台管理 (Model 資料模型)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)