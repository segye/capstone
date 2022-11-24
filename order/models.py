from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Shoppingcart(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name="사용자")
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name="상품")
    quantity = models.PositiveSmallIntegerField(null=True, default=1, validators=[MinValueValidator(1),
                                                                                  MaxValueValidator(100)],
                                                verbose_name="수량")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="주문시간")

    class Meta:
        ordering = ['id']
        db_table = 'shopping_order'
        verbose_name = '장바구니'
        verbose_name_plural = '장바구니'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name
