from django.contrib import admin
from .models import (
    about, 
    tahun_pendidikan_satu, 
    tahun_pendidikan_dua, 
    tahun_pendidikan_tiga, 
    tahun_pendidikan_empat,
    pekerjaan_pertama, 
    pekerjaan_kedua, 
    pekerjaan_ketiga, 
    pekerjaan_keempat,
    kontak,
    prestasi
)


# Register your models here.
admin.site.register(about)
#Pendidikan yang ditempuh
admin.site.register(tahun_pendidikan_satu)
admin.site.register(tahun_pendidikan_dua)
admin.site.register(tahun_pendidikan_tiga)
admin.site.register(tahun_pendidikan_empat)

#Riwayat Pekerjaan
admin.site.register(pekerjaan_pertama)
admin.site.register(pekerjaan_kedua)
admin.site.register(pekerjaan_ketiga)
admin.site.register(pekerjaan_keempat)

#kontak
admin.site.register(kontak)
#prestasi
admin.site.register(prestasi)