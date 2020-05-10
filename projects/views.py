from .models import Project
from .forms import ProjectForm
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView

#import of model Module for add one list in the project
from modules.models import Module

# Create your views here.

class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["modules"] = Module.objects.filter(project_id=self.get_object())
        return context


@method_decorator(staff_member_required, name='dispatch')
class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('projects')


@method_decorator(staff_member_required, name='dispatch')
class ProjectUpdate(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('project_update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('projects')