from django import forms
from posto_abc.app.models import Abastecimento


class AbastecimentoReportForm(forms.Form):
    abastecimentos = Abastecimento.objects
