from django.urls import path
from . import views

urlpatterns = [
    path("gateway/", views.GatewayView.as_view()),
]