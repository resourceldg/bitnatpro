"""
WSGI config for btn project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
<<<<<<< HEAD

=======
os.environ['HTTPS'] = "on"
>>>>>>> bae9da8043d0f93332068b707af75de1289681da
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btn.settings")

application = get_wsgi_application()
