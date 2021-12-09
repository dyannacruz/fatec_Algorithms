#Autora: Dyanna Cruz 

#Utilizando list comprehension, construir código em Python para gerar uma lista com os trinta primeiros números ímpares.

#Solução para os 30 primeiros números
import math
def impar(k):
    return [x for x in range(0, k) if x%2 != 0]
print(impar(61))
