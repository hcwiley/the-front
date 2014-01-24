from front_material.models import *
from django.contrib import admin

class NewsMediaInline(admin.TabularInline):
  model = NewsMedia

class NewsArticleAdmin(admin.ModelAdmin):
  inlines = [
    NewsMediaInline,
  ]

admin.site.register(NewsArticle, NewsArticleAdmin)
admin.site.register(NewsMedia)
admin.site.register(FrontInfo)
admin.site.register(FAQ)
