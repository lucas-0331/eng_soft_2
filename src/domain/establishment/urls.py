from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<str:order_items>/<str:username>/", views.OrderView, name="order"),
]
