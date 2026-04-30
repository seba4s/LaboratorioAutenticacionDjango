from django.urls import path
from . import views

urlpatterns = [
    # Ruta principal: Listado de calificaciones
    path('', views.listar_calificaciones, name='listar'),
    
    # Ruta para crear un nuevo registro
    path('crear/', views.crear_calificacion, name='crear'),
    
    # Ruta para editar (usa el ID o PK del registro)
    path('editar/<int:pk>/', views.editar_calificacion, name='editar'),
    
    # Ruta para eliminar
    path('eliminar/<int:pk>/', views.eliminar_calificacion, name='eliminar'),
]