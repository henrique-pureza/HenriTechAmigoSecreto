from django.contrib.admin   import *
from .Models                import *

class ParticipanteAdmin(ModelAdmin):
    list_filter = ("grupo__nome", "tipo")

site.register(Perfil)
site.register(Grupo)
site.register(Participante, ParticipanteAdmin)
site.register(Restricao)
site.register(Sorteio)
