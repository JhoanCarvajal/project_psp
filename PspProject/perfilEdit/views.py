from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def editPerfilUser(request):
    return render(request, 'perfilEdit/editPerfil.html',{
        'title':'Perfil de usuario',
    })



# Create your views here.
@method_decorator(login_required, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    template_name = "perfilEdit/user_confirm_delete.html"
    success_url = reverse_lazy('login')



# Create your views here.
@method_decorator(login_required, name='dispatch')
class UserUpdate(UpdateView):
    model = User
    fields = ['first_name','last_name']
    template_name = "perfilEdit/user_form.html"

    def get_success_url(self):
        return reverse_lazy('proyectos')
