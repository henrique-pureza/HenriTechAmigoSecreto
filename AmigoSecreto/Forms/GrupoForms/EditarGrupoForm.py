from AmigoSecreto.Forms import *

class EditarGrupoForm(ModelForm):
    class Meta:
        model   = Grupo
        fields  = "__all__"
        exclude = ["usuario_criador"]

        labels = {
            "endereco": "Endereço",
            "data_hora_sorteio": "Data e hora",
            "preco_min": "Preço mínimo",
            "preco_max": "Preço máximo"
        }

        widgets = {
            "nome": TextInput({
                "class": "form-control",
                "autocomplete": "off",
                "spellcheck": "false"
            }),
            "endereco": TextInput({
                "class": "form-control",
                "autocomplete": "off",
                "spellcheck": "false"
            }),
            "data_hora_sorteio": DateTimeInput({
                "class": "form-control",
                "type": "datetime-local",
                "autocomplete": "off",
                "spellcheck": "false"
            }, "%Y-%m-%dT%H:%M"),
            "preco_min": NumberInput({
                "class": "form-control",
                "min": 0,
                "max": 999999,
                "step": 0.01,
                "autocomplete": "off",
                "spellcheck": "false"
            }),
            "preco_max": NumberInput({
                "class": "form-control",
                "min": 0,
                "max": 999999,
                "step": 0.01,
                "autocomplete": "off",
                "spellcheck": "false"
            }),
            "banner": FileInput({
                "class": "form-control",
                "autocomplete": "off",
                "spellcheck": "false"
            })
        }
