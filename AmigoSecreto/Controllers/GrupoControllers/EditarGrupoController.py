from AmigoSecreto.Controllers import *

@MethodDecorator(LoginRequired(login_url=LoginURL), "get")
class EditarGrupoController(View):
    def get(self, request: HttpRequest, id: int, *a, **kw) -> HttpResponse:
        sorteio = Grupo.objects.filter(id=id).first()
        form    = EditarGrupoForm(instance=sorteio)
        perfil  = Perfil.objects.filter(usuario=request.user).first()

        return Render(
            request,
            "Grupo/EditarSorteio.html",
            {
                "form": form,
                "header_com_link": True,
                "perfil": perfil,
                "grupo": sorteio
            }
        )

    def post(self, request: HttpRequest, id: int, *a, **kw) -> HttpResponseRedirect:
        sorteio = Grupo.objects.filter(id=id).first()
        form    = EditarGrupoForm(request.POST, request.FILES, instance=sorteio)

        if form.is_valid():
            form.save()

            return Redirect("/grupo/" + str(sorteio.id))
