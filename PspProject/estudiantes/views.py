from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Estudiante
from programas.models import Programa

# Create your views here.
class EstudiantesNoCertificados(TemplateView):
    template_name = "estudiantes/estudiante_no_certificados.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = Estudiante.objects.all()
        return context

class EstudiantesCertificados(TemplateView):
    template_name = "estudiantes/estudiante_certificados.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = Estudiante.objects.all()
        return context

class EstudiantesCertificar(TemplateView):
    template_name = "estudiantes/estudiante_certificar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        estudiantes = Estudiante.objects.all()
        profesor = self.request.user.profesor
        context["profesor"] = profesor
        programas = []
        cantidad = []
        estudiantes_certificar = []
        for estudiante in estudiantes:
            if estudiante.id_profesor.id == profesor.id:
                p = Programa.objects.filter(id_usuario=estudiante.id_usuario)
                cant = p.count()
                if cant >= 4:
                    estudiantes_certificar.append(estudiante)
                    programas.append(p)
                    cantidad.append(p.count())
        context["programas"] = programas
        context["cantidad"] = cantidad
        context["estudiantes"] = estudiantes_certificar
                

        return context