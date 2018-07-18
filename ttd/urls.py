from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from events import views

urlpatterns = [
  path('', views.index, name='home'),
  path('about/',
      TemplateView.as_view(template_name='about.html'),
      name='about'),
  path('contact/',
      TemplateView.as_view(template_name='contact.html'),
      name='contact'),
  path('events/<slug>/', views.event_detail,
    name='event_detail'),
  path('admin/', admin.site.urls),
]
