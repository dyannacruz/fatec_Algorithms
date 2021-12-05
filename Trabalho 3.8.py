# Exercício 8: Simular através de código Python três jogadas consecutivas de um dado, retornando os valores no console.

from random import randint

print('Resultados dos lançamentos do dado:')
for i in range(3):
    print(f'{i+1}º lançamento =', randint(1, 6))