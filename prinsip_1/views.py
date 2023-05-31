from django.shortcuts import render, get_object_or_404
from .models import(
    materi,
    subMateri,
    text_materi_pertama,
    text_materi_kedua,
    text_materi_ketiga,
    gambar_pertama,
    gambar_kedua,
)
# Create your views here.
def prinsip_1(request):
    judul_materi = materi.objects.first().materi
    text_materi_1 = text_materi_pertama.objects.first().text_materi_1
    text_materi_2 = text_materi_kedua.objects.first().text_materi_2
    text_materi_3 = text_materi_ketiga.objects.first().text_materi_3
    sub_materi_1 = subMateri.objects.first().subMateri_1
    sub_materi_2 = subMateri.objects.first().subMateri_2
    gambar_1 = get_object_or_404(gambar_pertama).gambar_1
    gambar_2 = get_object_or_404(gambar_kedua).gambar_2
    
    context = {
        'judul_materi': judul_materi,
        'text_materi_1': text_materi_1,
        'text_materi_2': text_materi_2,
        'text_materi_3': text_materi_3,
        'sub_materi_1': sub_materi_1,
        'sub_materi_2': sub_materi_2,
        'gambar_1' : gambar_1,
        'gambar_2' : gambar_2,
    }
    
    return render(request, 'artikel.html', context)