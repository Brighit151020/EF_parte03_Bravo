from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, redirect, get_object_or_404
from miapp.models import Pais
from miapp.models import Editorial
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


def editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, 'editoriales.html', {'editoriales': editoriales})

def crear_editorial(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        url = request.POST['url']
        imagen = request.FILES.get('imagen')
        estado = True if request.POST.get('estado', False) else False

        Editorial.objects.create(nombre=nombre, url=url, imagen=imagen, estado=estado)
        messages.success(request, 'La editorial se registró correctamente.')
        return redirect('editoriales')

    return render(request, 'crear_editorial.html')

def eliminar_editorial(request, id_editorial):
    editorial = Editorial.objects.get(pk=id_editorial)
    editorial.delete()
    messages.success(request, 'La editorial se eliminó correctamente.')
    return redirect('editoriales')