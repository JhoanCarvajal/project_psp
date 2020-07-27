from django.urls import path

from .views import ProgramaCreate, ProgramaListView

urlpatterns = [
    path('lista/<int:id_u>/<int:id_p>/', ProgramaListView.as_view(), name='lista_programas_usuario'),
    path('crear/<int:id_u>/<int:id_p>/', ProgramaCreate.as_view(), name='program_create'),
]