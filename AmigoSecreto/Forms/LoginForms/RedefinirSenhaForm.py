from AmigoSecreto.Forms import *

class RedefinirSenhaForm(Form):
    nova_senha = CharField(
        required=True,
        label="Nova senha",
        widget=PasswordInput({
            "class": "form-control",
            "autocomplete": "off",
            "spellcheck": "false"
        })
    )
