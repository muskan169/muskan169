"""
WSGI config for Eshop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Eshop.settings")
# os.environ["DJANGO_SETTINGS_MODULE"] = "Eshop.settings"

# from whitenoise import WhiteNoise
# application = WhiteNoise(get_wsgi_application())
application = get_wsgi_application()