from django.contrib import admin
from .models import Song

# Register your models here.

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'audio_files','image','music_generes')
    search_fields = ('music_generes'),
admin.site.register(Song,SongAdmin)