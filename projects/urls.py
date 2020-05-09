from django.urls import path

from .views import ProjectListView, ProjectCreate, ProjectUpdate, ProjectDelete, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects'),
    path('<int:pk>/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('create/', ProjectCreate.as_view(), name='project_create'),
    path('update/<int:pk>/', ProjectUpdate.as_view(), name='project_update'),
    path('delete/<int:pk>/', ProjectDelete.as_view(), name='project_delete'),
]