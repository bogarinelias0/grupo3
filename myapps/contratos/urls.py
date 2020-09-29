from django.urls import path

from . import views


urlpatterns = [
    path('<int:pk>/', views.ContratoDetailView.as_view(), name='contratos_detalles'),
    path('contratar/oferta/<int:id_oferta>/', views.contratar, name='contratar'),
]
