# Faça um Programa que solicite a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor (lista). Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []
for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    altura = float(input(f"Digite a altura da pessoa {i+1} (em cm): "))
    idades.append(idade)
    alturas.append(altura)

print("\nDados na ordem inversa:")
idades.reverse()
alturas.reverse()
print(f"lista de idades: {idades}")
print(f"lista de altura: {alturas}")

# Informe quantos são maiores de 18 anos e quantos são menores
# Informe quantos são menores de 1.5 metros

maiores_18 = 0
menores_18 = 0
menor_150 = 0

for i in range(5):
    if idades[i] >= 18:
        maiores_18 += 1
    else:
        menores_18 += 1

    if alturas[i] < 1.5:
        menor_150 += 1

print("\nResultado:")
print(f"Maiores de 18 anos: {maiores_18}")
print(f"Menores de 18 anos: {menores_18}")
print(f"Pessoas com altura menor que 1.5m: {menor_150}")