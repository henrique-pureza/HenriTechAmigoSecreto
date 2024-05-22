from AmigoSecreto.Controllers import *

@MethodDecorator(UserPassesTest(lambda user: not user.is_authenticated, "/app"), "get")
class CadastrarController(View):
    def get(self, request: HttpRequest, *a, **kw) -> HttpResponse:
        form = CadastrarForm()

        return Render(
            request,
            "Login/Cadastrar.html",
            {
                "form": form,
                "alert": None,
                "header_com_link": True
            }
        )

    def post(self, request: HttpRequest, *a, **kw) -> (HttpResponse | HttpResponseRedirect):
        form  = CadastrarForm(request.POST)
        alert = None

        if form.is_valid():
            verifyUsernameUsed = User.objects.filter(username   = request.POST["nome_usuario"]) .first()
            verifyEmailUsed    = User.objects.filter(email      = request.POST["email"])        .first()

            if verifyUsernameUsed is not None:
                alert = "Este nome de usuário já está sendo usado."
            elif verifyEmailUsed is not None:
                alert = "Este email já está sendo usado."
            else:
                user = User.objects.create_user(
                    request.POST["nome_usuario"],
                    request.POST["email"],
                    request.POST["senha"]
                )

                if user is None:
                    alert = "Erro ao cadastrar."

        if alert:
            return Render(
                request,
                "Login/Cadastrar.html",
                {
                    "form": form,
                    "alert": alert,
                    "header_com_link": True
                }
            )
        else:
            Login(request, user)
            return Redirect("/app")
