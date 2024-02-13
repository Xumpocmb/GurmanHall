from django.urls import path
from user_app.views import register, login, logout, profile, email_verification

app_name = 'user_app'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('email_verification/<str:email>/<uuid:code>/', email_verification, name='email_verification'),
]
