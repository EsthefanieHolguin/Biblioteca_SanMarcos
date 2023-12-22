from django.urls import path
from .import views

from django.conf import settings

from django.contrib.staticfiles.urls import static
from django.conf.urls.static import static


# Definición de patrones de URL para las vistas en el archivo views.py
urlpatterns = [
    path('', views.inicio, name='inicio'), # Página de inicio
    path('nosotros', views.nosotros, name='nosotros'), # Página "Nosotros"
    path('libros', views.libros, name='libros'), # Vista para listar libros
    path('libros/crear', views.crear, name='crear'), # Vista para crear un nuevo libro
    path('libros/editar', views.editar, name='editar'), # Vista para editar libros (URL sin ISBN específico)
    path('eliminar/<int:isbn>', views.eliminar, name='eliminar'), # Vista para eliminar un libro
    path('libros/editar/<int:isbn>', views.editar, name='editar'), # Vista para editar un libro específico (con ISBN)
    path('csv/upload', views.subir_csv, name='subir_csv'), # Vista para subir datos desde un archivo CSV
    path('catalogo', views.catalogo, name='catalogo'), # Vista para el catálogo
    path('logout/', views.exit, name='exit'), # Vista para cerrar sesión



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)