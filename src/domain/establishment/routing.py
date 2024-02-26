from django.urls import path
from .consumers import OrderConsumer

websocket_urlpatterns = [
    path("ws/notification/<str:order_items>/", OrderConsumer.as_asgi()),
]
