from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('prinsip_1/', views.prinsip_1,name='prinsip_1'),
]