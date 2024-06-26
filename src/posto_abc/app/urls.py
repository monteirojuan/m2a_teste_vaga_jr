from django.urls import path
from posto_abc.app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("relatorio", views.abastecimento_report, name="relatorio"),
]
