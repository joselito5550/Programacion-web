from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import login as auth_login
from django.views.generic import TemplateView, FormView
from jugador_equipo.form import UserForm, EquipoForm
from .models import Perfiles, Equipo
from equipo_jornada.models import Liga, Jornada
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
                return redirect('/')
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
    success_url = reverse_lazy('/')

    def form_valid(self, form):
        user = form.save()
        perfil = Perfiles()
        perfil.usuario = user
        perfil.telefono = form.cleaned_data['telefono']
        perfil.equipo = form.cleaned_data['equipo']
        perfil.save()
        return redirect('/')


class Registrar_equipo(FormView):
    model = Equipo
    template_name = "registrar_equipo.html"
    form_class = EquipoForm
    success_url = reverse_lazy('/')

    def form_valid(self, form):
        equipo = form.save()
        return redirect('/')


def index(request):
    context['todos_equipos'] = Equipo.objects.all()
    if request.user.is_authenticated():
        context['usuario'] = Perfiles.objects.get(usuario=request.user)
        if context['usuario'].equipo:
            context['equipos'] = Equipo.objects.filter(
                Liga=context['usuario'].equipo.Liga)
            context['tiene_equipo'] = True
            context['jugadores'] = Perfiles.objects.filter(
                    equipo=context['usuario'].equipo)
            if request.user == context['usuario'].equipo.administrador:
                context['administrador_equipo'] = True
            else:
                context['administrador_equipo'] = False
                print context['administrador_equipo']
            if context['usuario'].equipo.Liga:
                if request.user == context['usuario'].equipo.Liga.administrador:
                    context['es_administrador_liga'] = True
                else:
                    context['es_administrador_liga'] = False
        else:
            context['equipo'] = "nada"
            context['tiene_equipo'] = False
            context['administrador_equipo'] = False
            context['es_administrador_liga'] = False
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
            return redirect('/')
    else:
        print "not request POST"
        return redirect('/')


def crear_jornadas(request):
    liga = Liga.objects.get(administrador=request.user)
    if liga is not None:
        equipos = Equipo.objects.filter(Liga=liga)
        context['equipos_jornadas'] = equipos
        return render(request, 'crear_jornadas.html', {'context': context})
    else:
        return redirect('/')


def crear_una_jornada(request):
    if request.method == "POST":
        nombre_equipo_1 = request.POST.get('nombre_equipo_1')
        nombre_equipo_2 = request.POST.get('nombre_equipo_2')
        jornada = Jornada()
        jornada.equipo1 = Equipo.objects.get(nombre=nombre_equipo_1)
        jornada.equipo2 = Equipo.objects.get(nombre=nombre_equipo_2)
        jornada.numero = 2
        jornada.fecha = request.POST.get('fecha')
        jornada.Liga = context['usuario'].equipo.Liga
        jornada.save()
        return redirect('/')


def resultado_jornada(request):
    if request.method == "POST":
        jornada = Jornada.objects.get(id=request.POST.get('id_jornada'))
        jornada.goles_primer_equipo = request.POST.get('resultado_equipo1')
        jornada.goles_segundo_equipo = request.POST.get('resultado_equipo2')
        jornada.save()
        equipo1 = Equipo.objects.get(nombre=jornada.equipo1)
        equipo2 = Equipo.objects.get(nombre=jornada.equipo2)
        if jornada.goles_primer_equipo>jornada.goles_segundo_equipo:
            equipo1.puntos = equipo1.puntos+3
            equipo1.save()
            return redirect('/')
        if jornada.goles_primer_equipo<jornada.goles_segundo_equipo:
            equipo2.puntos = equipo2.puntos+3
            equipo2.save()
            return redirect('/')
        if jornada.goles_primer_equipo==jornada.goles_segundo_equipo:
            equipo2.puntos = equipo2.puntos+1
            equipo1.puntos = equipo1.puntos+1
            equipo2.save()
            equipo1.save()
            return redirect('/')
    else:
        context['jornadas'] = Jornada.objects.filter(
            Liga=Liga.objects.get(administrador=request.user))
        return render(request, 'resultado_jornada.html', {'context': context})


def unirte_liga(request):
    if request.method == "POST":
        nombre_liga=request.POST.get('nombre_liga')
        print nombre_liga
        liga = Liga.objects.get(nombre=nombre_liga)
        equipo = Equipo.objects.get(administrador=request.user)
        equipo.Liga = liga
        equipo.save()
        return redirect('/')
