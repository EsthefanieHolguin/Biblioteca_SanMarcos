from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from django.db.models import Q
from .models import Libro
from .forms import LibroForm

# Acá creamos las funciones para acceder a las vistas HTML

def inicio(request):
    """
    Renderiza la página de inicio.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: La respuesta HTTP renderizada para la página de inicio.
    """

    return render(request, 'paginas/inicio.html')

def nosotros(request):
    """
    Renderiza la página "Nosotros".

    Args:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: La respuesta HTTP renderizada para la página "Nosotros".
    """

    return render(request, 'paginas/nosotros.html')

def catalogo(request):
    """
    Lista libros y muestra una barra de búsqueda en el catálogo.
    Para usuarios que reservan libros.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: La respuesta HTTP renderizada para la página del catálogo.
    """

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

    return render(request, 'paginas/catalogo.html', {'libros': libros})


@login_required
def libros(request): 
    """
    Lista libros y muestra una barra de búsqueda para bibliotecarios.
    También realiza la paginación de los resultados.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: La respuesta HTTP renderizada para la página de listado de libros.
    """

    busqueda = request.GET.get("buscar")
    libros = Libro.objects.all()

    # Ordena los libros por título
    libros = libros.order_by('titulo')

    #querys con la busqueda, que se obtiene del input name del index.html
    if busqueda:
        libros = Libro.objects.filter(
            Q(titulo__icontains = busqueda) |
            Q(autor__icontains = busqueda) |
            Q(isbn = busqueda) |
            Q(categoria__icontains = busqueda)
        ).distinct()

    # Configuración de la paginación
    paginator = Paginator(libros, 10)  # Muestra 10 libros por página
    page = request.GET.get('page')

    try:
        libros_paginados = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un número entero, entrega la primera página.
        libros_paginados = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango (por encima de la última), entrega la última página.
        libros_paginados = paginator.page(paginator.num_pages)

    return render(request, 'libros/index.html', {'libros': libros_paginados})

def crear(request):
    """
    Crea un nuevo libro y redirige a la página de listado de libros.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: La respuesta HTTP redirigida a la página de listado de libros.
    """

    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request,isbn):
    """
    Edita un libro existente y redirige a la página de listado de libros.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.
        isbn (str): El ISBN del libro a editar.

    Returns:
        HttpResponse: La respuesta HTTP redirigida a la página de listado de libros.
    """

    libro = Libro.objects.get(isbn=isbn)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario':formulario})

def eliminar(request, isbn):
    """
    Elimina un libro existente y redirige a la página de listado de libros.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.
        isbn (str): El ISBN del libro a eliminar.

    Returns:
        HttpResponse: La respuesta HTTP redirigida a la página de listado de libros.
    """

    libro = Libro.objects.get(isbn=isbn)
    libro.delete()
    return redirect('libros')

def subir_csv(request):
    """
    Sube un archivo CSV con información de libros y actualiza la base de datos.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: La respuesta HTTP redirigida a la página de listado de libros.
    """

    template_name = "libros/upload_csv.html"

    if request.method == "POST":
        csv_file = request.FILES["csv_file"]

        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")

        # Omitir la primera línea (cabecera)
        header_skipped = False

        for line in lines:

            # Omitir la primera línea (cabecera)
            if not header_skipped:
                header_skipped = True
                continue

            fields = line.split(",")
            if len(fields)>1:
                data_dict = {}
                data_dict ["isbn"] = fields[0]
                data_dict ["titulo"] = fields[1]
                data_dict ["autor"] = fields[2]
                data_dict ["categoria"] = fields[3]
                data_dict ["ubicacion"] = fields[4]
                data_dict ["ejemplares_totales"] = fields[5]
                data_dict ["ejemplares_disponibles"] = fields[6]
                data_dict ["ejemplares_prestados"] = fields[7]
                data_dict ["ejemplares_reservados"] = fields[8]
                data_dict ["descripcion"] = fields[9]

                try:
                    form = LibroForm(data_dict)
                    if form.is_valid():
                        form.save()
                    else:
                        print (form.errors.as_json(),data_dict["titulo"])
                except Exception as ex:
                    print(repr(ex))
        return redirect('libros')

    return render(request,template_name,{})

def exit(request):
    """
    Cierra la sesión del usuario y redirige a la página de inicio.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: La respuesta HTTP redirigida a la página de inicio.
    """
    
    logout(request)
    return redirect('inicio')
