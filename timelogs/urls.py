from django.urls import path

from .views import Nose

urlpatterns = [
    path('', Nose.as_view(), name='start_timelog')
]