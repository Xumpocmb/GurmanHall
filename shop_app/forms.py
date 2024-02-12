from shop_app.models import ContactMessages
from django import forms


class ContactMessagesForm(forms.ModelForm):
    class Meta:
        model = ContactMessages
        fields = ['name', 'email', 'phone', 'message']

    name = forms.CharField(max_length=25, required=True)
    phone = forms.CharField(max_length=12, required=True)
    email = forms.EmailField(required=True)
    message = forms.Textarea()


