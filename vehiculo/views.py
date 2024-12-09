from django.shortcuts import render, redirect

# Create your views here.
from .forms import Add
from .models import Vehiculo
from django.contrib.auth.decorators import permission_required

def index(request):
    return render(
        request,
        'index.html'
    )

@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def add(request):
    if request.method == 'POST':
        formulario = Add(request.POST)
        if formulario.is_valid():
            marca = formulario.cleaned_data['marca']
            modelo = formulario.cleaned_data['modelo']
            carroceria = formulario.cleaned_data['carroceria']
            motor = formulario.cleaned_data['motor']
            categoria = formulario.cleaned_data['categoria']
            precio = formulario.cleaned_data['precio']
            formulario.save()
            return redirect('guardado')
    else:
        formulario = Add()
    return render(request, 'add.html', {'formulario': formulario})

def guardado(request):
    return render(
        request,
        'guardado.html'
    )

@permission_required('vehiculo.visualizar_catalogo', raise_exception = True)
def listar(request):
    vehiculos = Vehiculo.objects.all()
    return render(
        request,
        'listar.html',
        {'vehiculos': vehiculos}
    )

# Registro
from .forms import RegistroUsuario
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

def registro(request):
    if request.method == 'POST':
        formulario = RegistroUsuario(request.POST)
        if formulario.is_valid():
            usuario = formulario.save(commit=False)
            usuario.set_password(formulario.cleaned_data['password'])
            usuario.save()

            # Permiso de visualización automatico
            content_type = ContentType.objects.get(app_label='vehiculo', model='vehiculo')
            permiso = Permission.objects.get(codename='visualizar_catalogo', content_type=content_type)
            usuario.user_permissions.add(permiso)

            return redirect('login')
    else:
        formulario = RegistroUsuario()
    return render(request, 'registro.html', {'formulario': formulario})