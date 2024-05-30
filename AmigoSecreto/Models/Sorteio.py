from AmigoSecreto.Models import *

class Sorteio(Model):
    grupo        = ForeignKey      ( Grupo,         null=False, related_name="sorteio_grupo"       , on_delete=CASCADE )
    presenteador = ForeignKey      ( Participante,  null=False, related_name="sorteio_presenteador", on_delete=CASCADE )
    presenteado  = ForeignKey      ( Participante,  null=False, related_name="sorteio_presenteado",  on_delete=CASCADE )

    def __str__(self):
        return f"{self.presenteador.usuario.username} tirou {self.presenteado.usuario.username}"
