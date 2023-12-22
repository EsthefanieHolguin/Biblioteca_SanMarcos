from django.urls import path
from .import views

from django.conf import settings

from django.contrib.staticfiles.urls import static
from django.conf.urls.static import static


#Acá el usuario va a poder entrar y acceder a la vista y se debe colocar la funcion definida en views.py en cada path
urlpatterns = [
    path('usuarios', views.usuarios, name='usuarios'), # Ruta para listar usuarios
    path('usuarios/crear', views.crear, name='crear_usuario'), # Ruta para crear un nuevo usuario
    path('usuarios/editar', views.editar, name='editar_usuario'), # Ruta de la vista para editar un usuario existente
    path('usuarios/eliminar/<int:rut_usuario>', views.eliminar, name='eliminar_usuario'), # Ruta para eliminar un usuario existente entregando RUT
    path('usuarios/editar/<int:rut_usuario>', views.editar, name='editar_usuario'), # Ruta para editar un usuario existente entregando RUT
    path('usuarios/upload', views.subir_usuarios, name='subir_usuarios'), # Ruta para subir datos de usuarios desde un archivo CSV


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)