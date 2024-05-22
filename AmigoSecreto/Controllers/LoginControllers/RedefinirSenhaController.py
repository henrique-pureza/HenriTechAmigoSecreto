from AmigoSecreto.Controllers import *

@MethodDecorator(UserPassesTest(lambda user: not user.is_authenticated, "/app"), "get")
class RedefinirSenhaController(View):
    def get(self, request: HttpRequest, token: str, *a, **kw) -> HttpResponse:
        perfil = Perfil.objects.filter(token=token).first()
        form   = RedefinirSenhaForm()

        if perfil is None:
            alert = "Token inválido. Mande o e-mail novamente."
            return Redirect("/recuperar_senha?error=" + alert)

        return Render(
            request,
            "Login/RecuperarSenhaEmail.html",
            {
                "form": form,
                "header_com_link": True
            }
        )

    def post(self, request: HttpRequest, token: str, *a, **kw) -> HttpResponseRedirect:
        form = RedefinirSenhaForm(request.POST)

        if form.is_valid():
            perfil = Perfil.objects.filter(token=token).first()
            perfil.usuario.set_password(request.POST["nova_senha"])
            perfil.token = None
            perfil.usuario.save()
            perfil.save()

            message = "Senha redefinida com sucesso. Tente fazer login novamente."
            return Redirect("/login?message=" + message)
