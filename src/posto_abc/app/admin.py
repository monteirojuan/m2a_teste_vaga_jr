from django.contrib import admin
from src.posto_abc.app.models import Tanque, Bomba, Abastecimento
from src.posto_abc.app.services.servico_abastecimento import criar_abastecimento


@admin.register(Abastecimento)
class AbastecimentoAdmin(admin.ModelAdmin):
    readonly_fields = [
        "data",
        "combustivel",
        "imposto",
        "valor_combustivel",
        "valor_imposto",
        "valor_total",
    ]

    def save_model(self, request, obj, form, change):
        criar_abastecimento(bomba_id=form.data["bomba"], litros=form.data["litros"])

    def get_form(self, request, obj=None, change=False, **kwargs):
        if obj:
            self.readonly_fields = list(set(self.readonly_fields + ["bomba", "litros"]))
        return super(AbastecimentoAdmin, self).get_form(request, obj, change, **kwargs)


admin.site.register(Tanque)
admin.site.register(Bomba)
