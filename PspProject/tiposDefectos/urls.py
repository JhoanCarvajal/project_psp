from django.urls import path

from .views import TiposDefectoListView, TipoDefectoCreateView

urlpatterns = [
    path('lista/', TiposDefectoListView.as_view(), name='lista_tipos_defectos'),
    path('crear/', TipoDefectoCreateView.as_view(), name='crear_tipos_defectos'),
]