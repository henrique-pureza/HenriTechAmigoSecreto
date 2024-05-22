from AmigoSecreto.Models import *

class Perfil(Model):
    usuario = OneToOneField ( User,           on_delete=CASCADE            )
    foto    = ImageField    ( null=True,      blank=True                   )
    token   = CharField     ( max_length=256, null=True,        blank=True )

    def __str__(self):
        return f"{self.usuario.username}"

    @Receiver(PostSave, sender=User)
    def criar_perfil_para_usuario(sender, instance, created, **kwargs):
        try:
            if created:
                Perfil.objects.create(usuario=instance)
        except:
            pass

    @Receiver(PostSave, sender=User)
    def salvar_perfil_do_usuario(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass
