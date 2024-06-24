from django.db import models
from django.utils.translation import gettext_lazy as _


class Combustivel(models.TextChoices):
    GASOLINA = "GAS", _("Gasolina")
    DIESEL = "DIE", _("Diesel")


class Tanque(models.Model):
    combustivel = models.CharField(max_length=3, choices=Combustivel)
    capacidade = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_atual = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Tanque {self.id} - Combustível: {Combustivel(self.combustivel).label}, Capacidade: {self.quantidade_atual}L de {self.capacidade}L"


class Bomba(models.Model):
    tanque = models.ForeignKey(Tanque, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Bomba {self.id} - Combustível: {Combustivel(self.tanque.combustivel).label}"
