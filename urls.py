from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^polls/', include('polls.urls')),
    (r'^admin/', include(admin.site.urls)),
)

    # Examples:
    #(r'^polls/$', 'index'),
    #(r'^polls/(?P<poll_id>\d+)/$', 'detail'),
    #(r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
    #(r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),


    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#urlpatterns += patterns('',
 #   (r'^admin/', include(admin.site.urls)),
#)
