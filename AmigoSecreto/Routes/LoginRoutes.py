from django.urls                 import path as Path
from AmigoSecreto.Controllers    import *

urlpatterns = [
    Path("",                                    IndexController             .as_view(),         name="index"),
    Path("login/",                              LoginController             .as_view(),         name="login"),
    Path("logout/",                             LogoutController            .as_view(),         name="logout"),
    Path("cadastrar/",                          CadastrarController         .as_view(),         name="cadastrar"),
    Path("recuperar_senha/",                    RecuperarSenhaController    .as_view(),         name="recuperar_senha"),
    Path("recuperar_senha_email/<str:token>/",  RedefinirSenhaController    .as_view(),         name="redefinir_senha")
]

