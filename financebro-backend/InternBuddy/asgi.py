"""
ASGI config for InternBuddy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from uvicorn.workers import UvicornWorker as BaseUvicornWorker


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InternBuddy.settings')

application = get_asgi_application()


class UvicornWorker(BaseUvicornWorker):
    CONFIG_KWARGS = {"loop": "uvloop", "http": "httptools", "lifespan": "off"}
