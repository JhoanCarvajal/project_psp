from django.urls import path

from .views import ProgramaCreate

urlpatterns = [
    # path('crear_programa/', crear_programa, name='crear_programa'),
    path('create/', ProgramaCreate.as_view(), name='program_create'),
]