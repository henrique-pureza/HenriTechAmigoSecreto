from AmigoSecreto.Controllers import *

@MethodDecorator(UserPassesTest(lambda user: not user.is_authenticated, "/app"), "get")
class LoginController(View):
    def get(self, request: HttpRequest, *a, **kw) -> HttpResponse:
        if request.user.is_authenticated:
            return Redirect("/app")

        form = LoginForm()

        if request.GET.get("message"):
            return Render(
                request,
                "Login/Login.html",
                {
                    "form": form,
                    "message": request.GET.get("message"),
                    "alert": None,
                    "header_com_link": True
                }
            )
        elif request.GET.get("error"):
            return Render(
                request,
                "Login/Login.html",
                {
                    "form": form,
                    "alert": request.GET.get("error"),
                    "message": None,
                    "header_com_link": True
                }
            )
        else:
            return Render(
                request,
                "Login/Login.html",
                {
                    "form": form,
                    "alert": None,
                    "message": None,
                    "header_com_link": True
                }
            )

    def post(self, request: HttpRequest, *a, **kw) -> HttpResponseRedirect:
        form    = LoginForm(request.POST)
        alert   = None

        if form.is_valid():
            user        = User.objects.filter(email=request.POST["email"]).first()
            check_user  = Authenticate(username=user.username, password=request.POST["senha"])

            if user is not None and check_user is not None:
                Login(request, check_user)
            else:
                alert = "Usuário ou senha incorretos."

                return Render(
                    request,
                    "Login/Login.html",
                    {
                        "form": form,
                        "alert": alert,
                        "message": None,
                        "header_com_link": True
                    }
                )

        return Redirect("/app")
