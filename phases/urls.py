from django.urls import path

from .views import PhaseListView, PhaseDetailView, PhaseCreate, PhaseUpdate, PhaseDelete

urlpatterns = [
    path('', PhaseListView.as_view(), name='phases'),
    path('<int:pk>/<slug:slug>/', PhaseDetailView.as_view(), name='phase_detail'),
    path('create/', PhaseCreate.as_view(), name='phase_create'),
    path('update/<int:pk>/', PhaseUpdate.as_view(), name='phase_update'),
    path('delete/<int:pk>/', PhaseDelete.as_view(), name='phase_delete'),
]