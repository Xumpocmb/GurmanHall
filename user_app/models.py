from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', verbose_name='Изображение', null=True, blank=True)
    phone = models.CharField(max_length=9, verbose_name='Телефон', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации', null=True, blank=True)
    last_login = models.DateTimeField(auto_now=True, verbose_name='Последний вход', null=True, blank=True)
    verified_email = models.BooleanField(default=False, verbose_name='Подтвержденная почта', null=True, blank=True)
    is_archived = models.BooleanField(default=False, verbose_name='Архивирован', null=True, blank=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    def __str__(self):
        return self.username

    def display_id(self):
        return f'ID: {self.id:05}'
