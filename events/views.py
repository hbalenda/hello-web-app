from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404
from events.forms import EventForm
from events.models import Event, User

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

def browse_by_name(request, initial=None):
  if initial:
    events = Event.objects.filter(
      name__istartswith=initial).order_by('name')
  else:
    events = Event.objects.all().order_by('name')
  initialLetters = []
  print(events)
  for event in events:
    name = event.name.lower().split()[0]
    initialLetters.append(name[0])
  initialLetters = "".join(sorted(list(set(initialLetters))))
  print(initialLetters)
  return render(request, 'search/search.html', {
    'events': events,
    'initialLetters': initialLetters,
    'initial': initial,
  })

def account(request, username):
  user = User.objects.get(username=username)
  events = Event.objects.filter(user=user)
  return render(request, 'registration/account.html', {
    'events': events
  })
