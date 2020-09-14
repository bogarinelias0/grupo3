import os

from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
from cuentas.models import Usuario



def get_image_path(instancia, filename):
    """Construye la ruta donde se van a guardar las imágenes de perfil"""
    instancia_id = instancia.id
    if instancia_id is None:
        instancia_id = Usuario.objects.order_by("id").last().id + 1
    path = os.path.join("static/img/users/", str(instancia_id), "profile", filename)
    return path


class Perfil(models.Model):
    user = models.OneToOneField(Usuario, null=True, on_delete=models.CASCADE)
    foto = models.ImageField(default='static/img/perfiles/empty-profile.png', upload_to=get_image_path, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Perfiles'
        
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=Usuario)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=Usuario)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()
