from .models import Phase

from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView

# Create your views here.

class PhaseListView(ListView):
    model = Phase


class PhaseDetailView(DetailView):
    model = Phase


@method_decorator(staff_member_required, name='dispatch')
class PhaseCreate(CreateView):
    model = Phase
    fields = ['name', 'description']
    success_url = reverse_lazy('phases')


@method_decorator(staff_member_required, name='dispatch')
class PhaseUpdate(UpdateView):
    model = Phase
    fields = ['name', 'description']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('phase_update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class PhaseDelete(DeleteView):
    model = Phase
    success_url = reverse_lazy('phases')