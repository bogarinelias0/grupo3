from django.urls import path

from . import views
from django.conf.urls import handler404
from myapps.home.views import mi_error_404
 
handler404 = mi_error_404

urlpatterns = [
    path('', views.HomeView.as_view(), name='inicio'),
    
]
