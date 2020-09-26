from django.contrib import admin


from.models import Posteo, Comment, Like, Dislike, User

admin.site.register(Posteo)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(User)
