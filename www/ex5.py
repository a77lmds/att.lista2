# Faça um programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor1 = []
vetor2 = []
for i in range(10):
    num1 = float(input(f"Digite o número {i+1} do vetor 1: "))
    num2 = float(input(f"Digite o número {i+1} do vetor 2: "))
    vetor1.append(num1)
    vetor2.append(num2)

vetor3 = []
