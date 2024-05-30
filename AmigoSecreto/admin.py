from django.contrib.admin   import *
from .Models                import *

class PerfilAdmin(ModelAdmin):
    search_fields = "usuario", "token"

    fieldsets = [
        [
            "Perfil", {
                "fields": ("foto",),
            }
        ],
        [
            "Recuperação de senha", {
                "fields": ("token",),
                "classes": ("collapse",)
            }
        ]
    ]

class GrupoAdmin(ModelAdmin):
    list_display        = "nome", "endereco_", "preco_min_", "preco_max_", "data_hora_sorteio_"
    list_display_links  = "nome", "endereco_", "preco_min_", "preco_max_", "data_hora_sorteio_"
    list_filter         = "endereco", "preco_min", "preco_max", "data_hora_sorteio"
    readonly_fields     = "usuario_criador",
    search_fields       = "nome", "endereco", "preco_min", "preco_max", "data_hora_sorteio"

    endereco_ = lambda self, grupo: grupo.endereco
    endereco_.short_description = "Endereço"

    preco_min_ = lambda self, grupo: grupo.preco_min
    preco_min_.short_description = "Preço mínimo"

    preco_max_ = lambda self, grupo: grupo.preco_max
    preco_max_.short_description = "Preço máximo"

    data_hora_sorteio_ = lambda self, grupo: grupo.data_hora_sorteio
    data_hora_sorteio_.short_description = "Data e hora do sorteio"

    fieldsets = [
        [
            "Informações básicas", {
                "fields": ("nome", "endereco", "preco_min", "preco_max", "data_hora_sorteio", "banner")
            }
        ],
        [
            "Usuário criador", {
                "fields": ("usuario_criador",),
            }
        ]
    ]

class ParticipanteAdmin(ModelAdmin):
    list_display        = "usuario_", "grupo", "tipo", "nao_pode_presentear_alguem_"
    list_display_links  = "usuario_", "grupo", "tipo", "nao_pode_presentear_alguem_"
    list_filter         = "usuario", "grupo", "tipo", "nao_pode_presentear_alguem"
    readonly_fields     = "usuario", "grupo"
    search_fields       = "usuario", "grupo", "tipo"

    usuario_ = lambda self, participante: participante.usuario
    usuario_.short_description = "Usuário"

    nao_pode_presentear_alguem_ = lambda self, participante: participante.nao_pode_presentear_alguem
    nao_pode_presentear_alguem_.short_description = "Não pode presentear alguém"

    fieldsets = [
        [
            None, {
                "fields": ("grupo",)
            }
        ],
        [
            "Tipo de participante e restrições", {
                "fields": ("tipo", "nao_pode_presentear_alguem")
            }
        ]
    ]

class RestricaoAdmin(ModelAdmin):
    list_display        = "presenteador", "presenteado", "grupo"
    list_display_links  = "presenteador", "presenteado", "grupo"
    list_filter         = "grupo__nome", "presenteador__usuario__username", "presenteado__usuario__username"
    readonly_fields     = "grupo",
    search_fields       = "grupo__nome", "presenteador__usuario__username", "presenteado__usuario__username"

    fieldsets = [
        [
            None, {
                "fields": ("grupo",)
            }
        ],
        [
            "Quem não pode presentear quem", {
                "fields": ("presenteador", "presenteado")
            }
        ]
    ]

class SorteioAdmin(ModelAdmin):
    list_display        = "presenteador", "presenteado", "grupo"
    list_display_links  = "presenteador", "presenteado", "grupo"
    list_filter         = "grupo__nome", "presenteador__usuario__username", "presenteado__usuario__username"
    readonly_fields     = "grupo",
    search_fields       = "grupo__nome", "presenteador__usuario__username", "presenteado__usuario__username"

    fieldsets = [
        [
            None, {
                "fields": ("grupo",)
            }
        ],
        [
            "Quem tirou quem", {
                "fields": ("presenteador", "presenteado")
            }
        ]
    ]

site.register(Perfil, PerfilAdmin)
site.register(Grupo, GrupoAdmin)
site.register(Participante, ParticipanteAdmin)
site.register(Restricao, RestricaoAdmin)
site.register(Sorteio, SorteioAdmin)
