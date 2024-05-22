from django.urls                import path as Path
from AmigoSecreto.Controllers   import *

urlpatterns = [
    Path("",                 AppController           .as_view(), name="app"),
    Path("criar_grupo/",     CriarGrupoController    .as_view(), name="criar_grupo"),
    Path("editar_usuario/",  EditarUsuarioController .as_view(), name="editar_usuario")
]
