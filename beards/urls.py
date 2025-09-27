from django.urls import path
from . import views

urlpatterns = [
    path("", views.OrderApi.as_view()),
    
]