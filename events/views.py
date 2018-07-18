from django.shortcuts import render
from events.models import Event

# Create your views here.
def index(request):
  events = Event.objects.all().order_by('?')
  # featured_event = Event.objects.filter(name='Tostito Bowl').order_by('name')
  return render(request, 'index.html', {
    'events': events,
  })

def event_detail(request, slug):
  event = Event.objects.get(slug=slug)
  return render(request, 'events/event_detail.html', {
    'event': event,
  })
