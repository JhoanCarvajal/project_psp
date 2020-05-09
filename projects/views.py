from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Project
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from .forms import ProjectForm
from django.views.generic.detail import DetailView

# Create your views here.

class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project


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