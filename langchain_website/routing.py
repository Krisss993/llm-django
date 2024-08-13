from django.urls import re_path  
from langchain_stream import views as v1
from chat import views as v2

websocket_urlpatterns = [  
    re_path(r'ws/chat/$', v1.ChatConsumer.as_asgi()),
    re_path(r'wx/chat/$', v2.ChatConsumer.as_asgi()), 
]