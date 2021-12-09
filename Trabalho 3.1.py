#Autora: Dyanna Cruz 

# Exercício 1: Criar código Python que inicialize duas listas vazias. Uma delas deverá receber pelo console os nomes relativos a dez alunos de uma escola,
# e a outra lista deverá receber, também pelo console, as notas desses alunos para as disciplinas de História, Matemática, Português, Geografia e Ciências.
# Criar uma função que adicione às listas os nomes e as notas, calculando para cada nome, a média das notas. Se a média for maior igual à cinco, a função 
# deve retornar, através de uma tupla, além do nome do aluno, a variável APROVADO = TRUE; se a média for menor que cinco, deve retornar a tupla com o nome
# e a variável APROVADO = FALSE. Na sequência, fora da função, devem ser impressos os resultados de todos os alunos.

def cad_notas(num_alunos):
    global alunos
    global notas
    resultados = ()
    disciplinas = ['História', 'Matemática', 'Português', 'Geografia', 'Ciências']
    for i in range(num_alunos):
        print('*' * 50)
        alunos.append(input(f'Digite o nome do {i+1}º aluno:\t'))
        sub_notas = []
        media = 0
        for d in disciplinas:
            #print('-' * 50)
            x = (float(input(f'Digite a nota de {d:10}:\t')))
            sub_notas.append(x)
            media += x
        notas.append(sub_notas)
        media /= 5
        if media >= 5:
            resultados = resultados + (alunos[i], True)
        else:
            resultados = resultados + (alunos[i], False)
    return resultados


alunos = []
notas = []
qtdde_alunos = 10

resultado_final = cad_notas(qtdde_alunos)
#print(alunos)
#print(notas)
#print(resultado_final)
print(f'\n\n{" ALUNO ":-^40}{"RESULTADO"}')
for i in range(0, len(resultado_final), 2):
    print(f'{resultado_final[i]:.<40}{"APROVADO" if resultado_final[i+1] else "REPROVADO"}')
print('\n\nFim do Programa!')