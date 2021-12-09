#Autora: Dyanna Cruz 

# Criar arquivo módulo Python com uma função que recebe como argumentos os nomes de 6 alunos de uma lista e os respectivos valores das notas de“Algoritmos
# e Introdução a Computação”, retornando as médias dos mesmos na disciplina. Na aplicação que chama a função do módulo é retornado no console os alunos e
# suas respectivas médias. Considerar o tratamento de exceções para eventuais erros que ocorram na inserção de dados ou nos cálculos.

import sys
sys.path.append('C:/Users/dyann/OneDrive/DYANNA/FATEC/1º SEMESTRE/05 - Algoritmos e Introdução à Computação/Trabalho')
import media

alunos = []
notas = []
novos_alunos = 0
while novos_alunos < 1:
	nome = input("Insira o nome do(a) aluno(a): ")
	if len(nome) == 0:
		print("Por favor insira o nome do aluno")
		exit()
	else:
		alunos.append(nome)

	try:
		nota1_value = float(input("Insira a primeira nota: "))
		if (nota1_value < 0 or nota1_value > 10):
			print("Por favor insira as notas corretamente")
			exit()
		notas.append(nota1_value)

		nota2_value = float(input("Insira a segunda nota: "))
		if (nota2_value < 0 or nota2_value > 10):
			print("Por favor insira as notas corretamente")
			exit()
		notas.append(nota2_value)

	except ValueError:
		print("Por favor insira as notas corretamente")
		exit()

	novo_aluno = input("Deseja incluir um novo aluno? [S/N]")
	if novo_aluno == "S":
		novos_alunos = 0
	else:
		novos_alunos = 1

notas_agrupadas = [notas[i:i + 2] for i in range(0, len(notas), 2)]

a = len(alunos)
i = 0
while i < a:
	media.media(alunos[i],notas_agrupadas[i])
	i = i + 1