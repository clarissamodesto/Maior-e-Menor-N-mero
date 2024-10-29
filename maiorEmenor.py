'''
Nome: Clarissa Cruz
Data: 29/10/2024
Versão 1
'''
# Faça um programa que leia três números, verifique (usando if e else) e mostre o maior e o menor deles;

num1 = float (input ('Digite um número: '))
num2 = float (input ('Digite outro número: '))
num3 = float (input ('Digite um terceiro número: ')) 

#Verificando o maior número
if num2 <= num1 >= num3:
    print (f'O maior número é o {num1}')
elif num1 <= num2 >= num3:
    print (f'O maior número é o {num2}')
else:
    print (f'O maior número é o {num3}')

#Verificando o menor número

if num2 >= num1 <= num3:
    print (f'O menor número é o {num1}')
elif num1 >= num2 <= num3:
    print (f'O menor número é o {num2}')
else:
    print (f'O menor número é o {num3}')