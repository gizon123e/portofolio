from django.shortcuts import render

# Create your views here.
def kuliah_inti (request):
    return render(request, 'kuliah_inti.html')

def kuliah_selektif (request):
    return render(request, 'kuliah_selektif_dan_efektif.html')