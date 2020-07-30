from django.urls import path

from .views import UserDeleteView, UserUpdate

urlpatterns = [
    path('actualizar/<int:pk>/', UserUpdate.as_view(), name='actualizar_cuenta'),
    path('eliminar/<int:pk>', UserDeleteView.as_view(), name='eliminar_mi_cuenta'),
]