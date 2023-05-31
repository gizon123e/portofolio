from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('desing_thinking/', views.design_thinking,name='design_thinking'),
]