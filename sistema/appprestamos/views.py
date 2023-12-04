from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Prestamo
from .forms import PrestamoForm
from django.contrib.auth.forms import AuthenticationForm
from appejemplares.models import Libro
from appejemplares import views
from appusuarios.models import Usuario


# Create your views here.
def prestamos(request):

    busqueda_prestamo = request.GET.get("buscar_prestamo")
    prestamos = Prestamo.objects.all()

    if busqueda_prestamo:
        prestamos = Prestamo.objects.filter(
            Q(id = busqueda_prestamo) |
            Q(usuario = busqueda_prestamo) |
            Q(fecha_prestamo = busqueda_prestamo)|
            Q(libro = busqueda_prestamo)
        ).distinct()
    return render(request, 'prestamos/index.html', {'prestamos': prestamos})

def nuevo_prestamo(request):
    formulario = PrestamoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('prestamos')
    return render(request, 'prestamos/nuevo_prestamo.html', {'formulario': formulario})

def editar_prestamo(request,id):
    prestamo = prestamo.objects.get(id=id)
    formulario = PrestamoForm(request.POST or None, request.FILES or None, instance=prestamo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('prestamos')
    return render(request, 'prestamos/editar_prestamo.html', {'formulario':formulario})

def eliminar_prestamo(request, id):
    prestamo = Prestamo.objects.get(id=id)
    prestamo.delete()
    return redirect('prestamos')