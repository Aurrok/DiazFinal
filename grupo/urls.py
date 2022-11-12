from django.urls import path
from grupo import views 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('bandas/', views.ListaBandas.as_view(), name = 'listar_bandas'),
    path('bandas/registrar/', views.RegistrarBanda.as_view(), name = 'registrar'),
    path('bandas/<int:pk>/editar/', views.EditarBanda.as_view(), name = 'editar_banda'),
    path('banda/<int:pk>/eliminar/', views.EliminarBanda.as_view(), name = 'eliminar_banda'),
    path('banda/<int:pk>/ver-banda/', views.VerBanda.as_view(), name = 'ver_banda'),
]
