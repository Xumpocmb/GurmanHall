from django.contrib import admin
from carts_app.models import Basket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    model = Basket
    fields = ['product', 'quantity', 'sauce', 'description', 'created_timestamp']
    readonly_fields = ['created_timestamp']
    extra = 1
