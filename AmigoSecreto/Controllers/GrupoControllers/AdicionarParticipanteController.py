from AmigoSecreto.Controllers import *

class AdicionarParticipanteController(View):
    def get(self, request: HttpRequest, id: int, *a, **kw) -> HttpResponse:
        perfil          = Perfil.objects.filter(usuario=request.user).first()
        grupo           = Grupo.objects.filter(id=id).first()
        participantes   = Participante.objects.filter(grupo__id=id).select_related("usuario__perfil").all()

        restricao_choices = [
            (participante.id, participante.usuario.username)
            for participante in participantes
        ]

        form = AdicionarParticipanteForm()
        form.fields["restricao"].choices = restricao_choices

        return Render(
            request,
            "Grupo/AdicionarParticipante.html",
            {
                "header_com_link": True,
                "perfil": perfil,
                "grupo": grupo,
                "form": form
            }
        )

    def post(self, request: HttpRequest, id: int, *a, **kw) -> HttpResponseRedirect:
        form = AdicionarParticipanteForm(request.POST)
        form.is_valid()
        restricoes_id = form.cleaned_data.get("restricao")

        if form.is_valid():
            grupo   = Grupo.objects.filter(id=id).first()
            perfil  = Perfil.objects.filter(usuario__email=form.cleaned_data.get("email")).first()

            if not perfil:
                return Render(
                    request,
                    "Grupo/AdicionarParticipante.html",
                    {
                        "header_com_link": True,
                        "perfil": Perfil.objects.filter(usuario=request.user).first(),
                        "grupo": grupo,
                        "form": form,
                        "erro": "O email fornecido não é de nenhum usuário existente. Certifique-se de que ele já criou conta no sistema."
                    }
                )

            participante_ja_existe = Participante.objects.filter(grupo=grupo, usuario=perfil.usuario).first()

            if participante_ja_existe:
                return Render(
                    request,
                    "Grupo/AdicionarParticipante.html",
                    {
                        "header_com_link": True,
                        "perfil": Perfil.objects.filter(usuario=request.user).first(),
                        "grupo": grupo,
                        "form": form,
                        "erro": "Você já adicionou um participante com esse email."
                    }
                )

            with Transaction.atomic():
                novo_participante                               = Participante()
                novo_participante.usuario                       = perfil.usuario
                novo_participante.grupo                         = grupo

                if form.cleaned_data.get("nao_pode_presentear_alguem"):
                    novo_participante.nao_pode_presentear_alguem = True

                novo_participante.save()

                restricoes_id = form.cleaned_data.get("restricao")

                if restricoes_id:
                    for restricao_id in restricoes_id:
                        presenteado = Perfil.objects.filter(id=restricao_id).first()

                        nova_restricao              = Restricao()
                        nova_restricao.grupo        .add(grupo)
                        nova_restricao.presenteador .add(perfil.usuario)
                        nova_restricao.presenteado  .add(presenteado.usuario)

                        nova_restricao.save()


        return Redirect("/grupo/" + str(id))
