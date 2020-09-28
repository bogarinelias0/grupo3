from django.urls import path

from . import views 


urlpatterns = [
    path("", views.OfertaListView.as_view(), name='ofertas'),
    # path("crear/", views.OfertaCreateView.as_view(), name='ofertas_crear'),
    path("crear/", views.postear_oferta, name='ofertas_crear'),
    # path("editar/<int:id>", views.editar_oferta, name='ofertas_editar'),
    path("editar/<int:pk>", views.OfertaUpdateView.as_view(), name='ofertas_editar'),
    path("detalles/<int:pk>/", views.OfertaDetailView.as_view(), name='oferta_detalles'),
]
