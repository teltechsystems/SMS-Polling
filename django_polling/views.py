from application.models import Poll
from django.shortcuts import render, HttpResponse

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

def polls_create(request):
    return render(request, 'polls/create.html')

def polls_current(request):
    return render(request, 'polls/current.html', {
        'poll'      : Poll.get_current()
    })