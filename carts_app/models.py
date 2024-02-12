from django.db import models
from user_app.models import User
from catalog_app.models import Product


class BasketQuerySet(models.QuerySet):
    def total_quantity(self):
        return sum(item.quantity for item in self)

    def total_sum(self):
        return sum(item.sum() for item in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    sauce = models.CharField(max_length=350, verbose_name='Соус для запеченных роллов', null=True, blank=True)
    description = models.CharField(max_length=350, verbose_name='Комментарий', null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ['id']

    def __str__(self):
        return f'Корзина: {self.user.username} | Продукт: {self.product.name}'

    def sum(self):
        return round(self.product.sell_price() * self.quantity, 2)
