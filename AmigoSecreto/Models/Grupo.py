from AmigoSecreto.Models import *

class Grupo(Model):
    nome                = CharField     (       null=False, max_length=256,                   )
    endereco            = CharField     (       null=False, max_length=256,                   )
    preco_min           = DecimalField  (       null=False, max_digits=8,   decimal_places=2, )
    preco_max           = DecimalField  (       null=False, max_digits=8,   decimal_places=2, )
    banner              = ImageField    (       null=True,  blank=True                        )
    data_hora_sorteio   = DateTimeField (       null=False                                    )
    usuario_criador     = ForeignKey    ( User, null=True,  on_delete=SET_NULL                )

    def __str__(self):
        return f"{self.nome}"
