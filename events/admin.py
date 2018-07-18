from django.contrib import admin

# import models
from events.models import Event
from events.models import Location

# slug creation
class EventAdmin(admin.ModelAdmin):
  model = Event
  list_display = ('name', 'description',)
  prepopulated_fields = {'slug': ('name',)}

class LocationAdmin(admin.ModelAdmin):
  model = Location
  list_display = ('name', 'description',)
  prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(Location, LocationAdmin)
