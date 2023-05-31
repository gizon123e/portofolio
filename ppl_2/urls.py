from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('ppl_2/', views.ppl_2,name='ppl_2'),
]