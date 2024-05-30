from AmigoSecreto.Forms import *

class LoginForm(Form):
    email = CharField(
        required=True,
        widget=TextInput({
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
