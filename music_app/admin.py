from django.contrib import admin
from .models import Song

# Register your models here.
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'audio_file', 'image', 'Musical_genres')
    search_fields = ('Musical_genres',)
admin.site.register(Song, SongAdmin)