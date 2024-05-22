from AmigoSecreto.Controllers import *

@MethodDecorator(UserPassesTest(lambda user: not user.is_authenticated, "/app"), "get") # Redireciona para a tela inicial caso o usuário já esteja logado
class IndexController(View):
    def get(self, request: HttpRequest, *a, **kw) -> HttpResponse:
        return Render(request, "Login/Index.html")
