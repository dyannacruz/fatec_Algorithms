#Exercício 5: Utilizar a função range( ) para gerar duas listas, uma com os dez primeiros números pares e outra com os dez primeiros números ímpares.
#Gerar uma terceira lista que corresponda a soma dos valores dos elementos correspondentes em cada uma das listas geradas anteriormente.
#Números pares:

list_1 = list(range(2, 22, 2))
list_2 = list(range(1, 21, 2))
print("Pares = ", list_1)
print("Ímpares = ", list_2)
soma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for a in range(10):
    soma[a] = list_1[a] + list_2[a]
print("Pares + Ímpares = ", soma)