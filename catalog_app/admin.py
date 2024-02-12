from django.contrib import admin

from catalog_app.models import Category, Product, Basket


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'price', 'discount', 'category'
    ]
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name', 'description']
    list_filter = ['category']
    readonly_fields = ['created_at']


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    model = Basket
    fields = ('product', 'quantity', 'sauce', 'description', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 1
