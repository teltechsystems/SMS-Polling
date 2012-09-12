from application.models import Poll
from django.shortcuts import render, HttpResponse, get_object_or_404

import simplejson
import time

def home(request):
    return render(request, 'home.html', {
        'recent_polls'  : Poll.objects.all().order_by('-id')[:5]
    })
    
def new_poll_listener(request):
    running_poll = Poll.get_current()
    
    new_poll = None
    
    while True:
        time.sleep(1)
        
        new_poll = Poll.get_current()
        
        if new_poll != running_poll:
            break
    
    return HttpResponse(simplejson.dumps({
        'new_poll'      : True
    }), content_type="application/json")
    
def new_response_listener(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    
    try:
        recent_response = poll.response_set.all().order_by('-id')[0]
    except IndexError, e:
        recent_response = None
    
    new_response = None
    
    while True:
        time.sleep(1)
        
        new_response = poll.response_set.all().order_by('-id')[0]
        
        if new_response != recent_response:
            break
    
    return HttpResponse(simplejson.dumps({
        'new_response'      : True
    }), content_type="application/json")

def polls_create(request):
    return render(request, 'polls/create.html')

def polls_current(request):
    return render(request, 'polls/current.html', {
        'poll'      : Poll.get_current()
    })