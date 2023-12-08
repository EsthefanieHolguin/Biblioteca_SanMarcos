from django.urls import path
from .import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.conf.urls.static import static



urlpatterns = [
    path('prestamos', views.prestamos, name='prestamos'),
    path('prestamos/nuevo_prestamo', views.nuevo_prestamo, name='nuevo_prestamo'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)