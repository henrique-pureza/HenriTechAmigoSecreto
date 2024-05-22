from AmigoSecreto.Controllers import *

@MethodDecorator(UserPassesTest(lambda user: not user.is_authenticated, "/app"), "get")
class RecuperarSenhaController(View):
    def get(self, request: HttpRequest, *a, **kw) -> HttpResponse:
        if request.user.is_authenticated:
            return Redirect("/app")

        form = RecuperarSenhaForm()

        if request.GET.get("error"):
            return Render(
                request,
                "Login/RecuperarSenha.html",
                {
                    "form": form,
                    "alert": request.GET.get("error"),
                    "header_com_link": True
                }
            )
        else:
            return Render(
                request,
                "Login/RecuperarSenha.html",
                {
                    "form": form,
                    "alert": None,
                    "header_com_link": True
                }
            )

    def post(self, request: HttpRequest, *a, **kw) -> HttpResponse:
        form = RecuperarSenhaForm(request.POST)

        if form.is_valid():
            perfil = Perfil.objects.filter(usuario__email=request.POST["email"]).first()

            if perfil is not None:
                try:
                    perfil.token = Sha256().hexdigest()
                    perfil.save()

                    try:
                        mail = EmailMessage(
                            "Recuperar senha - HenriTech Amigo Secreto",
                            RenderToString("Login/RecuperarSenhaMensagem.html", { "token": perfil.token }),
                            Environ.get("EMAIL"),
                            [perfil.usuario.email]
                        )
                        mail.content_subtype = "html"
                        mail.send(False)

                        return Render(
                            request,
                            "Login/RecuperarSenhaSucesso.html",
                            {
                                "header_com_link": True
                            }
                        )
                    except:
                        raise Exception
                except:
                    return Render(
                        request,
                        "Login/RecuperarSenha.html",
                        {
                            "form": form,
                            "alert": "Erro ao enviar o email.",
                            "header_com_link": True
                        }
                    )
