from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Usuario
from .forms import UsuarioForm



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
    usuario = Usuario.objects.get(id_usuario=id)
    formulario = UsuarioForm(request.POST or None, request.FILES or None, instance=usuario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/editar.html', {'formulario':formulario})

def eliminar(request, id):
    usuario = Usuario.objects.get(id_usuario=id)
    usuario.delete()
    return redirect('usuarios')

def subir_usuarios(request):
    template_name = "usuarios/upload_user.html"

    if request.method == "POST":
        csv_usuarios = request.FILES["csv_usuarios"]

        file_data = csv_usuarios.read().decode("utf-8")
        lines = file_data.split("\n")
        for line in lines:
            fields = line.split(",")
            if len(fields)>1:
                data_dict = {}
                data_dict ["rut"] = fields[1]
                data_dict ["nombre_usuario"] = fields[2]
                data_dict ["email"] = fields[3]
                data_dict ["curso"] = fields[4]

                try:
                    form = UsuarioForm(data_dict)
                    if form.is_valid():
                        form.save()
                    else:
                        print (form.errors.as_json(),data_dict["nombre_usuario"])
                except Exception as ex:
                    print(repr(ex))
        return redirect('usuarios')

    return render(request,template_name,{})