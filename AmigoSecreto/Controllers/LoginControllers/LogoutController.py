from AmigoSecreto.Controllers import *

class LogoutController(View):
    def get(self, request: HttpRequest, *a, **kw) -> HttpResponseRedirect:
        Logout(request)
        return Redirect("/login")
