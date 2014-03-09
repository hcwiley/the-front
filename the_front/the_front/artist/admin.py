from artist.models import *
from django.contrib import admin

class ArtistMediaInline(admin.TabularInline):
  model = ArtistMedia

def generate_thumbnails(modeladmin, request, queryset):
  for obj in queryset:
    obj.saveThumbnail()
    obj.saveImage()
generate_thumbnails.short_description = "Re-generate thumbnail images"

class ArtistMediaAdmin(admin.ModelAdmin):
  actions = [generate_thumbnails]

class ArtistAdmin(admin.ModelAdmin):
  inlines = [
    ArtistMediaInline,
  ]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(ArtistMedia, ArtistMediaAdmin)
