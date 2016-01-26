from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, FormView
from .models import Liga, Jornada


class LigaForm(ModelForm):

    class Meta:
        model = Liga
        fields = ('nombre', 'ciudad', 'anio_creacion', 'descripcion',
                  'administrador')


class JornadaForm(ModelForm):

    class Meta:
        model = Jornada
        fields = ('equipo1', 'equipo2', 'numero','fecha','ida_vuelta')
