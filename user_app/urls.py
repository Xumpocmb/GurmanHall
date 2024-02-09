from django.urls import path
from user_app.views import register, login, logout, profile

app_name = 'user_app'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
]
