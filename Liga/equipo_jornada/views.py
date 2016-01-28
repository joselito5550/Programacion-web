from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from jugador_equipo.models import Perfiles, Equipo
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Liga, Jornada
from .form import LigaForm, JornadaForm
from django.shortcuts import redirect


# Create your views here.
class Registrar_liga(FormView):
    model = Liga
    template_name = "registrar_liga.html"
    form_class = LigaForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        liga = form.save()
        return super(Registrar_liga, self).form_valid(form)


class Registrar_jornadas(FormView):
    model = Jornada
    template_name = "crear_jornadas.html"
    form_class = JornadaForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        jornada = form.save()
        return super(Registrar_jornadas, self).form_valid(form)

def administrar_liga(request):

    return render(request,'administrador_liga.html', {})

def crear_jornadas(request):
    return render(request,'administrador_liga.html', {})

# echarle un ojo para ver si funciona bien
def buscar_liga(request,nombre_liga):
    print nombre_liga
    if Liga.objects.filter(nombre=nombre_liga).exists():
        liga = Liga.objects.get(nombre=nombre_liga)
        print liga.nombre
        equipos_liga = Equipo.objects.filter(Liga=liga)
        return render(request,'visualizar_liga',{'equipos':equipos_liga})
    else:
        return render(request,'principal.html',{})

def buscarLiga(request):
    if request.method == 'POST':
        print request.POST.get('nombre_liga')
        nombre_liga = request.POST.get('nombre_liga')
        if Liga.objects.filter(nombre=nombre_liga).exists():
            liga = Liga.objects.get(nombre=nombre_liga)
            equipos_liga = Equipo.objects.filter(Liga=liga)
            return render(request,'visualizar_liga.html',{'equipos':equipos_liga})
        else:
            return redirect('/index')
    else:

        return redirect('/index')
