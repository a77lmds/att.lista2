# Faça um programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor1 = []
vetor2 = []
for i in range(10):
    vetor1.append(int(input("vetor 1: ")))
for i in range(10):
    vetor2.append(int(input("vetor 2: ")))

vetor3 = []
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i]) 
print(vetor3)