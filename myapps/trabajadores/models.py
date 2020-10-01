from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):

    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey( User,on_delete=models.CASCADE)
    #autor = models.OneToOneField(User, null=False, on_delete=models.CASCADE)


    def __str__(self):
    	return self.titulo


class Comentario(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	tiempo_creacion = models.DateTimeField(auto_now_add=True)
	contenido = models.TextField()

	def __str__(self):
		return self.contenido



