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
from loginRegister import views as loginss

urlpatterns = [
    path('', loginss.login_page), 
    path('admin/', admin.site.urls),
    path('modulos/', views.modulos, name='modulos'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('log_in/', loginss.login_page, name='log_in'),
    path('register/', loginss.register, name='register'),
    path('logout_page/', loginss.logout_usert, name='logout_page'),
    # para poder incluir lo de reset pass
    path('accounts/', include('django.contrib.auth.urls')),

]
