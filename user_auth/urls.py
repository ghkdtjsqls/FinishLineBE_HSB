# user_auth/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('user_signup/', views.user_signup, name='signup'),
    path('login/', views.login_view, name='login'),
]