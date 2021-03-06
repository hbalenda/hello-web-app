from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import (
  password_reset,
  password_reset_done,
  password_reset_confirm,
  password_reset_complete,
  password_change,
  password_change_done,
)
from events.backends import MyRegistrationView

from events import views

urlpatterns = [
  path('', views.index, name='home'),
  path('about/',
      TemplateView.as_view(template_name='about.html'),
      name='about'),
  path('contact/',
      TemplateView.as_view(template_name='contact.html'),
      name='contact'),
  # event URls
  path('browse/', RedirectView.as_view(
    pattern_name='browse', permanent=True)),
  path('browse/name/', views.browse_by_name, name='browse'),
  path('browse/name/<initial>/', views.browse_by_name, name='browse_by_name'),
  path('events/', RedirectView.as_view(
    pattern_name='browse', permanent=True)),
  path('events/<slug>/', views.event_detail,
    name='event_detail'),
  path('events/<slug>/edit',
    views.edit_event, name='edit_event'),
  # account
  path('accounts/', include('registration.backends.simple.urls')),
  path('accounts/account/<username>', views.account, name="account"),
  path('accounts/register/', MyRegistrationView.as_view(),
    name='registration_register'),
  path('accounts/create_event/', views.create_event,
    name='registration_create_event'),
  # password reset URLs
  path('accounts/password/reset/', password_reset,
    {'template_name': 'registration/password_reset_form.html'},
    name="password_reset"),
  path('accounts/password/reset/done', password_reset_done,
    {'template_name': 'registration/password_reset_done.html'},
    name="password_reset_done"),
  path('accounts/password/reset/<uidb64>/<token>/', password_reset_confirm,
    {'template_name': 'registration/password_reset_confirm.html'},
    name="password_reset_confirm"),
  path('accounts/password/done', password_reset_complete,
    {'template_name': 'registration/password_reset_complete.html'},
    name="password_reset_complete"),
  path('accounts/password/change', password_change,
    {'template_name': 'registration/password_change_form.html'},
    name="password_change_form"),
  path('accounts/password/change/done', password_change_done,
    {'template_name': 'registration/password_change_done.html'},
    name="password_change_done"),
  # admin
  path('admin/', admin.site.urls),
]
