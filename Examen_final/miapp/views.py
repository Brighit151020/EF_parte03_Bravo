from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

def index(request):
   
    return render(request,'index.html', {
})

def editoriales(request):
    return render(request,'editoriales.html',{
})

def registrar_pais(request):
    return render(request,'registrar_pais.html',{
})
def crear_editorial(request):
    return render(request,'crear_editorial.html',{
})


