# healthapp/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'serverprojet.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Add your WebSocket routing here if needed
})
AUTH_USER_MODEL = 'accounts.CustomUser'
