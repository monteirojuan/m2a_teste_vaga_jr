from django.shortcuts import render
from posto_abc.app.models import Tanque, Bomba, Abastecimento
from posto_abc.app.services import servico_abastecimento


def index(request):
    context = {
        "tanques": Tanque.objects.all(),
        "bombas": Bomba.objects.all(),
        "abastecimentos": Abastecimento.objects.all(),
    }
    return render(request, "index.html", context)


def abastecimento_report(request):
    context = servico_abastecimento.relatorio_abastecimento(request.GET)
    # todo: transformar em pdf
    return render(request, "relatorio.html", context)
