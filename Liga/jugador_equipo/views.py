from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import login as auth_login
from django.views.generic import TemplateView, FormView
from jugador_equipo.form import UserForm, EquipoForm
from .models import Perfiles, Equipo
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

context = {}
# Create your views here.


def inicio_sesion(request):
    if request.user.is_authenticated():
        context['logueado'] = True
    else:
        context['logueado'] = False
    return render(request, 'login.html', {'context': context})


def login(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(username=usuario, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                context['usuario'] = Perfiles.objects.get(usuario=request.user)
                return render(request, 'principal.html', {'context': context})
        else:
            context['mensaje'] = 'Nombre de usuario y/o password incorrectos.'
            context['tipoMensaje'] = 2
    return render(request, 'login.html', {'context': context})

@login_required
def cerrar(request):
    if request.user.is_authenticated():
        logout(request)
        context['mensaje'] = "Cerrada sesion"
    else:
        context['mensaje'] = "No has iniciado sesion"
    return render(request, 'principal.html', {'context': context})


class Registrarse(FormView):
    template_name = 'registrarse.html'
    form_class = UserForm
    success_url = reverse_lazy('registrarse')

    def form_valid(self, form):
        user = form.save()
        perfil = Perfiles()
        perfil.usuario = user
        perfil.telefono = form.cleaned_data['telefono']
        perfil.equipo = form.cleaned_data['equipo']
        perfil.save()
        return redirect('/index')


class Registrar_equipo(FormView):
    model = Equipo
    template_name = "registrar_equipo.html"
    form_class = EquipoForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        equipo = form.save()
        return redirect('/index')


def index(request):
    context['todos_equipos'] = Equipo.objects.all()
    if request.user.is_authenticated():
        context['usuario'] = Perfiles.objects.get(usuario=request.user)
        if context['usuario'].equipo:
            context['equipos'] = Equipo.objects.filter(
                Liga=context['usuario'].equipo.Liga)
            context['tiene_equipo'] = True
            if request.user == context['usuario'].equipo.administrador:
                context['administrador_equipo'] = True
                context['jugadores'] = Perfiles.objects.filter(
                    equipo=context['usuario'].equipo)
            else:
                context['administrador_equipo'] = False
                print context['administrador_equipo']
        else:
            context['equipo'] = "nada"
            context['tiene_equipo'] = False
    return render(request, 'principal.html', {'context': context})


def ver_equipos(request):
    if Equipo.objects.exists():
        equipos = Equipo.objects.all()
        perfiles = Perfiles.objects.get(usuario=request.user)
        return render(request, 'ver_equipos.html', {'equipos': equipos, 'exists_equipo': True, 'perfiles': perfiles})
    else:
        print "No hay equipos"
        return render(request, 'ver_equipos.html', {'exists_equipo': False})


def unirte_equipo(request):
    if request.method == 'POST':
        nombre_equipo = request.POST.get('nombre_equipo')
        if Equipo.objects.get(nombre=nombre_equipo):
            usuario = Perfiles.objects.get(usuario=request.user)
            usuario.equipo = Equipo.objects.get(nombre=nombre_equipo)
            usuario.save()
            context['usuario'] = usuario
            print "Equipo cambiado"
            return render(request, 'principal.html', {'context': context})
    else:
        print "not request POST"
        return render(request, 'principal.html', {'context': context})
