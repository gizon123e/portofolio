from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('teknologi/', views.teknologi,name='teknologi'),
]