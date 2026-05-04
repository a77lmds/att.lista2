# Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = []
for i in range(10):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)
    
print("\nNúmeros na ordem inversa:")
numeros.reverse()
print(f"lista de números: {numeros}")
