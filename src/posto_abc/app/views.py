from django.shortcuts import render
from .models import Tanque, Bomba


def index(request):
    context = {
        "tanques": Tanque.objects.all(),
        "bombas": Bomba.objects.all(),
    }
    return render(request, "index.html", context)
