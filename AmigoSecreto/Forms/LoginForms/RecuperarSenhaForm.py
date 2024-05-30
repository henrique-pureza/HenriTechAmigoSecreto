from AmigoSecreto.Forms import *

class RecuperarSenhaForm(Form):
    email = EmailField(
        required=True,
        widget=EmailInput({
            "class": "form-control",
            "autocomplete": "off",
            "spellcheck": "false"
        })
    )
