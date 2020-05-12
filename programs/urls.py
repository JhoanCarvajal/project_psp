from django.urls import path

from .views import ProgramListView, ProgramDetailView, ProgramCreate, ProgramUpdate, ProgramDelete

urlpatterns = [
    path('', ProgramListView.as_view(), name='programs'),
    path('<int:pk>/<slug:slug>/', ProgramDetailView.as_view(), name='program_detail'),
    path('create/<int:pk>', ProgramCreate.as_view(), name='program_create'),
    path('update/<int:pk>/', ProgramUpdate.as_view(), name='program_update'),
    path('delete/<int:pk>/', ProgramDelete.as_view(), name='program_delete'),
]