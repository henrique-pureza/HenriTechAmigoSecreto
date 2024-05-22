from AmigoSecreto.Forms import *

class CadastrarForm(Form):
    nome_usuario = CharField(
        required=True,
        label="Nome de usuário (o nome que aparecerá nos sorteios)",
        widget=TextInput({
            "class": "form-control",
            "autocomplete": "off",
            "spellcheck": "false"
        })
    )

    email = EmailField(
        required=True,
        widget=EmailInput({
            "class": "form-control",
            "autocomplete": "off",
            "spellcheck": "false"
        })
    )

    senha = CharField(
        required=True,
        widget=PasswordInput({
            "class": "form-control",
            "autocomplete": "off",
            "spellcheck": "false"
        })
    )
