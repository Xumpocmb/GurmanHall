from django import forms
from orders_app.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'delivery_method']


class OperatorOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'address', 'phone', 'delivery_method', 'description']

        first_name = forms.CharField()
        address = forms.CharField()
        phone = forms.CharField()
        delivery_method = forms.CharField()
        description = forms.CharField()
