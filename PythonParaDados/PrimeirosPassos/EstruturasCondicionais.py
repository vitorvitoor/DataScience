import os

#1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
num1 = int(input("Digite o primeiro número desejado: "))
num2 = int(input("Digite o segundo número desejado: "))

if num1 > num2:
    print(f"O primeiro número {num1} é de maior valor que o segundo {num2}")
elif num1 == num2:
    print("Os dois números tem o mesmo valor")
else:
    print(f"O Segundo número {num2} é maior que o primeiro {num1}")

input("\n>> Pressione ENTER para ir para o próximo exercício...")
os.system('cls')

#2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
percentual = float(input("Digite o percentual de crescimento de produção da empresa: ")) 
if percentual >= 0.5:
    print(f"Porcentagem de crescimento positiva {percentual}%")
else:
    print(f"Porcentagem de crescimento negativa {percentual}%")

input("\n>> Pressione ENTER para ir para o próximo exercício...")
os.system('cls')

#3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
letra = input("Digite a letra desejada: ").lower()

if letra in ["a", "e", "i", "o", "u"]:
    print(f"A letra inserida '{letra}' é uma VOGAL")
else:
    print(f"A letra '{letra}' é uma consoante")

input("\n>> Pressione ENTER para ir para o próximo exercício...")
os.system('cls')

#4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
ano1 = int(input("Digite o valor médio do primeiro ano para o carro desejado: "))
ano2 = int(input("Digite o valor médio do segundo ano para o carro desejado: "))
ano3 = int(input("Digite o valor médio do terceiro ano para o carro desejado: "))

maior_preco = max(ano1, ano2, ano3)
menor_preco = min(ano1, ano2, ano3)

print(f"O maior valor foi: R$ {maior_preco}")
print(f"O menor valor foi: R$ {menor_preco}")

input("\n>> Pressione ENTER para ir para o próximo exercício...")
os.system('cls')

#5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
produto1 = int(input("Digite o valor do primeiro produto desejado: "))
produto2 = int(input("Digite o valor do segundo produto desejado: "))
produto3 = int(input("Digite o valor do terceiro produto desejado: "))

produto_barato = min(produto1, produto2, produto3)

print(f"o produto mais barato é: {produto_barato}")

input("\n>> Pressione ENTER para ir para o próximo exercício...")
os.system('cls')

#6) Escreva um programa que leia três números e os exiba em ordem decrescente.
n1 = float(input("Digite o valor do primeiro número desejado: "))
n2 = float(input("Digite o valor do segundo número desejado: "))
n3 = float(input("Digite o valor do terceiro número desejado: "))

if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print(f"Ordem: {n1}, {n2}, {n3}")
    else:
        print(f"Ordem: {n1}, {n3}, {n2}")

if n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print(f"Ordem: {n2}, {n1}, {n3}")
    else:
        print(f"Ordem: {n2}, {n3}, {n1}")

if n3 >= n1 and n3 >= n2:
    if n1 >= n2:
        print(f"Ordem: {n3}, {n1}, {n2}")
    else:
        print(f"Ordem: {n3}, {n2}, {n1}")

input("\n>> Pressione ENTER para ir para o próximo exercício...")
os.system('cls')

#7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
turno = input("Em qual turno você estuda? (manhã, tarde ou noite): ").strip().lower()

if turno == "manhã":
    print("Bom dia!")

if turno == "tarde":
    print("Boa tarde!")

if turno == "noite":
    print("Boa noite!")

else:
    print("O turno inserido está incorreto.")

input("\n>> Pressione ENTER para ir para o próximo exercício...")
os.system('cls')

#8) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.
numero_inteiro = int(input("Digite o número INTEIRO desejado: "))

if numero_inteiro % 2 == 0:
    print("Par")
else:
    print("Ímpar")

input("\n>> Pressione ENTER para ir para o próximo exercício...")
os.system('cls')

#9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.
numero_desejado = float(input("Digite o número desejado: ").replace(",", "."))

if numero_desejado % 1 == 0:
    print("O número escolhido é um número INTEIRO")
else:
    print("O número escolhido é um número DECIMAL")

input("\n>> Pressione ENTER para ir para o próximo exercício...")
os.system('cls')

#10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

num1 = int(input("Digite o primeiro número desejado: "))
num2 = int(input("Digite o segundo número desejado: "))
operacao = input("Digite o tipo de operação desejada: (+, -, *, /)")

resultado = 0 
valido = True

if operacao == "+":
    resultado = num1 + num2

if operacao == "-":
    resultado = num1 - num2

if operacao == "*":
    resultado = num1 * num2

if operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero não permitida.")
        valido = False
else:
    print("Operação não permitida")
    valido = False

if valido:
    print(f"\n--- Analisando o resultado: {resultado} ---")

    if resultado % 2 == 0:
        print("- O número é PAR")
    else:
        print("- O número é ÍMPAR")

    if resultado > 0:
        print("- O número é POSITIVO")
    elif resultado < 0:
        print("- O número é NEGATIVO")
    else:
        print("- O número é ZERO (Neutro)")

    if resultado % 1 == 0:
        print("- O número é INTEIRO")
    else:
        print("- O número é DECIMAL")