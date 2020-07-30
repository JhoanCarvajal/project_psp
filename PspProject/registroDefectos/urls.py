from django.urls import path

from .views import RegistroDefectoCreate

urlpatterns = [
    #path('lista/<int:id_u>/<int:id_p>/', RegistroTiempoCreate, name='lista_tiempos'),
    #path('detalles/<int:pk>/<slug:slug>/', RegistroTiempoCreate, name='detalles_tiempo'),
    path('crear/', RegistroDefectoCreate, name='crear_registro_defecto'),
]