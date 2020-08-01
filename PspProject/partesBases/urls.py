from django.urls import path

from .views import ParteBaseCreate

urlpatterns = [
    path('crear/<int:pk>/', ParteBaseCreate.as_view(), name='crear_parte_base'),
]