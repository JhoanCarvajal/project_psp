"""PspProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainApp import views
from perfilEdit import views as editPerfil
from programas import views as programaP


urlpatterns = [
    path('', include('mainApp.urls')), 
    path('admin/', admin.site.urls),
    #apps
    path('programas/', include('programas.urls')),
    path('proyectos/', include('proyectos.urls')),
    path('registroTiempos/', include('registroTiempos.urls')),
    path('registroDefectos/', include('registroDefectos.urls')),
    path('tiposDefectos/', include('tiposDefectos.urls')),
    path('partesBases/', include('partesBases.urls')),
    path('perfilEdit/', include('perfilEdit.urls')),
    path('partesAñadidas/', include('partesAñadidas.urls')),
    path('partesReusadas/', include('partesReusadas.urls')),
    
    path('modulos/', views.modulos, name='modulos'),
    path('perfil/',editPerfil.editPerfilUser, name='editPerfilUs'),
    path('programa/',programaP.programa, name='programa'),
    path('programas/',programaP.programas, name='programas'),
    path('defectos/',programaP.defectos, name='defectos'),
    path('listaDefesctos/',programaP.listaDefesctos, name='listaDefectos'),
    
    #url para mostrar programas
    path('programas/<int:id_proyecto>/', views.programasDeUsuarios, name='lista_programas_usuario'),

    #path para el login y todo lo relacionado
    path('accounts/', include('registration.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('resportes/', include('reportes.urls')),

]
