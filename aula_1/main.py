print('Teste2')

#crie um programa em que o usuário digite um texto e conte a quentidade de caracteres.

nome = input('Digite o seu texto: ')
caracteres = len(nome)
print(caracteres)

#crie um programa em que digite 2 números e ele traga a soma desses números

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = n1 + n2
print(soma)

#Desafio do dia: Cálculo de Bônus com Entrada do Usuário
#Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

nome = str(input('Digite o seu texto: '))
salario = nome = int(input('Digite o seu salario: '))
PERCENTUAL = 1.5
bonus = 1000 + salario * PERCENTUAL
print(f"Meu nome é: {nome}, e meu bonus foi de: {bonus}")