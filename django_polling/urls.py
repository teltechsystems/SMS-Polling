from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/create$', 'views.polls_create'),
    url(r'^polls/current$', 'views.polls_current'),
    url(r'^new-poll-listener$', 'views.new_poll_listener'),
    url(r'^poll/(?P<poll_id>\d+)/new-response-listener$', 'views.new_response_listener'),
    url(r'^telapi/inbound/sms$', 'views.telapi_inbound_sms'),
    url(r'^admin$', 'views.admin'),
    url(r'^$', 'views.home'),
)
