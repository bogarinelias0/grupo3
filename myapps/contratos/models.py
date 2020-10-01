from django.db import models
from django.utils import timezone

# Create your models here.

from django.contrib.auth.models import User
from myapps.ofertas.models import Oferta
from myapps.categorias.models import Categoria


class Contrato(models.Model):
    CHOICES = [
        ("en espera", "En espera"),
        ("aceptado", "Aceptado"),
        ("rechazado", 'Rechazado'),
        ("finalizado", 'Finalizado'),
        ("cancelado", "Cancelado"),
        ("borrador", "Borrador")
    ]
    PUNTAJES = [
        (1, 'Malo'),
        (2, 'Regular'),
        (3, 'Pasable'),
        (4, 'Bueno'),
        (5, 'Excelente'),
    ]
    oferta = models.ForeignKey(Oferta, null=True, blank=True, related_name='contratos', on_delete=models.SET_NULL)
    contratante = models.ForeignKey(User, null=False, blank=False, related_name='contratos_hechos', on_delete=models.PROTECT)
    contratado = models.ForeignKey(User, null=False, blank=False, related_name='contratos_recibidos', on_delete=models.PROTECT)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(default=CHOICES[5][0], choices=CHOICES, max_length=15)
    detalles = models.TextField(null=True, blank=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    categorias = models.ManyToManyField(Categoria, blank=True)
    puntaje = models.IntegerField(choices=PUNTAJES, default=None, null=True, blank=True)

    def cerrar(self):
        self.fecha_cierre = timezone.now()
        self.estado = self.CHOICES[3][0]
        self.save()

    def aceptar(self):
        self.estado = self.CHOICES[1][0]
        self.save()

    def finalizar(self):
        self.estado = self.CHOICES[3][0]
        self.save()

    def rechazar(self):
        self.estado = self.CHOICES[2][0]
        self.save()

    def is_active(self):
        if self.estado in self.CHOICES[0:2]:
            return True
        else:
            return False

    def __str__(self):
        return str(self.id)

    def set_puntaje(self, puntaje):
        if puntaje in self.PUNTAJES:
            self.puntaje = puntaje

    def get_punjate(self):
        return self.puntaje

    def confirmar(self):
        self.estado = self.CHOICES[0][0]
        self.save()

    def inicial(self):
        self.estado = self.CHOICES[5][0]
        self.save()


# class Trabajo(models.Model):
#     PUNTAJES = [
#         (1, 'Malo'),
#         (2, 'Regular'),
#         (3, 'Pasable'),
#         (4, 'Bueno'),
#         (5, 'Excelente'),
#     ]
#     CHOICES = [
#         ("en espera", "En espera"),
#         ("aceptado", "Aceptado"),
#         ("rechazado", 'Rechazado'),
#         ("finalizado", 'Finalizado'),
#         ("cancelado", "Cancelado"),
#     ]
#     contratante = models.ForeignKey(User, on_delete=models.CASCADE)
#     trabajador = models.ForeignKey(User, on_delete=models.CASCADE)
#     contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
#     puntaje = models.IntegerField(choices=PUNTAJES, default=None, null=True, blank=True)
#     estado = models.CharField(default=CHOICES[0][0], choices=CHOICES, max_length=15)

#     def puntuar(self, puntaje):
#         if puntaje in self.PUNTAJES:
#             self.puntaje = puntaje
