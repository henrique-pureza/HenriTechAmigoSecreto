from random import choice

# participantes = [
#     "Henrique Pureza Queiroz",
#     "Ariel Queiroz Bauer",
#     "Juana Lucho",
#     "Marçal Bauer",
#     "Sinara Rodrigues Pureza",
#     "Alessandra Queiroz Bauer",
#     "Ulysses Queiroz",
#     "Vera Terezinha Lucho Queiroz",
#     "Marina Lucho Queiroz",
#     "Telêmaco Queiroz Júnior",
#     "Yasmin"
# ]

# restricoes = {
#     "Henrique Pureza Queiroz": ["Sinara Rodrigues Pureza", "Telêmaco Queiroz Júnior"],
#     "Ariel Queiroz Bauer": ["Marçal Bauer", "Alessandra Queiroz Bauer", "Yasmin"],
#     "Juana Lucho": ["Ulysses Queiroz", "Marina Lucho Queiroz"],
#     "Marçal Bauer": ["Ariel Queiroz Bauer", "Alessandra Queiroz Bauer"],
#     "Sinara Rodrigues Pureza": ["Henrique Pureza Queiroz", "Telêmaco Queiroz Júnior"],
#     "Alessandra Queiroz Bauer": ["Ariel Queiroz Bauer", "Marçal Bauer"],
#     "Ulysses Queiroz": ["Juana Lucho", "Marina Lucho Queiroz"],
#     "Marina Lucho Queiroz": ["Juana Lucho", "Ulysses Queiroz"],
#     "Telêmaco Queiroz Júnior": ["Henrique Pureza Queiroz", "Sinara Rodrigues Pureza"],
#     "Yasmin": ["Ariel Queiroz Bauer"]
# }

def SortearComRestricoes(participantes: list, restricoes: dict[str, list[str]]) -> dict[str, str]:
    sorteio = {}

    participantes_iterable = participantes.copy()

    for presenteador in participantes:
        if restricoes.get(presenteador):
            presenteados_possiveis = [
                participante
                for participante in participantes_iterable
                if participante not in restricoes.get(presenteador) and participante != presenteador
            ]

            if len(presenteados_possiveis) > 0:
                presenteado = choice(presenteados_possiveis)
                sorteio[presenteador] = presenteado
                participantes_iterable.remove(presenteado)
            else:
                SortearComRestricoes(participantes, restricoes)
        else:
            presenteado = choice(participantes_iterable)

            while presenteado == presenteador:
                presenteado = choice(participantes_iterable)

            sorteio[presenteador] = presenteado
            participantes_iterable.remove(presenteado)

    return sorteio

# sorteio = sortear_com_restricoes(participantes, restricoes)
