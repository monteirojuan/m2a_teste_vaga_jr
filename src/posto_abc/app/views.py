from django.shortcuts import render
from posto_abc.app.models import Tanque, Bomba, Abastecimento


def index(request):
    context = {
        "tanques": Tanque.objects.all(),
        "bombas": Bomba.objects.all(),
        "abastecimentos": Abastecimento.objects.all(),
    }
    return render(request, "index.html", context)
