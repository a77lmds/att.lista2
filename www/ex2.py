#1 ler e imprimir 8 valores lidos do teclado.
#2 Escrever a média e a soma destes valores.
#3 Imprimir o menor e o maior.

w  =[]

for i in range (0,8):
	p = int(input(f"digite um {i+1} valor: "))
	w.append(p)
	
print(w)

soma = sum(w)
print(f"Essa é a soma: {soma}")

media = soma / 8
print(f"Média dos valores: {media}")

print(f"Maior número da lista é: {max(w)}")
print(f"Menor número da lista é: {min(w)}")