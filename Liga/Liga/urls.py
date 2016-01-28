"""Liga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from jugador_equipo import views
from equipo_jornada.views import Registrar_liga, administrar_liga, crear_jornadas, Registrar_jornadas, buscar_liga, buscarLiga

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inicio_sesion$', views.inicio_sesion),
    url(r'^login$', views.login),
    url(r'^index$', views.index),
    url(r'^cerrar$', views.cerrar),
    url(r'^registro$', views.Registrarse.as_view(), name='registrarse'),
    url(r'^registrar_equipo$', views.Registrar_equipo.as_view(),
        name='registrar_equipo'),
    url(r'^registrar_liga$', Registrar_liga.as_view(), name='registrar_liga'),
    url(r'^crear_jornadas/$', Registrar_jornadas.as_view(), name='registrar_jornada'),
    url(r'^ver_equipos$', views.ver_equipos),
    url(r'^unirte_equipo$', views.unirte_equipo),
    url(r'^buscar_liga/(?P<nombre_liga>\w+)', buscar_liga),
    url(r'^buscarLiga/$', buscarLiga)
]
