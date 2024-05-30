from AmigoSecreto.Controllers import *

class AdicionarRestricaoController(View):
    def get(self, request: HttpRequest, id: int, *a, **kw) -> HttpResponse:
        presenteador_id = request.GET.get("presenteador")

        perfil          = Perfil.objects.filter(usuario=request.user).first()
        grupo           = Grupo.objects.filter(id=id).first()
        participantes   = Participante.objects.filter(grupo__id=id).select_related("usuario__perfil").all()
        presenteador    = Participante.objects.filter(id=presenteador_id).first()

        restricao_choices = [
            (participante.id, participante.usuario.username)
            for participante in participantes
            if participante != presenteador
        ]

        form = AdicionarRestricaoForm()
        form.fields["presenteado"].choices = restricao_choices

        return Render(
            request,
            "Grupo/AdicionarRestricao.html",
            {
                "header_com_link": True,
                "perfil": perfil,
                "grupo": grupo,
                "form": form,
                "presenteador": presenteador
            }
        )

    def post(self, request: HttpRequest, id: int, *a, **kw) -> HttpResponseRedirect:
        grupo         = Grupo.objects.filter(id=id).first()
        presenteador  = Participante.objects.filter(id=request.GET.get("presenteador")).first()

        print(request.POST)

        return Redirect("/grupo/" + str(id))
