from django.shortcuts import render
from .models import Tanque, Bomba, Abastecimento


def index(request):
    context = {
        "tanques": Tanque.objects.all(),
        "bombas": Bomba.objects.all(),
        "abastecimentos": Abastecimento.objects.all(),
    }
    return render(request, "index.html", context)
