from AmigoSecreto.Forms import *

class EditarUsuarioForm(Form):
    nome_usuario = CharField(
        required=False,
        label="Nome de usuário (o nome que aparecerá nos sorteios)",
        widget=TextInput({
            "class": "form-control",
            "autocomplete": "off",
            "spellcheck": "false"
        })
    )

    senha = CharField(
        required=False,
        widget=PasswordInput({
            "class": "form-control",
            "placeholder": "A senha não é exibida aqui por motivos de segurança",
            "autocomplete": "new-password",
            "spellcheck": "false"
        })
    )

    foto = ImageField(
        required=False,
        widget=FileInput({
            "class": "form-control",
            "autocomplete": "off",
            "spellcheck": "false"
        })
    )
