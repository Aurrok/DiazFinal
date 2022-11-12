from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from grupo.models import Banda
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from grupo.forms import BuscarBanda


def inicio(request):
    return render(request, 'grupo/inicio.html')

class RegistrarBanda(CreateView):
    model = Banda
    template_name = 'grupo/registrar_banda.html'
    success_url = '/bandas/'
    fields = ['nombre', 'cant_integrantes','descripcion']
    

class EditarBanda(LoginRequiredMixin , UpdateView):
    model = Banda
    success_url = '/bandas/'
    template_name = 'grupo/editar_banda.html'
    fields = ['nombre', 'cant_integrantes','descripcion']


class EliminarBanda(LoginRequiredMixin , DeleteView):
    model = Banda
    success_url = '/bandas/'

    template_name = 'grupo/eliminar_banda.html'
    


class ListaBandas(ListView):
    model = Banda
    template_name = 'grupo/listar_bandas.html'
    
    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        if nombre:
            object_list = self.model.objects.filter(nombre__icontains=nombre)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['form'] = BuscarBanda()
        return context
    
    

class VerBanda(DetailView):
    model=  Banda
    template_name = 'grupo/ver_banda.html'
    
    

