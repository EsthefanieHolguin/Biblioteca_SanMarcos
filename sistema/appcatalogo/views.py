from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def catalogo(request):
    return HttpResponse("<h1>Catalogo</h1>")
def listado(request):
    return render(request, 'paginas/listado.html')
