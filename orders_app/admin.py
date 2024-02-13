from django.contrib import admin
from orders_app.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', ]
    fields = ['id', 'status', 'created_at', 'updated_at', 'customer',
              ('first_name', 'last_name', 'email', 'address', 'phone',),
              'delivery_method', 'basket_history']

    readonly_fields = ['id', 'created_at', 'updated_at', 'customer', 'basket_history']
