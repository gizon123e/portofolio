from django.db import models

# Create your models here.
class about(models.Model):
    about_my_self = models.TextField(default='')

    def __str__(self):
        return self.about_my_self[:50]  # Menampilkan 50 karakter pertama dari my_text


#Pendidikan yang ditempuh

class tahun_pendidikan_satu(models.Model):
    tahun_pendidikan_1 = models.TextField(default='')
    sekolah_pendidikan_1 = models.TextField(default='')

    def __str__(self):
        return f"{self.sekolah_pendidikan_1[:50]}, {self.tahun_pendidikan_1[:50]}"

class tahun_pendidikan_dua(models.Model):
    tahun_pendidikan_2 = models.TextField(default='')
    sekolah_pendidikan_2 = models.TextField(default='')

    def __str__(self):
        return f"{self.sekolah_pendidikan_2[:50]}, {self.tahun_pendidikan_2[:50]}"
    
class tahun_pendidikan_tiga(models.Model):
    tahun_pendidikan_3 = models.TextField(default='')
    sekolah_pendidikan_3 = models.TextField(default='')

    def __str__(self):
        return f"{self.sekolah_pendidikan_3[:50]}, {self.tahun_pendidikan_3[:50]}"
    
class tahun_pendidikan_empat(models.Model):
    tahun_pendidikan_4 = models.TextField(default='')
    sekolah_pendidikan_4 = models.TextField(default='')

    def __str__(self):
        return f"{self.sekolah_pendidikan_4[:50]}, {self.tahun_pendidikan_4[:50]}"
#Riwayat Pekerjaan    
class pekerjaan_pertama(models.Model):
    pekerjaan_tahun_1 = models.TextField(default='')
    pekerjaan_1 = models.TextField(default='')
    def __str__(self):
        return f"{self.pekerjaan_tahun_1[:50]}, {self.pekerjaan_1[:50]}"

class pekerjaan_kedua(models.Model):
    pekerjaan_tahun_2 = models.TextField(default='')
    pekerjaan_2 = models.TextField(default='')   

    def __str__(self):
        return f"{self.pekerjaan_tahun_2[:50]}, {self.pekerjaan_2[:50]}"

class pekerjaan_ketiga(models.Model):
    pekerjaan_tahun_3 = models.TextField(default='')
    pekerjaan_3 = models.TextField(default='')

    def __str__(self):
        return f"{self.pekerjaan_tahun_3[:50]}, {self.pekerjaan_3[:50]}"

class pekerjaan_keempat(models.Model):
    pekerjaan_tahun_4 = models.TextField(default='')
    pekerjaan_4 = models.TextField(default='')

    def __str__(self):
        return f"{self.pekerjaan_tahun_4[:50]}, {self.pekerjaan_4[:50]}"

#Kontak
class kontak(models.Model):
    nomor = models.TextField(default='')
    email = models.TextField(default='')

    def __str__(self):
        return f"{self.nomor[:50]}, {self.email[:50]}"
    
#PRESTASI#
class prestasi(models.Model):
    prestasi_1 = models.TextField(default='', null=True, blank=True)
    prestasi_2 = models.TextField(default='', null=True, blank=True)
    prestasi_3 = models.TextField(default='', null=True, blank=True)
    prestasi_4 = models.TextField(default='', null=True, blank=True)
    prestasi_5 = models.TextField(default='', null=True, blank=True)
    prestasi_6 = models.TextField(default='', null=True, blank=True)
    prestasi_7 = models.TextField(default='', null=True, blank=True)
    prestasi_8 = models.TextField(default='', null=True, blank=True)
    prestasi_9 = models.TextField(default='', null=True, blank=True)
    prestasi_10 = models.TextField(default='', null=True, blank=True)