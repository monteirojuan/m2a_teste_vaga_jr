from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class Combustivel(models.TextChoices):
    GASOLINA = "GAS", _("Gasolina")
    DIESEL = "DIE", _("Diesel")


class Tanque(models.Model):
    combustivel = models.CharField(max_length=3, choices=Combustivel)
    capacidade = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_atual = models.DecimalField(max_digits=10, decimal_places=2)
    preco_litro = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Tanque {self.id} - Combustível: {Combustivel(self.combustivel).label}, Capacidade: {self.quantidade_atual}L de {self.capacidade}L"


class Bomba(models.Model):
    tanque = models.ForeignKey(Tanque, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Bomba {self.id} - Combustível: {Combustivel(self.tanque.combustivel).label}"


class Abastecimento(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    bomba = models.ForeignKey(Bomba, on_delete=models.DO_NOTHING)
    combustivel = models.CharField(max_length=3, choices=Combustivel)
    litros = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(limit_value=0.01)],
    )
    imposto = models.IntegerField(
        validators=[
            MinValueValidator(limit_value=0),
            MaxValueValidator(limit_value=100),
        ],
    )
    valor_combustivel = models.DecimalField(max_digits=10, decimal_places=2)
    valor_imposto = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        # Durante a criação, no Admin, a data pode ser None.
        if self.data is None:
            return "Abastecimento"

        return f"Abastecimento: R$ {self.valor_total} ({self.bomba})"

    def combustivel_str(self):
        return Combustivel(self.combustivel).label
