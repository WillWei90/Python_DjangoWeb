from django.http import HttpResponse
from django.shortcuts import render, redirect

from webapp.models import Product, Cart
import json

# Create your views here.
# request  前端網頁請求資訊
def index(request):
    # HttpResponse 類別  回應給瀏覽器的網頁內容
    # return HttpResponse("首頁畫面")
    return render(request, 'index.html')


def menu(request):
    # QuerySet 可迭代 使用 for in 環圈 逐項讀取
    products = Product.objects.all()
    carts = Cart.objects.all()
    count = len(carts)
    渲染字典 = {'count': count,'products': products}
    # render 渲染畫面
    return render(request, 'menu.html', 渲染字典)

#刪除購物車某個產品
def del_cart(request):
    if request.method != 'POST':
        return HttpResponse('糟糕,提交有問題')

    # 取得 POST 請求 提供的字串資料
    data = request.POST["data"]

    # 字串 轉 字典
    data_dict = json.loads(data)
    pid = data_dict["pid"]

    #刪除 購物車 產品
    Cart.objects.get(pk=pid).delete()

    # (重導向畫面) 回應瀏覽器 訪問另一個 view
    url_name = 'cart'
    return redirect(url_name)
def submit_cart(request):
    if request.method != 'POST':
        return HttpResponse('糟糕,提交有問題')

    # 取得 POST 請求 提供的字串資料
    data = request.POST["data"]

    # 字串 轉 字典
    data_dict = json.loads(data)
    pid = data_dict["pid"]

    # 查詢 單筆 Product
    p = Product.objects.get(pk=pid)

    # 購物車 新增資料
    Cart.objects.create(product=p)

    # (重導向畫面) 回應瀏覽器 訪問另一個 view
    url_name = 'menu'
    return redirect(url_name)

def cart(request):
    # QuerySet 可迭代 使用 for in 環圈 逐項讀取
    carts = Cart.objects.all()

    渲染字典 = {'carts': carts}
    # render 渲染畫面
    return render(request, 'cart.html', 渲染字典)


def submit_order(request):
    # HttpResponse 類別  回應給瀏覽器的網頁內容
    return HttpResponse("處理訂單提交，施工中...")

def show_order(request):
    pass

def download(request):
    pass

def bar(request):
    pass






