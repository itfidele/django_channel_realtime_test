from django.urls import path
from .consumers import WSConsumer

ws_urlpatterns =[
    path('ws/integer/',WSConsumer.as_asgi())
]