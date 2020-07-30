from django.urls import path

from .views import ReporteListView, ReporteCreateView


urlpatterns = [
    path('lista/', ReporteListView.as_view(), name='lista_reportes'),
    path('create/', ReporteCreateView.as_view(), name='create_reportes'), 
]
