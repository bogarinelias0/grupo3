from django.urls import path


from .views import PerfilDetailView  #, perfil_detail_view

urlpatterns = [
    path("<int:pk>/", PerfilDetailView.as_view(), name='perfil_details'),
]
