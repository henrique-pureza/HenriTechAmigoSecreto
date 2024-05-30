from AmigoSecreto.Forms import *

class AdicionarRestricaoForm(Form):
    presenteado = MultipleChoiceField(
        required=True,
        label="(segure Ctrl para selecionar mais de 1)",
        widget=SelectMultiple({
            "class": "form-select",
            "id": "select-restricao"
        })
    )
