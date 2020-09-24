from django.urls import path

from . import views 


urlpatterns = [
    path("", views.OfertaListView.as_view(), name='ofertas'),
    path("crear/", views.OfertaCreateView.as_view(), name='ofertas_crear'),
    path("detalles/<int:pk>/", views.OfertaDetailView.as_view(), name='oferta_detalles'),
]
