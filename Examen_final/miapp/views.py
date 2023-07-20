from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, redirect, get_object_or_404
from miapp.models import Pais
from django.contrib import messages


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
def inicio(request):
    return render(request,'layout.html',{
    })



def paises(request):
    paises = Pais.objects.all()
    return render(request, 'paises.html', {'paises': paises})

def registrar_pais(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        poblacion = request.POST['poblacion']
        estado = True if request.POST.get('estado') else False

        Pais.objects.create(codigo=codigo, nombre=nombre, poblacion=poblacion, estado=estado)
        messages.success(request, 'El país se registró correctamente.')

    return render(request, 'registrar_pais.html')

def eliminar_pais(request, id_pais):
    pais = Pais.objects.get(pk=id_pais)
    pais.delete()
    messages.success(request, 'El país se eliminó correctamente.')
    return redirect('paises')