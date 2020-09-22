from django.contrib import admin

# Register your models here.

from.models import posteo, posteoview, Coment, like, dislike

admin.site.register(posteo)
admin.site.register(posteoview)
admin.site.register(Coment)
admin.site.register(like)
admin.site.register(dislike)
