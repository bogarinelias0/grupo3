from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from posteo import views
from posteo.views import (
    posteoListViews,
    posteoDetailViews,
    posteoCreateViews,
    posteoUpdateViews,
    posteoDeleteViews,
    like
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', posteoListViews.as_view(), name='list'),
    path('create/', posteoCreateViews.as_view(), name='create'),
    path('<int:pk>', posteoDetailViews.as_view(), name='detail'),
    path('<int:pk>/update/', posteoUpdateViews.as_view(), name='update'),
    path('<int:pk>/delete/', posteoDeleteViews.as_view(), name='delete'),
    path('post/', views.lista_post),
    path('like/<slug>/', like, name='like')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
