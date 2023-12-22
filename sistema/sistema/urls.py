
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
path('', include('appejemplares.urls')), #Registramos la url raíz de la app libreria
    path('', include('appusuarios.urls')),
    path('', include('appprestamos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
