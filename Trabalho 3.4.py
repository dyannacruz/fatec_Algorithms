# Exercício 4: Criar uma função para remover da lista do exercício 2, depois de ordenada, os elementos pares,
# imprimindo-os no console à medida que forem retirados da lista.

def retirada(item, lista):
    usada = lista[:]
    print(f'Elemento retirado: {usada[item]}')
    usada.pop(item)
    return usada

ordenada = ['Utilizar o', 'sequenciamento de listas', 'para mostrar', 'no console', 'a seqüência dos',
            'elementos da lista', 'que satisfaça o contexto', 'do significado', 'da frase', 'contida na mesma',
            '(para quem gosta', 'de cinema)']

for k, v in enumerate(ordenada):
    if k % 2 == 0:
        retirada(k, ordenada)