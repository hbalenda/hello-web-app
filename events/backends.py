from registration.backends.simple.views import RegistrationView

# new registration view, subclassing RegistrationView from the plugin
class MyRegistrationView(RegistrationView):
  # the named URL that we want to redirect to
  success_url = 'registration_create_event'
