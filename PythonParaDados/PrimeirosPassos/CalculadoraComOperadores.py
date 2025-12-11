'''
Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.
Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.
Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.
'''

#1
valor1 = float(input("Digite o primeiro valor numérico desejado: "))
valor2 = float(input("Digite o segundo valor numérico desejado: "))
print (f"A soma de {valor1} + {valor2} = {valor1 + valor2}")

#2
valor1 = float(input("Digite o primeiro valor numérico desejado: "))
valor2 = float(input("Digite o segundo valor numérico desejado: "))
valor3 = float(input("Digite o terceiro valor numérico desejado: "))
print (f"A soma de {valor1} + {valor2} + {valor3} = {valor1 + valor2 + valor3}")

#3
valor1 = float(input("Digite o primeiro valor numérico desejado: "))
valor2 = float(input("Digite o segundo valor numérico desejado: "))
print (f"A subtração de {valor1} - {valor2} = {valor1 - valor2}")

#4
valor1 = float(input("Digite o primeiro valor numérico desejado: "))
valor2 = float(input("Digite o segundo valor numérico desejado: "))
print (f"A multiplicação de {valor1} * {valor2} = {valor1 * valor2}")

#5
numerador = int(input("Digite o numerador desejado: "))
denominador = int(input("Digite o denominador desejado: ", "Denominador precisa ser diferente de ZERO (0)"))
print (f"A divisão de {numerador} / {denominador} = {numerador / denominador}")

#6
operador = int(input("Digite o operador desejado: "))
potencia = int(input("Digite a potencia desejada: "))
print (f"A exponenciação de {operador} ** {potencia} = {operador ** potencia}")

#7
numerador = int(input("Digite o numerador desejado: "))
denominador = int(input("Digite o denominador desejado: ", "Denominador precisa ser diferente de ZERO (0)"))
print (f"A divisão inteira de {numerador} // {denominador} = {numerador // denominador}")

#8
numerador = int(input("Digite o numerador desejado: "))
denominador = int(input("Digite o denominador desejado: ", "Denominador precisa ser diferente de ZERO (0)"))
print (f"O resto da divisão  de {numerador} % {denominador} = {numerador % denominador}")

#9
valor1 = float(input("Digite a primeira nota desejado: "))
valor2 = float(input("Digite a segunda nota desejado: "))
valor3 = float(input("Digite a terceira nota desejado: "))
print (f"A média das notas {valor1} + {valor2} + {valor3} = {(valor1 + valor2 + valor3) / 3}")

#10

