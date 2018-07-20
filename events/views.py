from django.shortcuts import render, redirect
from events.forms import EventForm
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

def edit_event(request, slug):
  event = Event.objects.get(slug=slug)
  form_class = EventForm

  # if we're coming to this view from the submitted form
  if request.method == 'POST':
    # Get data from the submitted form
    form = form_class(data=request.POST, instance=event)
    if form.is_valid():
      form.save()
      return redirect('event_detail', slug=event.slug)

  # otherwise just show the form
  else:
    form = form_class(instance=event)

  return render(request, 'events/edit_event.html', {
    'event': event,
    'form': form,
  })
