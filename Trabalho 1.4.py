#Autora: Dyanna Cruz  

# Exercício 4: Um desenvolvedor de software para uma estação meteorológica tem que fazer a leitura das seguintes variáveis,
#  para o dia corrente e dar previsões para o dia seguinte, conforme as condições: - variáveis:
#→ Temperatura;
#→ Umidade Relativa do Ar; -
#condições:
#Se (Temperatura ≥ 28ºC e Umidade Relativa do Ar ≥ 50%)
#Previsão: “irá chover amanhã”;
#Senão
#Previsão: “amanhã o dia será sem chuvas”;
#- Escrever código em Python para ler as variáveis, mostrar os seus valores no console; -
#Mostrar a previsão do tempo para o dia seguinte, simulando algumas possibilidades.


print("*" * 8, "Como estará o tempo?", "*" * 8)
Temperatura = float(input("Digite a temperatura: "))
Umidade_relativa_do_ar = float(input("Digite a umidade relativa do ar: "))

#Exibição
print("_" * 40)
print("Temperatura: ", Temperatura)
print("\nUmidade relativa do ar", Umidade_relativa_do_ar)
print("_" * 40)
print("\nPrevisão do tempo:")
if Temperatura >= 28 and Umidade_relativa_do_ar >= 50:
    print("\nIrá chover amanhã")
else:
    print("Amanhã o dia será sem chuvas")
print("_" * 40)
