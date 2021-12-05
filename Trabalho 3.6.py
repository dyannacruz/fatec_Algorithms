# Exercício 6: Construir código Python que através de funções, identifique entre três valores numéricos do tipo float,
# a serem inseridos pelo usuário através do console, o menor valor.

def menor_num(a, b, c):
    lista = [a, b, c]
    lista.sort()
    return lista[0]


# Entrada dos números pelo usuário
print('Digite 3 números reais para descobrir o menor:')
x = float(input('1º número: '))
y = float(input('2º número: '))
z = float(input('3º número: '))

# invocando a função
menor = menor_num(x, y, z)

# exibição
print(f'O menor dos 3 números é {menor}')