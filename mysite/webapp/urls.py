# 殷志忠老師 (TeacherYin.com)
from django.urls import path
# 從目前套件載入 from .
from . import views

urlpatterns = [
    # path('', views.index()),
    # 網址路徑 對映 哪個 view 函數
    path('', views.menu, name='index'),
    path('menu/', views.menu, name='menu'),
    path('cart/', views.cart, name='cart'),
    path('del_cart/', views.del_cart, name='del_cart'),

    path('submit_cart/', views.submit_cart, name='submit_cart'),
    path('submit_order/', views.submit_order, name='submit_order'),

    path('show_order/', views.show_order, name='show_order'),
    path('download/', views.download, name='download'),

    path('bar/', views.bar, name='bar'),
]