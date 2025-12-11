'''
Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.
Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
'''

#1
nome = input("Digite o seu nome: ")
print(f"Olá {nome}")

#2
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"Olá, {nome}, você tem {idade} anos.")

#3
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura em metros: "))
print(f"Olá, {nome}, você tem {idade} anos e mede {altura} metros de altura")
