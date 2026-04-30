from django.contrib import admin
from django.urls import path, include # Importamos include
from calificaciones_nombre_estudiantes import views as calificaciones_views

urlpatterns = [
    path('', calificaciones_views.inicio, name='inicio'),
    path('calificaciones/', include('calificaciones_nombre_estudiantes.urls')),
    path('admin/', admin.site.urls),
]