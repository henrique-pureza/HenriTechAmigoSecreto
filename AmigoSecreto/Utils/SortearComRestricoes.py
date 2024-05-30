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
    """
    ### SortearComRestricoes

    Faz um sorteio de Amigo Secreto levando em conta que certas pessoas não podem tirar determinados participantes.

    :param participantes (list) - Uma lista de strings com o nome dos participantes do sorteio.
    :param restricoes (dict[str, list[str]]) - Um dicionário cuja chave é um participante e o valor é uma lista de participantes restritos.

    :return (dict[str, str]) - Um dicionário cujas chaves são os presenteadores e os valores, os presenteados.
    """
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
