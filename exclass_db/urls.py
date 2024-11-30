from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.main),
    path('', views.every_crawl, name=''),
]