# Exercício 3: Para a lista do exercício 2, determinar a dimensão da mesma e mostrar no console os elementos ímpares
# depois da frase ordenada.

ordenada = ['Utilizar o', 'sequenciamento de listas', 'para mostrar', 'no console', 'a seqüência dos',
            'elementos da lista', 'que satisfaça o contexto', 'do significado', 'da frase', 'contida na mesma',
            '(para quem gosta', 'de cinema)']

print(f'A lista tem tamanho = {len(ordenada)}')
for i in range(1, len(ordenada), 2):
    print(f'{i}º elemento: {ordenada[i]}')