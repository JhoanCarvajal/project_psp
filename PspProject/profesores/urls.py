from django.urls import path
from .views import profesorDetalles

urlpatterns = [
    path('detalles/', profesorDetalles , name='profesor_detaller'), 
]