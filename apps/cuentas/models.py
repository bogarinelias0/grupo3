import os
from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings


# def get_image_path(instancia, filename):
#     """Construye la ruta donde se van a guardar las imágenes de perfil"""
#     instancia_id = instancia.id
#     if instancia_id is None:
#         instancia_id = User.objects.order_by("id").last().id + 1
#     path = os.path.join("static/img/users/", str(instancia_id), "profile", filename)
#     return path

def get_image_path(instancia, filename):
    """Construye la ruta donde se van a guardar las imágenes de perfil"""
    user_id = instancia.user.id
    # if user_id is None:
    #     user_id = User.objects.order_by("id").last().id + 1
    path = os.path.join("img/users/", str(user_id), "profile", filename)
    return path


class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Países'

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, null=False, blank=False, related_name='provincias', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return self.nombre



class Localidad(models.Model):
    nombre = nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, null=False, blank=False, related_name='localidades', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Localidades'

    def __str__(self):
        return self.nombre


class Domicilio(models.Model):
    calle = models.CharField(max_length=100, blank=True, null=True)
    numero_calle = models.IntegerField(blank=True, null=True)
    manzana = models.IntegerField(blank=True, null=True)
    parcela = models.IntegerField(blank=True, null=True)
    barrio = models.CharField(max_length=100, blank=True, null=True)
    localidad = models.ForeignKey(Localidad, null=True, blank=True, related_name='domicilios', on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Domicilios'

    def __str__(self):
        return self.calle + ' ' + (str(self.numero_calle) if self.numero_calle else '')


class Perfil(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    foto = models.ImageField(default='img/perfiles/empty-profile.png', upload_to=get_image_path, null=True, blank=True)
    descripcion = models.TextField(max_length=1000, blank=True)
    puntuacion = models.DecimalField(null=True, blank=True, max_digits=3, decimal_places=2)
    domicilio = models.ForeignKey(Domicilio, related_name='personas', on_delete=models.PROTECT, null=True, blank=True)
    numero_telefono = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return self.user.username


# truquito para crear un perfil si se crea un usuario
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()
