from AmigoSecreto.Controllers import *

@MethodDecorator(LoginRequired(login_url=LoginURL), "get")
class CriarGrupoController(View):
    def get(self, request: HttpRequest, *a, **kw) -> HttpResponse:
        form    = CriarGrupoForm({ "usuario_criador": request.user })
        perfil  = Perfil.objects.filter(usuario=request.user).first()

        return Render(
            request,
            "App/CriarSorteio.html",
            {
                "form": form,
                "header_com_link": True,
                "perfil": perfil
            }
        )

    def post(self, request: HttpRequest, *a, **kw) -> HttpResponseRedirect:
        form = CriarGrupoForm(request.POST, request.FILES)

        if form.is_valid():
            grupo: Grupo = form.save()

            return Redirect("/grupo/" + str(grupo.id))
