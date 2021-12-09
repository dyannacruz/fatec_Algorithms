#Autora: Dyanna Cruz 

# Exercício 1: Exercício 1: Escrever código Python para testar os valores das variáveis A à F na tabela e mostraros resultados no
# console, para a expressão: Inserir os valores pelo console.

#Definindo variáveis
print("*" * 20, "variáveis de A a F","*" * 20)
A1 = float(input("Digite o valor de A1: "))
B1 = float(input("Digite o valor de B1: "))
C1 = input("Digite o valor de C1: ")
D1 = float(input("Digite o valor de D1: "))
E1 = float(input("Digite o valor de E1: "))
F1 = input("Digite o valor de F1: ")

A2 = float(input("Digite o valor de A2: "))
B2 = float(input("Digite o valor de B2: "))
C2 = input("Digite o valor de C2: ")
D2 = float(input("Digite o valor de D2: "))
E2 = float(input("Digite o valor de E2: "))
F2 = input("Digite o valor de F2: ")

A3 = float(input("Digite o valor de A3: "))
B3 = float(input("Digite o valor de B3: "))
C3 = input("Digite o valor de C3: ")
D3 = float(input("Digite o valor de D3: "))
E3 = float(input("Digite o valor de E3: "))
F3 = input("Digite o valor de F3: ")

A4 = float(input("Digite o valor de A4: "))
B4 = float(input("Digite o valor de B4: "))
C4 = input("Digite o valor de C4: ")
D4 = float(input("Digite o valor de D4: "))
E4 = float(input("Digite o valor de E4: "))
F4 = input("Digite o valor de F4: ")

#Exibição
print("_" * 70)
print("\n                               Variáveis")
print("_" * 70)
print("        A          B          C          D          E          F")
print("_" * 70)
print("\n     ", A1,"      ", B1,"      ", C1,"      ", D1,"      ", E1,"      ",  F1)
print("\n    ", A2,"     ", B2,"     ", C2,"    ", D2,"    ", E2,"     ",  F2)    
print("\n     ", A3,"      ", B3,"      ", C3,"      ", D3,"      ", E3,"      ",  F3)
print("\n     ", A4,"      ", B4,"      ", C4,"     ", D4,"     ", E4,"      ",  F4)
print("_" * 70)

#Resultado da equação
print("_" * 70)
Resultado1 = A1 <= B1 or not C1 or D1 > E1 and F1
Resultado2 = A2 <= B2 or not C2 or D2 > E2 and F2
Resultado3 = A3 <= B3 or not C3 or D3 > E3 and F3
Resultado4 = A4 <= B4 or not C4 or D4 > E4 and F4

#Exibição
print("\n                          Resultados")
print("_" * 70)
print("               1:", Resultado1, "   2:", Resultado2, "   3:", Resultado3,"   4:", Resultado4)
print("_" * 70)