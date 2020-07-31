from django.urls import path

from .views import GraficosDetailView

urlpatterns = [
    path('estadisticas/<int:pk>', GraficosDetailView.as_view(), name='ver_estadisticas'),
]