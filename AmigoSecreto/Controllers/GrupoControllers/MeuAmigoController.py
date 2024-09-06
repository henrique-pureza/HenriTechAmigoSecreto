from AmigoSecreto.Controllers import *

class MeuAmigoController(View):
    def get(self, request: HttpRequest, id: int, *a, **kw) -> HttpResponse:
        perfil          = Perfil        .objects  .filter(usuario=request.user)                                             .first()
        grupo           = Grupo         .objects  .filter(id=id)                                                            .first()
        usuario_logado  = Participante  .objects  .filter(usuario__id=request.user.id)                                      .first()

        return Render(
            request,
            "Grupo/MeuAmigo.html",
            {
                "grupo": grupo,
                "usuario_logado": usuario_logado,
                "header_com_link": True,
                "perfil": perfil,
            }
        )
