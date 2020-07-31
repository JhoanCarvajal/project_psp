from django.urls import path

from .views import RegistroTiempoCreate, TiemposListView, CrearRegistroTiempoView

urlpatterns = [
    path('lista/<int:pk>', TiemposListView.as_view(), name='lista_tiempos'),
    path('crear/<int:pk>', CrearRegistroTiempoView.as_view(), name='form_crear_registro_tiempo'),
    path('insertar/', RegistroTiempoCreate, name='crear_registro_tiempo'),
    
]