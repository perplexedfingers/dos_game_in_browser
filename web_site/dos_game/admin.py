from django.contrib import admin

from .models import Game, Name, Tag, Language

admin.site.register(Game)
admin.site.register(Name)
admin.site.register(Tag)
admin.site.register(Language)
