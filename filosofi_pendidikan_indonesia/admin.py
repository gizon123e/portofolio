from django.contrib import admin
from .models import (
    materi,
    subMateri,
    text_materi_pertama,
    text_materi_kedua,
    text_materi_ketiga,
    gambar_pertama,
    gambar_kedua
)
# Register your models here.
admin.site.register(materi)
admin.site.register(subMateri)
admin.site.register(text_materi_pertama)
admin.site.register(text_materi_kedua)
admin.site.register(text_materi_ketiga)
admin.site.register(gambar_pertama)
admin.site.register(gambar_kedua)