from django.urls import path

from .views import ReporteListView


urlpatterns = [
    path('lista/', ReporteListView.as_view(), name='lista_reportes'),
    
]