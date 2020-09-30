from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Pais, Provincia, Localidad, Domicilio, Perfil


admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Localidad)
admin.site.register(Domicilio)


class PerfilInline(admin.StackedInline):
    """Perfil en el admin"""
    model = Perfil
    can_delete = False
    verbose_name_plural = 'Perfil'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    """Custom User Admin, agrega el Perfil del Usuario"""
    inlines = (PerfilInline, )
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User) # Hcemos esto para poder registrar nuesto usuario customizado
admin.site.register(User, CustomUserAdmin)
