#Exercício 1: Construir código em Python que possa calcular a média aritmética do aluno selecionado
#e retornar no console se o mesmo está aprovado (média >= 5.0) ou reprovado. Mostrar no console todas
#as notas do aluno selecionado → utilizar elif para selecionar o aluno.

#            História  Geografia   Português  Matemática  Ciências  Literatura
#Aluno
#Maria         5.6       6.7         7.0         10.0        4.0        8.0
#Tânia         2.3       6.6         8.0         5.5        10.0        5.0
#José          7.7       4.0         7.0         7.9         2.2        6.5
#Daniel        9.0      10.0         3.3         8.0         6.0        4.6

#Notas das disciplinas por aluno
#Maria
Maria_Historia = 5.6
Maria_Geografia = 6.7
Maria_Portugues = 7.0
Maria_Matematica = 10.0
Maria_Ciencias = 4.0
Maria_Literatura = 8.0
#Tania
Tania_Historia = 2.3
Tania_Geografia = 6.6
Tania_Portugues = 8.0
Tania_Matematica = 5.5
Tania_Ciencias = 10.0
Tania_Literatura = 5.0
#Jose
Jose_Historia = 7.7
Jose_Geografia = 4.0
Jose_Portugues = 7.0
Jose_Matematica = 7.9
Jose_Ciencias = 2.2
Jose_Literatura = 6.5
#Daniel
Daniel_Historia = 9.0
Daniel_Geografia = 10.0
Daniel_Portugues = 3.3
Daniel_Matematica = 8.0
Daniel_Ciencias = 6.0
Daniel_Literatura = 4.6

#Exibição
Media_Maria = ((Maria_Historia + Maria_Geografia + Maria_Portugues + Maria_Matematica + Maria_Ciencias + Maria_Literatura) /6)
Media_Tania = ((Tania_Historia + Tania_Geografia + Tania_Portugues + Tania_Matematica + Tania_Ciencias + Tania_Literatura) /6)
Media_Jose = ((Jose_Historia + Jose_Geografia + Jose_Portugues + Jose_Matematica + Jose_Ciencias + Jose_Literatura) /6)
Media_Daniel = ((Daniel_Historia + Daniel_Geografia + Daniel_Portugues + Daniel_Matematica + Daniel_Ciencias + Daniel_Literatura) /6)

#Menu
print("-"*27, "*Lista de alunos*", "-"*27)
print("\t" * 4, "1 = Maria", "2 = Tânia", "3 = José", "4 = Daniel")

Aluno = int(input("\t\t\t\t\t\t""Digite o número do aluno: "))
if Aluno >= 5:
    print("\n", "\t "*5, "Este aluno não consta na lista")
    
print("_"*72) 
if Aluno == 1:
    print("\t"*7, "Disciplinas")
    print("\nHistória""\t""Geografia""\t""Português""\t""Matemática""\t""Ciências""\t""Literatura")
    print("\t", Maria_Historia,"\t\t", Maria_Geografia,"\t\t", Maria_Portugues,"\t\t", Maria_Matematica,"\t\t", Maria_Ciencias,"\t\t ", Maria_Literatura)
    print("_"*72)
    print("\t "*6, f" Média =: {Media_Maria:1.2f}")
    if Media_Maria >= 5:
        print ("\n", "\t"*6, "Aluno(a) aprovado(a)")
        print("_"*72) 
elif Aluno == 2 and Media_Tania >= 5:
    print("\t"*7, "Disciplinas")
    print("\nHistória""\t""Geografia""\t""Português""\t""Matemática""\t""Ciências""\t""Literatura")
    print("\t",Tania_Historia,"\t\t",Tania_Geografia,"\t\t",Tania_Portugues,"\t\t ",Tania_Matematica,"\t  ",Tania_Ciencias,"\t\t ",Tania_Literatura)
    print("_"*72) 
    print("\t "*6, f" Média =: {Media_Tania:1.2f}")
    if Media_Tania >= 5:
        print ("\n", "\t"*6, "Aluno(a) aprovado(a)")
        print("_"*72) 
elif Aluno == 3:
    print("\t"*7, "Disciplinas")
    print("\nHistória""\t""Geografia""\t""Português""\t""Matemática""\t""Ciências""\t""Literatura")
    print("\t", Jose_Historia,"\t\t", Jose_Geografia,"\t\t", Jose_Portugues,"\t\t", Jose_Matematica,"\t\t", Jose_Ciencias,"\t\t ", Jose_Literatura)
    print("_"*72) 
    print("\t "*6, f" Média =: {Media_Jose:1.2f}")
    if Media_Jose >= 5:
        print ("\n", "\t"*6, "Aluno(a) aprovado(a)")
        print("_"*72) 
elif Aluno == 4: 
    print("\t"*7, "Disciplinas")
    print("\nHistória""\t""Geografia""\t""Português""\t""Matemática""\t""Ciências""\t""Literatura")
    print("\t", Daniel_Historia,"\t\t", Daniel_Geografia,"\t\t", Daniel_Portugues,"\t\t", Daniel_Matematica,"\t\t", Daniel_Ciencias,"\t\t ", Daniel_Literatura)
    print("_"*72) 
    print("\t "*6, f" Média =: {Media_Daniel:1.2f}")
    if Media_Daniel >= 5:
        print ("\n", "\t"*6, "Aluno(a) aprovado(a)")
        print("_"*72) 