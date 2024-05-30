from AmigoSecreto.Models import *

class Restricao(Model):
    grupo        = ForeignKey ( Grupo,          related_name="restricao_grupo"       , on_delete=CASCADE, null=False)
    presenteador = ForeignKey ( Participante,   related_name="restricao_presenteador", on_delete=CASCADE, null=False)
    presenteado  = ForeignKey ( Participante,   related_name="restricao_presenteado" , on_delete=CASCADE, null=False)

    def __str__(self):
        return f"{self.presenteador.usuario.username} não pode tirar {self.presenteado.usuario.username}"
