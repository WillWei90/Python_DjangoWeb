import datetime

from django.db import models


# Create your models here.
# 設計自己 Model 繼承 Django 寫好的 Model (已經有 Manager可用)
# Model 設計完
#   激活， 到 mysite/settings.py 設定 INSTALLED_APPS
#   遷移資料庫 下指令
#       建立 遷移程式 0001.py
#       python manage.py makemigrations webapp
#       執行遷移
#       python manage.py migrate

class Product(models.Model):
    # 定義要在資料庫表格建立那些欄位
    # 欄位名稱 =  欄位種類 初值設定
    #           CharField 字串類型  長度限制  預設值
    #           IntegerField 整數類型 預設值

    # 編號  primary_key 代表最重要的欄位(主鍵)，值不能重複
    # id = models.IntegerField(primary_key=True)
    # django 會自動建立 id 可以省略

    # 設計自己 Model 繼承 Django 寫好的 Model (已經有 Manager可用)
    # Model 設計完
    #   激活， 到 mysite/settings.py 設定 INSTALLED_APPS
    #   遷移資料庫 下指令
    #       建立 遷移程式 0001.py
    #       python manage.py makemigrations webapp
    #       執行遷移
    #       python manage.py migrate

    # 餐點名稱
    title = models.CharField(max_length=100, default='')
    # 餐點價格
    price = models.IntegerField(default=0)
    # 簡介
    description = models.CharField(max_length=100, default='')
    # 圖片網址
    img_url = models.CharField(max_length=100, default='')

    # 字串函數
    def __str__(self):
        return f'{self.id} {self.title} {self.price} {self.description} {self.img_url}'


# 購物車
class Cart(models.Model):
    # 產品 ForeignKey 引用另一個資料模型 Model
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # 數量
    qty = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.id} {self.product} {self.qty}'


# 訂單
class Order(models.Model):
    # import datetime
    # 日期
    date = models.DateField(default=datetime.date(2024,1,1))
    # 桌號
    table_number = models.IntegerField(default=0)
    # 產品 ForeignKey 引用另一個資料模型 Model
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # 數量
    qty = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.table_number} {self.date} {self.product} {self.qty}'