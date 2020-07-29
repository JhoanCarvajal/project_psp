from django.urls import path

from .views import TiposDefectoListView

urlpatterns = [
    path('lista/', TiposDefectoListView.as_view(), name='lista_tipos_defectos'),
]