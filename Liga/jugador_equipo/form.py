from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, FormView
from .models import Equipo, Perfiles


class UserForm(UserCreationForm, ModelForm):
    telefono = forms.IntegerField()
    equipo = forms.ModelChoiceField(
        queryset=Equipo.objects.all(), empty_label="Elige un equipo")


class EquipoForm(ModelForm):

    class Meta:
        model = Equipo
        fields = ('nombre', 'ciudad', 'anio_creacion', 'descripcion',
                  'nombre_del_entrenador', 'administrador', 'Liga', 'contrasena')
