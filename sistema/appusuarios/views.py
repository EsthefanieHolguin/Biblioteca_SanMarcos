from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Usuario
from .forms import UsuarioForm
from appejemplares import views


# Create your views here.
def usuarios(request):  #Listar usuarios y barra busqueda
    busqueda = request.GET.get("buscar_usuario")
    usuarios = Usuario.objects.all()

    #querys con la busqueda, que se obtiene del input name del index.html
    if busqueda:
        usuarios = Usuario.objects.filter(
            Q(rut = busqueda) |
            Q(nombre_usuario__icontains = busqueda) |
            Q(email__icontains = busqueda)
        ).distinct()

    return render(request, 'usuarios/index.html', {'usuarios': usuarios})

def crear(request):
    formulario = UsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/crear.html', {'formulario': formulario})
def editar(request,id):
    usuario = Usuario.objects.get(id=id)
    formulario = UsuarioForm(request.POST or None, request.FILES or None, instance=usuario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/editar.html', {'formulario':formulario})

def eliminar(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('usuarios')