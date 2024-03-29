from django.db import models
from user_app.models import User
from carts_app.models import Basket


class Order(models.Model):
    CREATED = 0
    CONFIRMED = 1
    PROCESSING = 2
    READY = 3
    ON_WAY = 4
    DELIVERED = 5
    CANCELLED = 6

    STATUSES = (
        (CREATED, 'Создан'),
        (CONFIRMED, 'Подтвержден'),
        (PROCESSING, 'В обработке'),
        (READY, 'Готов'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Выдан'),
        (CANCELLED, 'Отменен'),
    )

    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=True)
    address = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=True)
    basket_history = models.JSONField(default=dict)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    delivery_method = models.CharField(max_length=255, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def __str__(self):
        formatted_date = self.created_at.strftime('%d-%m-%Y %H:%M')
        return f'Заказ № {self.id} | {formatted_date} | {self.customer} | {self.get_status_display()}'

    def fill_basket_history(self):
        baskets = Basket.objects.filter(user=self.customer)
        total_sum = float(baskets.total_sum())
        basket_history = {
            'baskets': [basket.de_json() for basket in baskets],
            'total_sum': total_sum
        }
        self.basket_history = basket_history
        baskets.delete()
        self.save()
