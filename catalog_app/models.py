from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название категории')
    image = models.ImageField(upload_to='media/category_images', blank=True, null=True, verbose_name='Изображение')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Категория:{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, default='Описание отсутствует', verbose_name='Описание')
    image = models.ImageField(upload_to='media/product_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=3, decimal_places=2, verbose_name='Скидка в процентах')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['id']

    def __str__(self):
        return f'Продукт: {self.name}'

    def display_id(self):
        return f'ID: {self.id:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - (self.price * self.discount / 100), 2)
        return self.price
