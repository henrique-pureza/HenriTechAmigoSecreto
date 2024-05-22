from AmigoSecreto.Models import *

class Sorteio(Model):
    grupo        = ManyToManyField ( Grupo,             related_name="sorteio_grupo"                           )
    presenteador = ForeignKey      ( User,  null=False, related_name="sorteio_presenteador", on_delete=CASCADE )
    presenteado  = ForeignKey      ( User,  null=False, related_name="sorteio_presenteado",  on_delete=CASCADE )

    def __str__(self):
        return f"{self.presenteador.username} tirou {self.presenteado.username}"
