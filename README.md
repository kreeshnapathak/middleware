# middleware
This is middleware config for accessing request and user in models, signals.
Donot forget to add this middleware in your settings middileware.

To use this:
from src.apps.notification import middlewares
# Get the current request object:
request = middlewares.get_current_request()
# You can get the current user directly with:
user = middlewares.get_current_user()
