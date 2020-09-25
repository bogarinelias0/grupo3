from django.db import models

# Create your models here.
class Provincia(models.Model):
	id = models.AutoField (primary_key = True)
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre




class Localidad(models.Model):
	id = models.AutoField (primary_key = True)
	nombre = models.CharField(max_length=30)
	provincia = models.ForeignKey(Provincia, null=False, blank=False, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre


