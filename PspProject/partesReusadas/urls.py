from django.urls import path

from .views import PartesReusadaCreateView

urlpatterns = [
    path('crear/<int:pk>', PartesReusadaCreateView.as_view(), name='crear_parte_reusada'),
]