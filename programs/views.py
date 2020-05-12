from .models import Program

from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView

# Create your views here.

class ProgramListView(ListView):
    model = Program


class ProgramDetailView(DetailView):
    model = Program


@method_decorator(staff_member_required, name='dispatch')
class ProgramCreate(CreateView):
    model = Program
    fields = ['name', 'description', 'module_id', 'planned', 'finished']
    success_url = reverse_lazy('programs')


@method_decorator(staff_member_required, name='dispatch')
class ProgramUpdate(UpdateView):
    model = Program
    fields = ['name', 'description', 'planned', 'finished']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('program_update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class ProgramDelete(DeleteView):
    model = Program
    success_url = reverse_lazy('programs')