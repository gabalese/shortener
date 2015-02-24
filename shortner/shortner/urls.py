from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', 'urls.views.home_view', name='home'),
    url(r'^list/', 'urls.views.url_list_view', name='list'),
    url(r'^create/', 'urls.views.url_create_view', name='create'),
    url(r'^admin/', include(admin.site.urls)),
)
