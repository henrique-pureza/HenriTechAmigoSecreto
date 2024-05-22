from AmigoSecreto.Controllers import *

class GrupoIndexController(View):
    def get(self, request: HttpRequest, id: int, *a, **kw) -> HttpResponse:
        perfil          = Perfil        .objects  .filter(usuario=request.user)                                             .first()
        grupo           = Grupo         .objects  .filter(id=id)                                                            .first()
        participantes   = Participante  .objects  .filter(grupo__id=id).select_related("usuario__perfil").order_by("tipo")  .all()
        usuario_logado  = Participante  .objects  .filter(usuario__id=request.user.id)                                      .first()
        error           = request.GET             .get("error")

        participantes = list(participantes)
        if usuario_logado.tipo == 2 and len(participantes) > 1:
            participantes.remove(usuario_logado)
            participantes.insert(0, usuario_logado)
        else:
            i = 0
            for participante in participantes:
                old_i = participantes.index(participante)

                if participante.tipo == 2:
                    participantes.insert(i, participante)
                    participantes.pop(old_i + 1)

                    i += 1

        return Render(
            request,
            "Grupo/Index.html",
            {
                "grupo": grupo,
                "participantes": participantes,
                "usuario_logado": usuario_logado,
                "header_com_link": True,
                "perfil": perfil,
                "error": error
            }
        )

    def post(self, request: HttpRequest, id: int, *a, **kw) -> HttpResponseRedirect:
        action          = request.POST.get("action")
        participante_id = request.POST.get("participante")

        if action == "promover_admin":
            participante        = Participante.objects.filter(id=participante_id).first()
            participante.tipo   = 2
            participante.save()
        elif action == "remover_admin":
            participante        = Participante.objects.filter(id=participante_id).first()
            participante.tipo   = 3
            participante.save()
        elif action == "deletar_participante":
            participante        = Participante.objects.filter(id=participante_id).first()
            participante.delete()
        elif action == "sair_do_grupo":
            participante = Participante.objects.filter(usuario=request.user).first()

            if participante.tipo == 2:
                admins = Participante.objects.filter(grupo__id=id, tipo=2).all()

                if len(admins) == 1:
                    erro = "Erro: você é o único administrador desse sorteio. Promova alguém a admin e depois saia."
                    return Redirect("/grupo/" + str(id) + "?error=" + erro)
                else:
                    participante.delete()
                    return Redirect("/app/")
            else:
                participante.delete()
                return Redirect("/app/")
        elif action == "sortear":
            grupo           = Grupo         .objects  .filter(id=id)                                           .first()
            participantes   = Participante  .objects  .filter(grupo__id=id).select_related("usuario__perfil")  .all()

        return Redirect("/grupo/" + str(id))
