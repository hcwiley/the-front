from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'the_front.views.home', name='home'),
     url(r'^contact$', 'the_front.views.contact', name='contact'),
     url(r'^about$', 'the_front.views.about', name='about'),

     url(r'^artists', include('artist.urls')),
     url(r'^news', include('front_material.news.urls')),

     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
)
if settings.IS_DEV:
    # let django serve user generated media while in development
    urlpatterns += patterns('',
#TODO don't let people name their top level series admin, site_media, etc.
        #url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
