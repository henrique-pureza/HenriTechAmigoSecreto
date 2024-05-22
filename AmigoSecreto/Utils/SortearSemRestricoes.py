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

def SortearSemRestricoes(participantes: list[str]) -> dict[str, str]:
    sorteio = {}

    participantes_iterable = participantes.copy()

    for presenteador in participantes:
        presenteado = choice(participantes_iterable)

        while presenteado == presenteador:
            presenteado = choice(participantes_iterable)

        sorteio[presenteador] = presenteado
        participantes_iterable.remove(presenteado)

    return sorteio

# sorteio = sortear_sem_restricoes(participantes)
# print(sorteio)
