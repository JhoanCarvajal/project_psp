from django.urls import path

from .views import ProgramaCreate, ProgramaListView, ProgramaDetailView, InfoPrograma

urlpatterns = [
    path('lista/<int:id_u>/<int:id_p>/', ProgramaListView.as_view(), name='lista_programas_usuario'),
    path('detalles/<int:pk>/<slug:slug>/', ProgramaDetailView.as_view(), name='detalles_programa'),
    path('crear/<int:id_u>/<int:id_p>/', ProgramaCreate.as_view(), name='program_create'),
    path('info/<int:pk>/', InfoPrograma.as_view(), name='info_programa'),
]