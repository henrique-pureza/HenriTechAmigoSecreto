from AmigoSecreto.Models import *

class Restricao(Model):
    grupo        = ManyToManyField ( Grupo, related_name="restricao_grupo"        )
    presenteador = ManyToManyField ( User,  related_name="restricao_presenteador" )
    presenteado  = ManyToManyField ( User,  related_name="restricao_presenteado"  )

    def __str__(self):
        return f"{self.presenteador.username} não pode tirar {self.presenteado.username}"
