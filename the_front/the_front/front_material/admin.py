from front_material.models import *
from django.contrib import admin

class NewsMediaInline(admin.TabularInline):
  model = NewsMedia
  #exclude = ['is_old_news']

class NewsArticleAdmin(admin.ModelAdmin):
  inlines = [
    NewsMediaInline,
  ]

class PressMediaInline(admin.TabularInline):
  model = PressMedia
class PressLinkInline(admin.TabularInline):
  model = PressLink

class PressAdmin(admin.ModelAdmin):
  inlines = [
    PressMediaInline,
    PressLinkInline,
  ]

admin.site.register(NewsArticle, NewsArticleAdmin)
admin.site.register(NewsMedia)
admin.site.register(Press, PressAdmin)
#admin.site.register(PressMedia)
admin.site.register(FrontInfo)
admin.site.register(FAQ)
admin.site.register(Link)
