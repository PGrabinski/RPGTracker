from django.contrib import admin

from .models import Session, Character, Player

class CharactersInline(admin.TabularInline):
    model = Session.characters.through
    extra = 1

class SessionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Session info', {'fields': ['title', 'game_master', 'game_date',]}),
        ('Details', {'fields': ['description', 'xp_for_all']})
    ]
    inlines = [CharactersInline]
    search_fields = ['title']
    list_display = ('title', 'game_date')
    list_filter = ['game_date']

class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['first_name', 'last_name', 'nickname']}),
        ('Date', {'fields': ["join_date"]},)
    ]
    list_display = ('first_name', 'last_name', 'nickname')
    list_filter = ['last_name']
    search_fields = ['first_name', 'last_name', 'nickname']

class CharacterAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General', {'fields': ['player', 'name', 'creation_date']}),
        ('Career', {'fields': ['career_path', 'career_level']},)
    ]
    list_display = ('name', 'career_path')
    list_filter = ['career_path', 'care_level']
    search_fields = ['name', 'career_path']

admin.site.register(Session, SessionAdmin)
admin.site.register(Character)
admin.site.register(Player)