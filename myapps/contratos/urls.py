from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.ContratoDetailView.as_view(), name='contratos_detalle'),
]
