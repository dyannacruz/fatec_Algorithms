#Autora Dyanna Cruz 

#Exercício 3: Em uma compra de supermercado, foram adquiridos os seguintes itens e quantidades:
#- Arroz → 5kg;
#- Feijão → 3kg;
#- Açúcar → 2kg;
#- Batata → 3kg;
#- Óleo → 5 litros;
#- Bolacha de Água e Sal → 1 pacote;
#- Bolacha de Maizena → 1 pacote;
#- Banana → 1 dúzia e meia;
#- Couve-Flor → 2 maços;
#- Leite em Pó → 2 latas de 1kg;
#→ Criar código em Python para inserir os preços por unidade de cada item das compras e depois
#mostrar estes preços no console;
#→ Calcular o preço total para cada item em função das quantidades, e mostrá-los no console;
#→ Calcular o preço total da compra e mostrá-lo no console;
#→ Estabelecer um limite de preço para o total da compra;
#→ Se o preço da compra for inferior ao limite estabelecido imprimir no console: “pagamento em dinheiro”;
#→ Se o preço da compra for superior ao limite estabelecido imprimir no console: “pagamento em parcelas com uso de cartão”.


# Solução:

#Cálculo do preço total de cada item
#Preços
print("_" * 56)
Preco_Arroz = float(input("Insira o preço de 1Kg de arroz R$: "))
Preco_Feijao = float(input("Insira o preço de 1Kg de feijão: R$ "))
Preco_Acucar = float(input("Insira o preço de 1Kg de açucar R$: "))
Preco_Batata = float(input("Insira o preço de 1Kg de batata R$: "))
Preco_Oleo = float(input("Insira o preço de 1l de óleo R$: "))
Preco_Bolacha_de_agua_e_sal = float(input("Insira o preço da bolacha de água e sal R$: "))
Preco_Bolacha_de_maizena = float(input("Insira o preço da bolacha de maizena R$: "))
Preco_Banana = float(input("Insira o preço da unidade da banana R$: "))
Preco_Couve_flor = float(input("Insira o preço do maço de couve-flor R$: "))
Preco_Leite_em_po = float(input("Insira o preço do Kg de leite em pó R$: "))

#Quantidades
print("_" * 56)
Qtd_Arroz = int(input("Insira a qtd. de Arroz: "))
Qtd_Feijao = int(input("Insira a qtd. Feijao: ")) 
Qtd_Acucar = int(input("Insira a qtd. Açucar: "))
Qtd_Batata = int(input("Insira a qtd. Batata: "))
Qtd_Oleo = int(input("Insira a qtd. Óleo: "))
Qtd_Bolacha_de_agua_e_sal = int(input("Insira a qtd. Bolacha de agua e sal: "))
Qtd_Bolacha_de_maizena = int(input("Insira a qtd. Bolacha_de_maizena: "))
Qtd_Banana = int(input("Insira a qtd. Banana: "))
Qtd_Couve_flor = int(input("Insira a qtd. Couve flor: "))
Qtd_Leite_em_po = int(input("Insira a qtd. Leite em pó: "))

#Totais
print("_" * 56)
Total_Arroz = Preco_Arroz * Qtd_Arroz
Total_Feijao = Preco_Feijao * Qtd_Feijao
Total_Acucar = Preco_Acucar * Qtd_Acucar
Total_Batata = Preco_Batata * Qtd_Batata
Total_Oleo = Preco_Oleo * Qtd_Oleo
Total_Bolacha_de_agua_e_sal = Preco_Bolacha_de_agua_e_sal * Qtd_Bolacha_de_agua_e_sal
Total_Bolacha_de_maizena = Preco_Bolacha_de_maizena * Qtd_Bolacha_de_maizena
Total_Banana = Preco_Banana * Qtd_Banana
Total_Couve_flor = Preco_Couve_flor * Qtd_Couve_flor
Total_Leite_em_po = Preco_Leite_em_po * Qtd_Leite_em_po
Total_compra = Total_Arroz + Total_Feijao + Total_Acucar + Total_Batata + Total_Oleo + Total_Bolacha_de_agua_e_sal + Total_Bolacha_de_maizena + Total_Banana + Total_Couve_flor + Total_Leite_em_po

#Exibição
print("_" * 56)
print("*" * 19, "Resumo da Compra", "*" *19)
print("\nItem                     QTD   Valor Unit     Subtotal")
print("\nArroz                    ", Qtd_Arroz, "    R$ ", Preco_Arroz, "      R$ ", round(Total_Arroz, 2))
print("Feijão                   ", Qtd_Feijao, "    R$ ", Preco_Feijao, "      R$ ", round(Total_Feijao, 2))
print("Açucar                   ", Qtd_Acucar, "    R$ ", Preco_Acucar, "      R$ ",   round(Total_Acucar, 2))
print("Batata                   ", Qtd_Batata, "    R$ ", Preco_Batata, "      R$ ",   round(Total_Batata, 2))
print("Óleo                     ", Qtd_Oleo  , "    R$ ", Preco_Oleo,   "      R$ ",   round(Total_Oleo, 2))
print("Bolacha de água e sal    ", Qtd_Bolacha_de_agua_e_sal, "    R$ ", Preco_Bolacha_de_agua_e_sal,"      R$ ",   round(Total_Bolacha_de_agua_e_sal, 2))
print("Bolacha de maizena       ", Qtd_Bolacha_de_maizena,    "    R$ ", Preco_Bolacha_de_maizena,"       R$ ",   round(Total_Bolacha_de_maizena, 2))
print("Banana                   ", Qtd_Banana, "    R$ ", Preco_Banana, "       R$ ",   round(Total_Oleo,2 ))
print("Couve-Flor               ", Qtd_Couve_flor, "    R$ ", Preco_Couve_flor,"      R$ ",   round(Total_Couve_flor, 2))
print("Leite em pó              ", Qtd_Leite_em_po, "    R$ ", Preco_Leite_em_po,"      R$ ",   round(Total_Leite_em_po, 2))
print("_" * 56)
#Limite de compra

print("_" * 56)
Limite_de_compra = float(input("Digite o limite de compra: "))
if Total_compra <= Limite_de_compra:
    print("\nO pagamento deverá ser em dinheiro")
else:
    print("\nO pagamento deverá ser com uso do cartão")
print("_" * 56)