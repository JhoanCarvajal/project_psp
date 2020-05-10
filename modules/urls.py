from django.urls import path

from .views import ModuleListView, ModuleDetailView, ModuleCreate, ModuleUpdate, ModuleDelete

urlpatterns = [
    path('', ModuleListView.as_view(), name='modules'),
    path('<int:pk>/<slug:slug>/', ModuleDetailView.as_view(), name='module_detail'),
    path('create/<int:pk>', ModuleCreate.as_view(), name='module_create'),
    path('update/<int:pk>/', ModuleUpdate.as_view(), name='module_update'),
    path('delete/<int:pk>/', ModuleDelete.as_view(), name='module_delete'),
]