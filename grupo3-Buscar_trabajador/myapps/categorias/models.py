import os

from django.db import models

# Create your models here.

# TODO poner este tipo de funciones en un paquete aparte llamado utils o similar
def get_image_path(instancia, filename):
    """Construye la ruta donde se van a guardar las imágenes de la categoría"""
    categoria_id = instancia.id
    path = os.path.join("img/categorias/", str(categoria_id), "portada", filename)
    return path


class Categoria(models.Model):
    nombre = models.CharField(max_length=150)
    # slug = models.SlugField(max_length=50, unique=True)
    foto = models.ImageField(default="img/categorias/img_defecto/categoria-img.jpg", upload_to=get_image_path, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    # prepopulated_fields = {"slug": ("nombre",)}

    def __str__(self):
        return self.nombre

