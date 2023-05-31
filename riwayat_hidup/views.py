from django.shortcuts import render
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
    prestasi,
)

# Create your views here.
def riwayat_hidup(request):
    aboutSelf = about.objects.first()  # Mendapatkan objek mymodel pertama
    #Pendidikan yang ditempuh
    tahunPendidikanSatu = tahun_pendidikan_satu.objects.first().tahun_pendidikan_1
    sekolahPendidikanSatu = tahun_pendidikan_satu.objects.first().sekolah_pendidikan_1
    tahunPendidikanDua = tahun_pendidikan_dua.objects.first().tahun_pendidikan_2
    sekolahPendidikanDua = tahun_pendidikan_dua.objects.first().sekolah_pendidikan_2
    tahunPendidikanTiga = tahun_pendidikan_tiga.objects.first().tahun_pendidikan_3
    sekolahPendidikanTiga = tahun_pendidikan_tiga.objects.first().sekolah_pendidikan_3
    tahunPendidikanEmpat = tahun_pendidikan_empat.objects.first().tahun_pendidikan_4
    sekolahPendidikanEmpat = tahun_pendidikan_empat.objects.first().sekolah_pendidikan_4

    #RIWAYAT PEKERJAAN#
    pekerjaanTahunPertama = ''
    pekerjaanPertama = ''
    obj_pekerjaan_Pertama = pekerjaan_pertama.objects.first()
    if obj_pekerjaan_Pertama:
        pekerjaanTahunPertama = obj_pekerjaan_Pertama.pekerjaan_tahun_1
        pekerjaanPertama = obj_pekerjaan_Pertama.pekerjaan_1
    #####
    pekerjaanTahunKedua = ''
    pekerjaanKedua = ''
    obj_pekerjaan_Kedua = pekerjaan_kedua.objects.first()
    if obj_pekerjaan_Kedua:
        pekerjaanTahunKedua = obj_pekerjaan_Kedua.pekerjaan_tahun_2
        pekerjaanKedua = obj_pekerjaan_Kedua.pekerjaan_2
    #####
    pekerjaanTahunKetiga = ''
    pekerjaanKetiga = ''
    obj_pekerjaan_Ketiga = pekerjaan_ketiga.objects.first()
    if obj_pekerjaan_Ketiga:
        pekerjaanTahunKetiga = obj_pekerjaan_Ketiga.pekerjaan_tahun_3
        pekerjaanKetiga = obj_pekerjaan_Ketiga.pekerjaan_3
    #####
    pekerjaanTahunKeempat = ''
    pekerjaanKeempat = ''
    obj_pekerjaan_keempat = pekerjaan_keempat.objects.first()
    if obj_pekerjaan_keempat:
        pekerjaanTahunKeempat = obj_pekerjaan_keempat.pekerjaan_tahun_4
        pekerjaanKeempat = obj_pekerjaan_keempat.pekerjaan_4
    #####
    #kontak
    no = kontak.objects.first().nomor
    email = kontak.objects.first().email
    #####
    prestasiPertama = ''
    obj_prestasi_pertama = prestasi.objects.first()
    if obj_prestasi_pertama:
        prestasiPertama = obj_prestasi_pertama.prestasi_1
    #####
    prestasiKedua = ''
    obj_prestasi_pertama = prestasi.objects.first()
    if obj_prestasi_pertama:
        prestasiKedua = obj_prestasi_pertama.prestasi_2
    #####
    prestasiKetiga = ''
    obj_prestasi_pertama = prestasi.objects.first()
    if obj_prestasi_pertama:
        prestasiKetiga = obj_prestasi_pertama.prestasi_3
    #####
    prestasiKeempat = ''
    obj_prestasi_pertama = prestasi.objects.first()
    if obj_prestasi_pertama:
        prestasiKeempat = obj_prestasi_pertama.prestasi_4
    #####
    prestasiKelima = ''
    obj_prestasi_pertama = prestasi.objects.first()
    if obj_prestasi_pertama:
        prestasiKelima = obj_prestasi_pertama.prestasi_5
    #####
    prestasiKeenam = ''
    obj_prestasi_pertama = prestasi.objects.first()
    if obj_prestasi_pertama:
        prestasiKeenam = obj_prestasi_pertama.prestasi_6
    #####
    prestasiKetujuh = ''
    obj_prestasi_pertama = prestasi.objects.first()
    if obj_prestasi_pertama:
        prestasiKetujuh = obj_prestasi_pertama.prestasi_7
    #####
    prestasiKedelapan = ''
    obj_prestasi_pertama = prestasi.objects.first()
    if obj_prestasi_pertama:
        prestasiKedelapan = obj_prestasi_pertama.prestasi_8
    #####
    prestasiKesembilan = ''
    obj_prestasi_pertama = prestasi.objects.first()
    if obj_prestasi_pertama:
        prestasiKesembilan = obj_prestasi_pertama.prestasi_9
    #####
    prestasiKesepuluh = ''
    obj_prestasi_pertama = prestasi.objects.first()
    if obj_prestasi_pertama:
        prestasiKesepuluh = obj_prestasi_pertama.prestasi_10
    #####
    context = {
        'about': aboutSelf,
        #Pendidikan yang ditempuh 
        'tahunPendidikanSatu': tahunPendidikanSatu,
        'sekolahPendidikanSatu': sekolahPendidikanSatu,
        'tahunPendidikanDua' : tahunPendidikanDua,
        'sekolahPendidikanDua': sekolahPendidikanDua,
        'tahunPendidikanTiga' : tahunPendidikanTiga,
        'sekolahPendidikanTiga': sekolahPendidikanTiga,
        'tahunPendidikanEmpat' : tahunPendidikanEmpat,
        'sekolahPendidikanEmpat': sekolahPendidikanEmpat,
        #Riwayat Pekerjaan
        'pekerjaanTahunPertama' : pekerjaanTahunPertama,
        'pekerjaanPertama' : pekerjaanPertama,
        'pekerjaanTahunKedua' : pekerjaanTahunKedua,
        'pekerjaanKedua' : pekerjaanKedua,
        'pekerjaanTahunKetiga' : pekerjaanTahunKetiga,
        'pekerjaanKetiga' : pekerjaanKetiga,
        'pekerjaanTahunKeempat' : pekerjaanTahunKeempat,
        'pekerjaanKeempat' : pekerjaanKeempat,
        #kontak
        'noHp' : no,
        'email' : email,
        #prestasi
        'prestasiPertama' : prestasiPertama,
        'prestasiKedua' : prestasiKedua,
        'prestasiKetiga' : prestasiKetiga,
        'prestasiKeempat' : prestasiKeempat,
        'prestasiKelima' : prestasiKelima,
        'prestasiKeenam' : prestasiKeenam,
        'prestasiKetujuh' : prestasiKetujuh,
        'prestasiKedelapan' : prestasiKedelapan,
        'prestasiKesembilan' : prestasiKesembilan,
        'prestasiKesepuluh' : prestasiKesepuluh,
    }

    return render(request, 'riwayat_hidup.html', context)