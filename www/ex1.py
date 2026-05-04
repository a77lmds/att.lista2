#1.Crie uma lista com números de 1 à 10
#2.Remova o elemento da posição 2
#3.Remova o elemento de valor 5
#4.Acrescente 11 e 12 ao fim da lista
#5.Acrescente 5 no início da lista (use a função insert)
#6.Exiba o tamanho da lista  (use a função len)
#7.Exiba a lista
#8.Ordene a lista
#9.Exiba a lista


w = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

del w[2]
print(w)

w.remove(5)
print(w)

w.append(11)
w.append(12)
print(w)

w.insert(0, 5)
print(w)

tamanho = len(w)
print(f"tamanho da lista: {tamanho}")

print(f"lista: {w}")
w.sort()
print(f"Lista ordenada: {w}")