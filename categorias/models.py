from django.db import models

# Create your models here.
class Categoria(models.Model):
	id = models.AutoField (primary_key = True)
	nombre = models.CharField('Nombre de la Categoria', max_length = 100)
	estado = models.BooleanField('Categoria Activada/Categoria no Activada', default = True)
	fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'

	def _str_(self):
		return self.nombre

