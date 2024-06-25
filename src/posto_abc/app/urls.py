from django.urls import path
from src.posto_abc.app import views

urlpatterns = [
    path("", views.index, name="index"),
]
