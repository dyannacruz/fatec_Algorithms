# Exercício 2: Escrever código Python para ler através do console as variáveis: “funcionário”, o nome do funcionário de uma empresa;
# “idade”, a idade do funcionário; “endereço”, o endereço do funcionário; a variável “função”, o cargo do funcionário e a variável 
# “salário”, o valor do seu salário. Utilizar o comando print para mostrar os resultados no console. Reajustar o salário lido em 20% 
# e mostrar o seu valor atualizado no console.

#Definindo variáveis
print("-" * 8, "Cálculo de Reajuste do Salário:","-" * 8)
Nome = input("Digite seu nome: ")
Endereco = input("Digite seu endereço: ")
Funcao = input("Digite a sua função: ")
Salario = float(input("Digite o valor do salário: R$ "))

#Exibição
print("_" * 50)
print("Nome: ", Nome)
print("Endereço: ", Endereco)
print("Função: ", Funcao)
print("Salário = R$ ", Salario)

#Resultado
print("_" * 50)
print("                   Resultado")
Reajuste_salario = Salario*0.20 + Salario
print("\nReajuste Salário = R$ ", Reajuste_salario)
print("_" * 50)