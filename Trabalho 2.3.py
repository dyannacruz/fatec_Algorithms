#Exercício 3: Dado um teste de múltipla escolha com cinco questões, onde cada questão vale 1 ponto e as respostas corretas são: 
#questão 1 = C, questão 2 = D, questão 3 = B, questão 4 = A e questão 5 = E. Escrever código Python que leia a resposta de cada 
#questão inserida por um usuário e retorne o total de pontos do mesmo. Utilizar o laço while.

#Respostas Corretas
RespCorretas = ["C","D","B","A","E"]
#Respostas do Usuário
RespUser = [] 
RespTotal = len(RespCorretas)
Q = 1
while len(RespUser) < RespTotal:
    Pergunta = "Digite a sua resposta para a pergunta " + format(Q) + ": "
    resp = input(Pergunta)
    RespUser.append(resp)
    Q = Q + 1
#Comparando as respostas do usuário com as respostas corretas
Pontos = 0
Loop = 0
while Loop < len(RespCorretas):
    if RespUser[Loop].lower() == RespCorretas[Loop].lower(): Pontos = Pontos + 1
    Loop = Loop + 1
#Resultado final
print ("Você fez", Pontos, "ponto(os).")