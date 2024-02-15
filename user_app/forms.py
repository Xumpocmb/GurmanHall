import uuid
from datetime import timedelta

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.utils.timezone import now

from user_app.models import User, EmailVerification


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2']

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        expiration = now() + timedelta(hours=48)
        record = EmailVerification.objects.create(user=user, code=uuid.uuid4(), expired=expiration)
        record.send_verification_email()
        return user


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['image', 'first_name', 'last_name', 'address', 'phone']

    image = forms.ImageField(required=False)

    first_name = forms.CharField()
    last_name = forms.CharField()

    address = forms.CharField()
    phone = forms.CharField()


class EmailChangeForm(UserChangeForm):
    email = forms.EmailField(label="Новый email", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email']
