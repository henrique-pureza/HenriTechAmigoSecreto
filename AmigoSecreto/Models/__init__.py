from django.db.models           import *
from django.contrib.auth.models import User
from django.db.models.signals   import post_save as PostSave
from django.dispatch            import receiver as Receiver

TIPOS = (
    (1, 'Admin'),
    (2, 'AdminGrupo'),
    (3, 'Participante')
)

from .Perfil        import Perfil
from .Grupo         import Grupo
from .Participante  import Participante
from .Restricao     import Restricao
from .Sorteio       import Sorteio
