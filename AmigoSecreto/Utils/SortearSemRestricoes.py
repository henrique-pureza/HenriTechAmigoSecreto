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
    """
    ### SortearSemRestricoes

    Faz um sorteio de Amigo Secreto.

    :param participantes (list) - Uma lista de strings com o nome dos participantes do sorteio.

    :return (dict[str, str]) - Um dicionário cujas chaves são os presenteadores e os valores, os presenteados.
    """

    sorteio = {}

    participantes_iterable = participantes.copy()

    for presenteador in participantes:
        presenteado = choice(participantes_iterable)

        while presenteado == presenteador:
            presenteado = choice(participantes_iterable)

        sorteio[presenteador] = presenteado
        participantes_iterable.remove(presenteado)

    return sorteio
