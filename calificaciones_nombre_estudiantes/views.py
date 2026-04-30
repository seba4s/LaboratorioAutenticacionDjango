from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from .models import Calificacion
from .forms import CalificacionForm, LoginUsuarioForm, RegistroUsuarioForm


def inicio(request):
    return render(request, 'calificaciones/inicio.html')


def registro_usuario(request):
    if request.user.is_authenticated:
        return redirect('listar')

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listar')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'calificaciones/registro.html', {'form': form})


def login_usuario(request):
    if request.user.is_authenticated:
        return redirect('listar')

    if request.method == 'POST':
        form = LoginUsuarioForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('listar')
    else:
        form = LoginUsuarioForm()

    return render(request, 'calificaciones/login.html', {'form': form})


def logout_usuario(request):
    logout(request)
    return redirect('login_usuario')

# 1. LISTAR y PROMEDIO GENERAL
@login_required(login_url='login_usuario')
def listar_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    # Función agregada para el promedio de todos los registros
    promedio_dict = Calificacion.objects.all().aggregate(Avg('promedio'))
    promedio_general = promedio_dict['promedio__avg']
    
    return render(request, 'calificaciones/listar.html', {
        'calificaciones': calificaciones,
        'promedio_general': promedio_general
    })

# 2. REGISTRAR (Crear)
@login_required(login_url='login_usuario')
def crear_calificacion(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save() # Esto dispara el save() del modelo que calcula el promedio
            return redirect('listar')
    else:
        form = CalificacionForm()
    return render(request, 'calificaciones/crear.html', {'form': form})

# 3. EDITAR (Actualizar)[cite: 1]
@login_required(login_url='login_usuario')
def editar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, 'calificaciones/editar.html', {'form': form})

# 4. ELIMINAR (Delete)[cite: 1]
@login_required(login_url='login_usuario')
def eliminar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        calificacion.delete()
        return redirect('listar')
    return render(request, 'calificaciones/eliminar.html', {'calificacion': calificacion})