from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('pembelajaran_sosial/', views.pembelajaran_sosial,name='pembelajaran_sosial'),
]