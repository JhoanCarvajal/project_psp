from django.urls import path

from .views import RegistroTiempoCreate, TiemposListView

urlpatterns = [
    path('lista/<int:pk>', TiemposListView.as_view(), name='lista_tiempos'),
    #path('redirect/<int:pk>', redirect_create, name='redirect_create'),
    path('crear/<int:pk>', RegistroTiempoCreate.as_view(), name='crear_registro_tiempo'),
    
]