from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from jugador_equipo.models import Perfiles, Equipo
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Liga, Jornada
from .form import LigaForm, JornadaForm

# Create your views here.
class Registrar_liga(FormView):
    model = Liga
    template_name = "registrar_liga.html"
    form_class = LigaForm
    success_url = reverse_lazy('index/')

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