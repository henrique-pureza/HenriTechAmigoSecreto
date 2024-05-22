from AmigoSecreto.Controllers import *

@MethodDecorator(LoginRequired(login_url=LoginURL), "get")
class EditarUsuarioController(View):
    def get(self, request: HttpRequest, *a, **kw) -> HttpResponse:
        perfil  = Perfil.objects.filter(usuario=request.user).first()
        form    = EditarUsuarioForm()

        return Render(
            request,
            "App/EditarUsuario.html",
            {
                "form": form,
                "header_com_link": True,
                "perfil": perfil
            }
        )

    def post(self, request: HttpRequest, *a, **kw) -> HttpResponseRedirect:
        form = EditarUsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            with Transaction.atomic():
                perfil = Perfil.objects.filter(usuario=request.user).first()

                if form.cleaned_data.get("nome_usuario"):
                    perfil.usuario.username = form.cleaned_data["nome_usuario"]

                if form.cleaned_data.get("senha"):
                    password = MakePassword(form.cleaned_data["senha"])
                    perfil.usuario.password = password

                if form.cleaned_data.get("foto"):
                    perfil.foto = form.cleaned_data["foto"]

                perfil.save()
                perfil.usuario.save()

                if form.cleaned_data.get("senha"):
                    Login(request, perfil.usuario)

        return Redirect("/app/")
