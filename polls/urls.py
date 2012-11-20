from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from mysite.polls.models import Poll

#from django.views.generic import DetailView, ListView

#urlpatterns = patterns('',
 #   (r'^$', 
  #       ListView.as_view(
   #         queryset=Poll.objects.order_by('-pub_date')[:5],
    #        context_object_name='latest_poll_list',
     #       template_name='polls/index.html')),

    #(r'^(?P<poll_id>\d+)/$', 
     #   DetailView.as_view(
      #      model=Poll,
       #     template_name='polls/detail.html')),
    #url(r'^(?P<poll_id>\d+)/results/$',
     #   DetailView.as_view(
      #      model=Poll,
       #     template_name='polls/results.html'),
        #name='poll_results'),
     #(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
#)



urlpatterns = patterns('mysite.polls.views',
    (r'^$', 'index'),
    (r'^(?P<poll_id>\d+)/$', 'detail'),
    (r'^(?P<poll_id>\d+)/results/$', 'results'),
    (r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)

