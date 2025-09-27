from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterApi.as_view()),
    path("get-me/", views.GetMeApi.as_view()),
    
]