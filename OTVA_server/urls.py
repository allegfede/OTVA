#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from OTVA_server import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OTVA_server.views.home', name='home'),
    # url(r'^OTVA_server/', include('OTVA_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # (r'^login/', include('auth.views.login_user')),
	#(r'^$', views.my_homepage_view),
    (r'^hello/$', views.hello),
    (r'^time/$',  views.current_datetime),
    url(r'^$', include('OTVA_server.schedule.urls')),
)

#from OTVA_server.views import my_homepage_view, hello, current_datetime
#urlpatterns = patterns('',
#    ('^$', my_homepage_view),
#    ('^hello/$', hello),
#    ('^time/$', current_datetime),
#)

from django.conf import settings

#your URL patterns

if settings.DEBUG:
    #urlpatterns += staticfiles_urlpatterns() #this servers static files and media files.
    #in case media is not served correctly
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )