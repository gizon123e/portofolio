from django.db import models

# Create your models here.
class materi(models.Model):
    materi = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.materi[:50]

class subMateri(models.Model):
    subMateri_1 = models.TextField(default='', null=True, blank=True)
    subMateri_2 = models.TextField(default='', null=True, blank=True)


class text_materi_pertama (models.Model):
    text_materi_1 = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.text_materi_1[:50]
    
class text_materi_kedua(models.Model):
    text_materi_2 = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.text_materi_2[:50]
    
class text_materi_ketiga(models.Model):
    text_materi_3 = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.text_materi_3[:50]
    
class gambar_pertama(models.Model):
    gambar_1 = models.ImageField(upload_to='images/')
    caption = "Klik Untuk Mengubah Gambar"

    def __str__(self):
        return self.caption

class gambar_kedua(models.Model):
    gambar_2 = models.ImageField(upload_to='images/')
    caption = "Klik Untuk Mengubah Gambar"

    def __str__(self):
        return self.caption