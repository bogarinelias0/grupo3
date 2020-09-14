import os

from django.db import models
from django.contrib.auth.models import User #, AbstractUser
# from django.core.validators import RegexValidator # To use later in a phone number validation
from django.conf import settings

# Create your models here.


class Domicilio(models.Model):
    provincia = models.CharField(max_length=80, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    barrio = models.CharField(max_length=100, blank=True, null=True)
    calle = models.CharField(max_length=100, blank=True, null=True)
    numero_calle = models.IntegerField(blank=True, null=True)
    manzana = models.IntegerField(blank=True, null=True)
    parcela = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.calle + ' ' + (str(self.numero_calle) if self.numero_calle else '')


# def get_image_path(instancia, filename):
#     """Construye la ruta donde se van a guardar las imágenes de perfil"""
#     instancia_id = instancia.id
#     if instancia_id is None:
#         instancia_id = Usuario.objects.order_by("id").last().id + 1
#     path = os.path.join("images/users/", str(instancia_id), "profile", filename)
#     print(path)
#     return path


class Usuario(User):
    numero_telefono = models.CharField(max_length=13, null=True, blank=True)
    domicilio = models.ForeignKey(Domicilio, related_name='people', on_delete=models.PROTECT, null=True, blank=True)
    # foto = models.ImageField(upload_to=get_image_path, null=True, blank=True)
