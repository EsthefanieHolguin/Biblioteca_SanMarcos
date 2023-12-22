from django.urls import path
from .import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.conf.urls.static import static



urlpatterns = [
    path('prestamos', views.prestamos, name='prestamos'), # Ruta para mostrar la lista de préstamos
    path('prestamos/nuevo_prestamo', views.nuevo_prestamo, name='nuevo_prestamo'), # Ruta para la creación de un nuevo préstamo
    path('prestamos/editar_prestamo/<int:id_prestamo>', views.editar_prestamo, name='editar_prestamo'), # Ruta para la edición de un préstamo existente
    path('prestamos/eliminar_prestamo/<int:id_prestamo>', views.eliminar_prestamo, name='eliminar_prestamo'), # Ruta para eliminar un préstamo existente

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)