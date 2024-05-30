from AmigoSecreto.Models import *

class Participante(Model):
    usuario                    = ForeignKey   ( User,  null=False,                                        on_delete=CASCADE )
    grupo                      = ForeignKey   ( Grupo, null=False,     related_name="participante_grupo", on_delete=CASCADE )
    tipo                       = IntegerField (        choices=TIPOS,  default=3                                            )
    nao_pode_presentear_alguem = BooleanField (        null=False,     default=False                                        )

    def __str__(self):
        return f"{self.usuario.username}"

    @Receiver(PostSave, sender=Grupo)
    def CriarUsuarioLogadoComoParticipante(sender, instance: Grupo, created, **kw):
        try:
            if created:
                Participante.objects.create(usuario=instance.usuario_criador, grupo=instance, tipo=2)
        except:
            pass
