from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('projek_k_1/', views.projek_k_1,name='projek_k_1'),
]