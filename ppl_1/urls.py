from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('ppl_1/', views.ppl_1,name='ppl_1'),
]