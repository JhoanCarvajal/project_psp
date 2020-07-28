from django.urls import path

from .views import ProyectoListView

urlpatterns = [
    path('lista_proyectos/', ProyectoListView.as_view(), name='proyectos'),
]