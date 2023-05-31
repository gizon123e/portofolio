from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.kuliah_inti, name="kuliah_inti"),
    path('', views.kuliah_selektif, name="kuliah_selektif"),
]