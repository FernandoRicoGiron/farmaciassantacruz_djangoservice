"""
WSGI config for farmacia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

from farmacia.settings import PROJECT_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farmacia.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(PROJECT_DIR, 'static'))
application.add_files(os.path.join(PROJECT_DIR, 'static'), prefix='more-files/')
