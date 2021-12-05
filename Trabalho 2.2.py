#Exercício 2: Construir código Python que mostre no console a tabuada de soma e divisão de um número, utilizando o laço while.

#SOMA
print("_"*35)
print("-"*9, "*Tabuada soma*", "-"*9)
N_Soma = float(input("   Digite o valor da tabuada: "))
print("")
z = 1
while z <= 10:
        print(f"\t{z:^3.1f} \t + \t {N_Soma:1.1f} \t= {N_Soma+z:^1.1f}")
        z = z + 1
print("_"*35)


#DIVISÃO
print("-"*8, "*Tabuada divisão*", "-"*8)
b = float(input("   Digite o valor da tabuada: "))
print("")
a = b
c = 1
while c <= 10:
        print("\t"f" {a:^1.1f} \t: {b:1.1f} \t = {a/b:1.1f}")
        a = a + b
        c = c + 1
print("_"*35)




#SUBTRAÇÃO (ARRUMAR)
print("-"*7, "*Tabuada subtração*", "-"*7)
N_Sub = int(input("   Digite o valor da tabuada: "))
print("")
w = 1
while w <= 10:
        print("\t"f" {w:^1.1f} \t- {N_Sub:1.1f} \t= {w-N_Sub:>1.1f}")
        w = w + 1
print("_"*35)
       
#MULTIPLICAÇÃO
print("-"*5, "*Tabuada multiplicação*", "-"*5)
N_Mult = int(input("   Digite o valor da tabuada: "))
print("")
g = 1
while g <= 10:
        print("\t"f" {g:^1.1f} \tx {N_Mult:1.1f} \t= {g*N_Mult:1.1f}")
        g = g + 1
print("_"*35)