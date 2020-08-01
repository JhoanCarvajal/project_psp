from django.urls import path

from .views import EstudiantesNoCertificados, EstudiantesCertificados, EstudiantesCertificar

urlpatterns = [
    path('no_certificados/', EstudiantesNoCertificados.as_view(), name='lista_no_certificados'),
    path('certificados/', EstudiantesCertificados.as_view(), name='lista_certificados'),
    path('certificar/', EstudiantesCertificar.as_view(), name='lista_certificar'),
]