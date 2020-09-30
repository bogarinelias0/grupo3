from django.urls import path

from . import views


urlpatterns = [
    path("", views.buscar, name='buscar'),
]

# urlpatterns = [
#     path("", views.buscar_trabajador, name='buscar trabajador'),
# ]
