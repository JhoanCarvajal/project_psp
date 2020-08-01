from django.urls import path

from .views import PartesAñadidaCreate

urlpatterns = [
    path('crear/<int:pk>/', PartesAñadidaCreate.as_view(), name='crear_parte_añadida'),
]