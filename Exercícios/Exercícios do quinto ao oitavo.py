# 5º Ler um salário de um funcionário e aumentá-lo em 20%. Imprima seu salário final.
salario = float(input("Qual o valor do salário? "))
print(f"Um salário de R${salario} acrescido em 20%, é: R${salario + (salario * 0.20)}")

# 6º Ler o valor de um cheque e escrever quanto vai ser recolhido de CPMF.
# Considere de taxa de 0,3%. Imprimir o valor do imposto.
valor = float(input("Qual o valor do cheque? "))
valortax = valor * (0.3/100)
print(f"O imposto de CPMF sobre o cheque de R${valor} será de: R${valortax}")

# 7º Escreva uma sequência de comandos para solicitar o nome e a matrícula do aluno.
# Em seguida exibir as informações no seguinte formato:
# – Nome do Aluno: “XXXXXXXX”, Matrícula: “ZZZZ”
nome = str(input("Qual o nome do aluno? "))
matricula = int(input("Qua o número de matrícula? "))
print(f'Nome do aluno: "{nome}", Matrícula: "{matricula}"')

# 8º Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# E que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
from math import ceil
area = int(input("Qual o tamanho da área a ser pintada? "))
litros = area / 3
latas = ceil(litros / 18)
preço = latas * 80
print(f"Serão necessárias {latas} latas de tinta para pintar essa área, e custará R${preço}")
