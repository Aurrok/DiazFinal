from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from cuentas.forms import FormularioDeRegistro,EditarPerfilFormulario,CambioContraseña
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from cuentas.models import ExtensionUsuario


def ingresar(request):
    
    if request.method  == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            extensionUsuario, es_nuevo = ExtensionUsuario.objects.get_or_create(user=request.user)
            return redirect('inicio')
    else:       
        formulario = AuthenticationForm()
    
    
    return render(request, 'cuentas/ingresar.html', {'formulario' : formulario }) 

def nuevo_usuario(request):
    
    if request.method  == 'POST':
        formulario = FormularioDeRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = FormularioDeRegistro()
    
    return render(request, 'cuentas/nuevo_usuario.html', {'formulario' : formulario })

@login_required
def perfil(request):
    
    
    return render(request,'cuentas/perfil.html', {})


@login_required
def editar_perfil(request):
     
    request.user.extensionusuario
     
    if request.method == 'POST':
        formulario = EditarPerfilFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            data_nueva = formulario.cleaned_data
            request.user.first_name = data_nueva['first_name']
            request.user.last_name = data_nueva['last_name']
            request.user.email = data_nueva['email']
            request.user.extensionusuario.avatar = data_nueva['avatar']
           
            request.user.extensionusuario.save()
            request.user.save()
            return redirect('perfil')
        
    else:
        formulario = EditarPerfilFormulario(initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email, 
            'avatar': request.user.extensionusuario.avatar,
            }
        )
    
     
    return render(request,'cuentas/editar_perfil.html', {'formulario' : formulario})


class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cuentas/cambiar_contraseña.html'
    success_url = '/perfil/'
    form_class = CambioContraseña
    

    