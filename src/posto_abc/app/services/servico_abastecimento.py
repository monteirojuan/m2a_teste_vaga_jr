from posto_abc.app.models import Bomba, Abastecimento, Tanque
from decimal import Decimal
from django.db import transaction, models


def criar_abastecimento(bomba_id, litros):
    bomba = Bomba.objects.get(pk=bomba_id)
    with transaction.atomic():
        tanque = Tanque.objects.select_for_update().get(pk=bomba.tanque_id)

        # Não pode reabastecer mais do que tem no tanque
        if tanque.quantidade_atual < Decimal(litros):
            litros = tanque.quantidade_atual

        valor_combustivel = round(Decimal(litros) * tanque.preco_litro, 2)
        valor_imposto = round(valor_combustivel * Decimal(0.13), 2)
        valor_total = round(valor_combustivel + valor_imposto, 2)

        novo_abastecimento = Abastecimento(
            bomba_id=bomba_id,
            combustivel=tanque.combustivel,
            litros=Decimal(litros),
            imposto=13,
            valor_combustivel=valor_combustivel,
            valor_imposto=valor_imposto,
            valor_total=valor_total,
        )

        tanque.quantidade_atual = tanque.quantidade_atual - Decimal(litros)
        tanque.full_clean()
        tanque.save()

        novo_abastecimento.full_clean()
        novo_abastecimento.save()

        return novo_abastecimento


def relatorio_abastecimento(params):  # todo: melhorar exceptions
    query = Abastecimento.objects.order_by("data")

    if ("mes" in params) and ("ano" in params):
        query = query.filter(data__month=params["mes"], data__year=params["ano"])
    elif "ano" in params:
        query = query.filter(data__year=params["ano"])
    else:
        raise Exception

    if "bomba" in params and "tanque" in params:
        raise Exception

    if "bomba" in params:
        query = query.filter(bomba_id=params["bomba"])
    elif "tanque" in params:
        query = query.filter(bomba_id=params["tanque"])

    lista_abastecimentos = query.all()
    valor_total = 0
    if lista_abastecimentos:
        valor_total = lista_abastecimentos.aggregate(models.Sum("valor_total"))[
            "valor_total__sum"
        ]

    return {
        "lista_abastecimentos": lista_abastecimentos,
        "valor_total": round(valor_total, 2),
    }
