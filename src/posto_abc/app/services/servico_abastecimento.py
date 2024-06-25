from src.posto_abc.app.models import Bomba, Abastecimento, Tanque
from decimal import Decimal
from django.db import transaction


def criar_abastecimento(bomba_id, litros):
    with transaction.atomic():
        tanque = Tanque.objects.select_for_update().get(pk=bomba_id)

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
