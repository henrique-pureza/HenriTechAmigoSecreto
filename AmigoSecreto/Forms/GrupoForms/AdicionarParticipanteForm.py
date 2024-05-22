from AmigoSecreto.Forms import *

class AdicionarParticipanteForm(Form):
    email = EmailField(
        required=True,
        widget=EmailInput({
            "class": "form-control",
            "autocomplete": "off",
            "spellcheck": "false",
            "id": "email-input"
        })
    )

    nao_pode_presentear_alguem = BooleanField(
        required=False,
        label="Não quero que ele tire alguém",
        widget=CheckboxInput({
            "class": "form-check-input",
            "id": "checkbox-restricao"
        })
    )

    restricao = MultipleChoiceField(
        required=False,
        label="Restrição (segure Ctrl para selecionar mais de 1)",
        widget=SelectMultiple({
            "class": "form-select",
            "id": "select-restricao",
            "style": "display: none;"
        })
    )
