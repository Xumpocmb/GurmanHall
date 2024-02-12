from django.contrib import admin

from catalog_app.models import Category, Product


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
