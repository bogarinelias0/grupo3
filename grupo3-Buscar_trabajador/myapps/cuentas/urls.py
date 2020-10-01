from django.urls import path
from django.contrib.auth import views as auth_views


from . import views


urlpatterns = [
    path("usuario/<int:pk>", views.UserDetailView.as_view(), name="detalles_usuario"),
    path("usuario/editar", views.editar_perfil, name="editar_perfil"),
    path("registrar/", views.register_view, name='registrar'),
    path("login/", auth_views.LoginView.as_view(template_name='cuentas/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='cuentas/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='cuentas/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='cuentas/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="cuentas/password_reset_complete.html"), name='password_reset_complete'),
]
