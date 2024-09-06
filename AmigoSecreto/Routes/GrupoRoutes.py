from django.urls                import path as Path
from AmigoSecreto.Controllers   import *

urlpatterns = [
    Path("<int:id>/",                           GrupoIndexController.as_view(), name="grupo"),
    Path("<int:id>/editar/",                    EditarGrupoController.as_view(), name="editar_sorteio"),
    Path("<int:id>/adicionar_participante/",    AdicionarParticipanteController.as_view(), name="adicionar_participante"),
    Path("<int:id>/adicionar_restricao/",       AdicionarRestricaoController.as_view(), name="adicionar_restricao"),
    Path("<int:id>/meu_amigo/",                 MeuAmigoController.as_view(), name="meu_amigo")
]
