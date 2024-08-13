"""
ASGI config for langchain_website project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os  
from django.core.asgi import get_asgi_application  
from channels.routing import ProtocolTypeRouter, URLRouter  
from channels.auth import AuthMiddlewareStack  
import langchain_website.routing  
  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'langchain_website.settings')  
  
application = ProtocolTypeRouter({  
  "http": get_asgi_application(),  
  "websocket": AuthMiddlewareStack(  
        URLRouter(  
            langchain_website.routing.websocket_urlpatterns  
        )  
    ),  
})
