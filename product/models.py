from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="상품명")
    price = models.IntegerField(verbose_name="상품가격")
    description = models.TextField(verbose_name="상품설명")
    image = models.ImageField(blank=True, upload_to='')
    stock = models.IntegerField(verbose_name="상품재고")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="상품등록시간")
    category = models.CharField(max_length=30, verbose_name="카테고리")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        db_table = 'shopping_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'
