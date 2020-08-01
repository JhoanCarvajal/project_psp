from django.urls import path

from .views import PipListView, PipCreateView


urlpatterns = [
    path('lista/', PipListView.as_view(), name='lista_pips'),
    path('crear/', PipCreateView.as_view(), name='crear_pip'), 
]
