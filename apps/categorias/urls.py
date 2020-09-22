from django.urls import path

from . import views


urlpatterns = [
    path("", views.CategoriaListView.as_view(), name='categoria_lista'),
    path("crear/", views.CategoriaCrearView.as_view(), name='categoria_crear'),
    path("administrar/", views.administrar_categorias, name='categoria_administrar'),
]
