from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def Pendidikan(request):   
    return render(request, 'Pendidikan.html')

def Pengalaman(request):   
    return render(request, 'Pengalaman.html')

def Keahlian(request):   
    return render(request, 'Keahlian.html')


