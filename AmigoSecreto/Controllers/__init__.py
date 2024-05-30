from django.http                    import *
from django.shortcuts               import render, redirect as Redirect
from django.views                   import View
from django.contrib.auth            import authenticate as Authenticate, login as Login, logout as Logout
from django.contrib.auth.models     import User
from django.contrib.auth.decorators import login_required as LoginRequired, user_passes_test as UserPassesTest
from django.contrib.auth.hashers    import make_password as MakePassword
from django.utils.decorators        import method_decorator as MethodDecorator
from django.core.mail               import EmailMessage
from django.template.loader         import render_to_string as RenderToString
from django.conf                    import settings as Settings
from django.db                      import transaction as Transaction
from hashlib                        import sha256 as Sha256
from AmigoSecreto.Models            import *
from AmigoSecreto.Forms             import *
from os                             import environ as Environ
from AmigoSecreto.Utils             import SortearSemRestricoes, SortearComRestricoes, RenderStaticFilesInline
from typing                         import Any

Erro:     str = "Ops! Você tentou acessar uma página privada sem fazer login. Logue primeiro."
LoginURL: str = "/login?error=" + Erro

class TiposDeUsuarios:
    Admin           = 1
    AdminGrupo      = 2
    Participante    = 3

@RenderStaticFilesInline
def Render(request: HttpRequest, template_name: str, context: dict[str, Any], cssSources: list[str], jsSources: list[str], *a, **kw) -> HttpResponse:
    ctx         = context.copy()
    ctx["CSS"]  = cssSources
    ctx["JS"]   = jsSources

    return render(request, template_name, ctx, *a, **kw)

from .AppControllers   import AppController, CriarGrupoController, EditarUsuarioController
from .LoginControllers import IndexController, LoginController, RecuperarSenhaController, CadastrarController, RedefinirSenhaController, LogoutController
from .GrupoControllers import EditarGrupoController, GrupoIndexController, AdicionarParticipanteController, AdicionarRestricaoController
