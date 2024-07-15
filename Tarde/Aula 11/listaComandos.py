# Tipo de Dados Lista

# 1. **Criação e Acesso a Elementos**:
#    - **Questão**: Crie uma lista chamada `frutas` que contenha as seguintes frutas: maçã, banana, cereja, manga e abacaxi. Em seguida, acesse e imprima a terceira fruta da lista.
#    - **Dica**: Use índices para acessar elementos.

print("----- Exercício 1 -----")

frutas = ["Maçã", "Banana", "Cereja", "Manga", "Abacaxi"]

print(frutas[2])

# 2. **Modificação de Elementos**:
#    - **Questão**: Dada a lista `animais = ['gato', 'cachorro', 'papagaio', 'coelho']`, substitua o 'cachorro' por 'hamster' e imprima a lista modificada.
#    - **Dica**: Utilize a atribuição por índice.

print()
print("----- Exercício 2 -----")

animais = ["Gato", "Cachorro", "Papagaio", "Coelho"]
animais[1] = "Hamster"

print(animais)



# 3. **Adição de Elementos**:
#    - **Questão**: Adicione a fruta 'laranja' ao final da lista `frutas` criada na questão 1 e imprima a lista resultante.
#    - **Dica**: Utilize o método `append()`.

print()
print("----- Exercício 3 -----")

frutas.append("Laranja")
print(frutas)

# 4. **Inserção de Elementos**:
#    - **Questão**: Insira a fruta 'kiwi' na segunda posição da lista `frutas` e imprima a lista atualizada.
#    - **Dica**: Utilize o método `insert()`.

print()
print("----- Exercício 4 -----")

frutas.insert(1, "Kiwi")
print(frutas)

# 5. **Remoção de Elementos**:
#    - **Questão**: Remova a fruta 'manga' da lista `frutas` e imprima a lista atualizada.
#    - **Dica**: Utilize o método `remove()`.


print()
print("----- Exercício 5 -----")

frutas.remove("Manga")
print(frutas)


# 6. **Pop e Acesso**:
#    - **Questão**: Use o método `pop()` para remover e imprimir o último elemento da lista `animais`. Em seguida, imprima a lista restante.
#    - **Dica**: `pop()` retorna o elemento removido.
print()
print("----- Exercício 6 -----")

print("Removido:", animais.pop(-1))
print(animais)

# 7. **Contagem de Elementos**:
#    - **Questão**: Dada a lista `numeros = [2, 3, 4, 3, 5, 3, 6, 7]`, conte quantas vezes o número 3 aparece na lista.
#    - **Dica**: Utilize o método `count()`.

print()
print("----- Exercício 7 -----")

numeros = [2, 3, 4, 3, 5, 3, 6, 7]
print(numeros.count(3))

contador = 0

for n in numeros:
    if (n == 3):
        contador += 1
        
print(contador)




# 8. **Ordenação de Listas**:
#    - **Questão**: Ordene a lista `numeros` em ordem crescente e imprima a lista ordenada.
#    - **Dica**: Utilize o método `sort()`.

print()
print("----- Exercício 8 -----")

numeros.sort()
print(numeros)


# 9. **Listas Aninhadas**:
#    - **Questão**: Crie uma lista chamada `matriz` que contenha duas listas internas: `[1, 2, 3]` e `[4, 5, 6]`. Acesse e imprima o elemento 5 da `matriz`.
#    - **Dica**: Use índices duplos para acessar elementos em listas aninhadas.
print()
print("----- Exercício 9 -----")

funcionarios = [
    ["Joaquim", "Vendedor", 3000], 
    ["Manoel", "Gerente", 5000],
    ["Zeca", "Promotor", 6000]
]
print(funcionarios[0][2])

# 10. **Conversão para Listas**:
#     - **Questão**: Use a função list() para converter um range para uma nova lista chamada `numeros` que contenha os os números de 1 a 10. Em seguida, imprima a lista `numeros`.
#     - **Dica**: Lembre-se que coleções podem ser transformadas em outras coleções.

print()
print("----- Exercício 10 -----")


numeros = range(1,11)
numeros = list(numeros)

print(numeros)