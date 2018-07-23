from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404
from events.forms import EventForm
from events.models import Event

# Create your views here.
def index(request):
  events = Event.objects.all()
  # featured_event = Event.objects.filter(name='Tostito Bowl').order_by('name')
  return render(request, 'index.html', {
    'events': events,
  })

def event_detail(request, slug):
  event = Event.objects.get(slug=slug)
  return render(request, 'events/event_detail.html', {
    'event': event,
  })

@login_required
def edit_event(request, slug):
  event = Event.objects.get(slug=slug)

  if event.user != request.user:
    raise Http404

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

def create_event(request):
  form_class = EventForm
  # if form is being submitted, submit it!
  if request.method == 'POST':
    form = form_class(request.POST)
    if form.is_valid():
      # Create an instance but don't save yet
      event = form.save(commit=False)
      event.user = request.user
      event.slug = slugify(event.name)
      # Save
      event.save()
      # redirect to new event
      return redirect('event_detail', slug=event.slug)
  # otherwise just show the form
  else:
    form = form_class()

  return render(request, 'events/create_event.html', {
    'form': form,
  })

def account(request):
  return render(request, 'registration/account.html')
