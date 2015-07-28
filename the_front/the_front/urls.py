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
     url(r'^join$', 'the_front.views.join', name='join'),
     url(r'^fundraiser$', 'the_front.views.fundraiser', name='fundraiser'),
     url(r'^fundraiser/$', 'the_front.views.fundraiser', name='fundraiser'),
     url(r'^film-festival$', 'the_front.views.film_festival', name='film_festival'),
     url(r'^film-festival/$', 'the_front.views.film_festival', name='film_festival'),
     url(r'^fundraiser/success$', 'the_front.views.success', name='success'),
     url(r'^contact$', 'the_front.views.contact', name='contact'),
     url(r'^about$', 'the_front.views.about', name='about'),

     url(r'^artists', include('artist.urls')),
     url(r'^shows', include('front_material.news.urls')),
     url(r'^press', include('front_material.press.urls')),
     url(r'^links', include('front_material.links.urls')),

     url(r'^image/rotate/(?P<dirr>.*)/(?P<pk>.*)$', 'the_front.views.rotate', name='rotate'),
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
     (r'^tinymce/', include('tinymce.urls')),
)
if settings.IS_DEV:
    # let django serve user generated media while in development
    urlpatterns += patterns('',
#TODO don't let people name their top level series admin, site_media, etc.
        #url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
