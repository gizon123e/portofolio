from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('projek_k_2/', views.projek_k_2,name='projek_k_2'),
]