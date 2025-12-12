import os

'''
Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
Crie um código que solicite uma frase e depois imprima a frase na tela.
Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.
Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.
Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
'''

#1
frase = "Olá, Mundo!"
print(frase)

#2
frase = input("Digite a frase desejada: ")
print(f"A frase desejada foi: {frase}")

#3
frase = input("Digite a frase desejada: ")
print(f"A frase desejada foi: {frase.upper()}")

#4
frase = input("Digite a frase desejada: ")
print(f"A frase desejada foi: {frase.lower()}")

#5
frase = "Olá, Mundo!"
print(frase.strip())

#6
frase = input("Digite a frase desejada: ")
print(f"A frase desejada foi: {frase.strip()}")

#7
frase = input("Digite a frase desejada: ")
print(f"A frase desejada foi: {frase.strip().lower()}")

#8
frase = input("Digite a frase desejada: ")
print(f"A frase desejada foi: {frase.replace('e', 'f')}")

#9
frase = input("Digite a frase desejada: ")
print(f"A frase desejada foi: {frase.replace('a', '@')}")

#10
frase = input("Digite a frase desejada: ")
print(f"A frase desejada foi: {frase.replace('s', '$')}")