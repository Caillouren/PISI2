# 1º Ler um número inteiro e exibir seu dobro.
num = int(input("Digite um número e eu lhe mostrarei o dobro do seu valor: "))
print(f"O do seu número é: {num * 2}")

# 2º Exibir a multiplicação de dois números reais informados pelo usuário.
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
print(f"A multiplicação dos números dado é: {num1 * num2:.2f}")

# 3º Calcular a média aritmética de três notas fornecidas pelo usuário.
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
print(f"A média aritmética dessas notas é: {(nota1 + nota2 + nota3) / 3:.2f}")

# 4º Faça um programa para ler as dimensões de um terreno e exibir a área do mesmo.
dim1 = int(input("Quantos metros de comprimento tem o terreno? "))
dim2 = int(input("Quantos metros de largura tem terreno? "))
print(f"A área do terreno, em questão, é de: {dim1 * dim2} metros quadrados")
