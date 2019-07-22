from django.contrib import admin

from .models import Session, Character, Player

admin.site.register(Session)
admin.site.register(Character)
admin.site.register(Player)