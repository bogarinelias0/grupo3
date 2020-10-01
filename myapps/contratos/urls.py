from django.urls import path

from . import views


urlpatterns = [
    # path('<int:pk>/', views.ContratoDetailView.as_view(), name='contratos_detalles'),
    path('<int:pk>/', views.contrato_detail_view, name='contratos_detalles'),
    path('<int:id_contrato>/aceptar/', views.aceptar_contrato, name='aceptar_contrato'),
    path('<int:id_contrato>/rechazar/', views.rechazar_contrato, name='rechazar_contrato'),
    path('<int:id_contrato>/confirmar/', views.confirmar_contrato, name='confirmar_contrato'),
    path('<int:id_contrato>/finalizar/', views.finalizar_contrato, name='finalizar_contrato'),
    # path('<int:id_contrato>/puntuar/', views.puntuar, name='puntuar'),
    path('mis_contratos/', views.mis_contratos, name='mis_contratos'),
    path('contratar/oferta/<int:id_oferta>/', views.contratar, name='contratar'),
    path('contratar/cancelar/<int:id_contrato>/', views.cancelar_contrato, name='cancelar_contrato'),
]
