from django.urls import path, include
from .views import register, log_out

urlpatterns = [
    path('register/', register, name='register'),
    path('log_out/', log_out, name='log_out'),
]