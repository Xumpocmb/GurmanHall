from django import forms
from orders_app.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'delivery_method']
        widgets = {
            'delivery_method': forms.RadioSelect(choices=(
                ('self_pickup', 'Самовывоз'),
                ('courier', 'Курьер'),
            )),
        }


