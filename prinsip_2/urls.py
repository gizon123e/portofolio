from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('prinsip_2/', views.prinsip_2,name='prinsip_2'),
]