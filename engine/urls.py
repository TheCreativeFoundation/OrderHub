from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('order/complete', views.CompleteOrderView.as_view()),
    path('order/send', views.SendOrderView.as_view()),
    path('/order/send/success', views.SendOrderSuccessView.as_view()),
    path('/order/send/failed', views.SendOrderFailedView.as_view()),
    
]