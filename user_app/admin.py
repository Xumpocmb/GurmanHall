from django.contrib import admin
from user_app.models import User


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    search_fields = ['name', 'username', 'email']

