from django.db import models
from user_app.models import User


class Order(models.Model):
    CREATED = 0
    CONFIRMED = 1
    PROCESSING = 2
    READY = 3
    ON_WAY = 4
    DELIVERED = 5
    STATUSES = (
        (CREATED, 'Создан'),
        (CONFIRMED, 'Подтвержден'),
        (PROCESSING, 'В обработке'),
        (READY, 'Готов'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Выдан'),
    )

    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=255, null=False, blank=False)
    basket_history = models.JSONField(default=dict)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    delivery_method = models.CharField(max_length=255, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ № {self.id} от {self.created_at}, статус: {self.get_status_display()}'

