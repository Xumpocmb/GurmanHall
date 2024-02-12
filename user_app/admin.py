from django.contrib import admin
from user_app.models import User, EmailVerification


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    search_fields = ['name', 'username', 'email']


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'created']
    readonly_fields = ['created']
    search_fields = ['user__username', 'user__email']
