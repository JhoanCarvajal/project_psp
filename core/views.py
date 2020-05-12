from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from programs.models import Program
from modules.models import Module

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title":"personal software process"})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"


class ProgramListView(ListView):
    model = Program

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["modules"] = Module.objects.all().select_related() 
        return context