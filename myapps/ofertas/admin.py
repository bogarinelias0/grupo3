from django.contrib import admin

# Register your models here.
from .models import Oferta
from .models import ImagenOferta

admin.site.register(Oferta)
admin.site.register(ImagenOferta)
