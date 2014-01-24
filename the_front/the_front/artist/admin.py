from artist.models import *
from django.contrib import admin

class ArtistMediaInline(admin.TabularInline):
  model = ArtistMedia

class ArtistAdmin(admin.ModelAdmin):
  inlines = [
    ArtistMediaInline,
  ]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(ArtistMedia)
