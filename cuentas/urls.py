from django.urls import path
from cuentas import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('ingresar/', views.ingresar, name= 'ingresar'),
    path('desconectar/', LogoutView.as_view(template_name= 'cuentas/desconectar.html'), name= 'desconectar'),
    path('nuevo_usuario/', views.nuevo_usuario, name= 'nuevo_usuario'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/cambiar-contraseña/', views.CambiarContraseña.as_view(), name='cambiar_contraseña'),
    
]
