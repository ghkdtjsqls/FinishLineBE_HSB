from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.main),
    path('', views.csrf_token_view, name='token'),
]