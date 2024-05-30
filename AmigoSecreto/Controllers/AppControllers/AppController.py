from AmigoSecreto.Controllers import *

@MethodDecorator(LoginRequired(login_url=LoginURL), "get") # Só pode acessar se estiver logado
class AppController(View):
    def get(self, request: HttpRequest, *a, **kw) -> HttpResponse:
        perfil      = Perfil.objects.filter(usuario=request.user).first()
        sorteios    = Grupo.objects.filter(participante_grupo__usuario__id=perfil.usuario.id).all()

        return Render(
            request,
            "App/Index.html",
            {
                "header_com_link": True,
                "perfil": perfil,
                "sorteios": sorteios
            }
        )
