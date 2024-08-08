# #### Inteiros (`int`)

# # 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# n1 = -4
# n2 = -5
# soma = n1 + (n2)
# print(soma)

# # 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# user_input = int(input('Digite um número: '))
# divisor = 5
# resto =  user_input % divisor
# print(resto)

# # 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# user_input1 = int(input('Digite um número: '))
# user_input2 = int(input('Digite um número: '))
# multi = user_input1 * user_input2

# # 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# divisor = int(input('Digite um número: '))
# dividendo = int(input('Digite um número: '))
# divisao_inteiro =  dividendo / divisor
# print(divisao_inteiro)

# # 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# num = int(input('Digite um número: '))
# quadrado = num ** 5
# print(quadrado)

# # #### Números de Ponto Flutuante (`float`)

# # 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# flutuante1 = float(input('Digite um número: '))
# flutuante2 = float(input('Digite um número: '))
# soma = flutuante1 + flutuante2

# # 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# nota1 = 10
# nota2 = 8
# media = (nota1 + nota2) / 2

# # 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = 3
# expoente = 4 
# exponenciacao = base ** expoente

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = 25
# fahrenheit= (9/5) * celsius + 32
# print(fahrenheit)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = float(25.7)
# quadrado_raio = raio ** 2
# pi = 3.14159
# area = pi * raio
# print(area)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# texto = str(input('Digite um texto: ')).upper()
# print(texto)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = str(input('Digite um texto: ')).lower()
# print(nome)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# texto2 = str(input('Digite um texto: ')).strip()
# print(texto2)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = str(input('Digite uma data: ')).split('/')
# print(data[0]) 
# print(data[1])  
# print(data[2])

# # 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# texto1 = 'Eu adoro '
# texto2 = 'banoffee'
# concat = texto1 + texto2
# print(concat)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# teste1 = int(input('Digite um número: '))
# teste2 = int(input('Digite um número: '))
# teste3 = int(input('Digite um número: '))
# verificacao = teste1 > teste2 and teste2 < teste3

# print(verificacao)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# teste4 = int(input('Digite um número: '))
# teste5 = int(input('Digite um número: '))
# valores = teste4 == teste5 or teste5 < teste4
# print(valores)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# valor_boleano = str(input('Insira um valor: ')) == 'True'

# if valor_boleano == False:
#     valor_boleano = True
# else:
#     valor_boleano = False

# print(valor_boleano)   

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
valor1 = int(input('Insira um valor: ')) 
valor2 = int(input('Insira um valor: ')) 

if valor1 == valor2:
    resposta = True
else:
    resposta = False

print(resposta)
    
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
valor3 = int(input('Insira um valor: ')) 
valor4 = int(input('Insira um valor: ')) 

if valor3 != valor4:
    resposta = True
else:
    resposta = False

print(resposta)

# #### try-except e if

# 21: Conversor de Temperatura

# 22: Verificador de Palíndromo

# 23: Calculadora Simples

# 24: Classificador de Números

# 25: Conversão de Tipo com Validação