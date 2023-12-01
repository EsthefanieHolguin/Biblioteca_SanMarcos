from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Libro
from .forms import LibroForm

# Acá creamos las funciones para acceder a las vistas HTML

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):  #Listar libros y barra busqueda
    busqueda = request.GET.get("buscar")
    libros = Libro.objects.all()

    #querys con la busqueda, que se obtiene del input name del index.html
    if busqueda:
        libros = Libro.objects.filter(
            Q(titulo__icontains = busqueda) |
            Q(autor__icontains = busqueda) |
            Q(isbn = busqueda) |
            Q(categoria__icontains = busqueda)
        ).distinct()

    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})
def editar(request,id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario':formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')