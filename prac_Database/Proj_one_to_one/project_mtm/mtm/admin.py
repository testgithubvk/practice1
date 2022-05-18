from django.contrib import admin
from .models import Song
# Register your models here.


class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name', 'song_durn', 'written_by']

admin.site.register(Song, SongAdmin)
