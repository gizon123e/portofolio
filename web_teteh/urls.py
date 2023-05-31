"""
URL configuration for web_teteh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from kuliah_inti import views
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.urls')),
    path('kuliah_inti/', views.kuliah_inti, name='kuliah_inti'),
    path('kuliah_selektif/', views.kuliah_selektif, name='kuliah_selektif'),
    path('riwayat_hidup/', include('riwayat_hidup.urls')),
    path('', include('filosofi_pendidikan_indonesia.urls')),
    path('', include('pemahaman.urls')),
    path('', include('prinsip_1.urls')),
    path('', include('prinsip_2.urls')),
    path('', include('pembelajaran_sosial.urls')),
    path('', include('projek_k_1.urls')),
    path('', include('projek_k_2.urls')),
    path('', include('ppl_1.urls')),
    path('', include('ppl_2.urls')),
    path('', include('computational.urls')),
    path('', include('design_thinking.urls')),
    path('', include('teknologi.urls')),
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  