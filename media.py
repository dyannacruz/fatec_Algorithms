# Função criada para o "Trabalho 3.7"

def media(aluno, notas):
    nota1 = float(notas[0] * 0.4)
    nota2 = float(notas[1] * 0.6)
    nota_final = float(nota1 + nota2)
    nota_final = str(nota_final)
    msg = "A média do(a) aluno(a) " + aluno + " é " + nota_final
    print(msg)
    return