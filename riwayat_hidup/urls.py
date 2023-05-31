from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.riwayat_hidup,name="riwayat_hidup"),
]