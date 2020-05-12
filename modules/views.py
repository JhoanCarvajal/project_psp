from .models import Module
from programs.models import Program

from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView

# Create your views here.

class ModuleListView(ListView):
    model = Module


class ModuleDetailView(DetailView):
    model = Module
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["programs"] = Program.objects.filter(module_id=self.get_object())
        return context


@method_decorator(staff_member_required, name='dispatch')
class ModuleCreate(CreateView):
    model = Module
    fields = ['name', 'description', 'project_id', 'planned', 'finished']
    success_url = reverse_lazy('modules')


@method_decorator(staff_member_required, name='dispatch')
class ModuleUpdate(UpdateView):
    model = Module
    fields = ['name', 'description', 'planned', 'finished']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('module_update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class ModuleDelete(DeleteView):
    model = Module
    success_url = reverse_lazy('modules')