from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings # New Import
from django.conf.urls.static import static # New Import

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Looks for url strings that match the pattern ^blog/. Once it's found, it takes the remainder of the url string and passes onto blog.urls, which handles it. Done with the help of the include() fn
    url(r'^blog/', include('blog.urls')),
    url(r'^assassin/', include('assassin.urls')),
)

# Makes sure that when DEBUG is false in the settings that the ALLOWED_HOSTS variable is modified
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
