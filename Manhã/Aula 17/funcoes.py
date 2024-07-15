# # Verificar palíndromo:

# # Descrição: Crie uma função chamada e_palindromo que recebe uma string e retorne True se a string for um palíndromo e False caso contrário.
# # Exemplo: Se o usuário digitar "radar", a função deve retornar True.
# def inverter_palavra(palavra):
#     palavraInvertida = ""
    
#     for i in range(len(palavra)):
#         palavraInvertida += palavra[-1-i]
        
#     return palavraInvertida

# def e_palindromo(palavra):
    
#     # palavraInvertida = ""
    
#     # for i in range(len(palavra)):
#     #     palavraInvertida += palavra[-1-i]
    
#     palavraInvertida = inverter_palavra(palavra)
                   
#     if palavra.lower() == palavraInvertida.lower():
#         return True
#     else:
#         return False
    
# print(e_palindromo("abacate"))

# aniversario = "1612"

# print(inverter_palavra("2161"))

# # Contar caracteres:

# # Descrição: Crie uma função chamada contar_caracteres que recebe uma string e retorne um dicionário com a contagem de cada caractere na string.
# # Exemplo: Se o usuário digitar "hello", a função deve retornar {'h': 1, 'e': 1, 'l': 2, 'o': 1}.

# def conta_caracteres(palavra):
#     # banana
#     caracteres = {}
    
#     for letra in palavra:
#         if letra not in caracteres:
#             caracteres[letra] = 1
#         else:
#             caracteres[letra] += 1
            
#         print(letra)
#         print(caracteres)
        
#     return caracteres

# def conta_caracteres2(palavra):
#     # banana
#     caracteres = {}
    
#     for letra in palavra:
#         caracteres[letra] = palavra.count(letra)
            
#         print(letra)
#         print(caracteres)
        
#     return caracteres

# def conta_caracteres3(palavra):
#     # banana
#     caracteres = {}
#     palavraSemDuplicatas = set(palavra)
    
#     for letra in palavraSemDuplicatas:
#         caracteres[letra] = palavra.count(letra)
            
#         print(letra)
#         print(caracteres)
        
#     return caracteres
        
# conta_caracteres("banana")
# conta_caracteres2("abacate")
# conta_caracteres3("arara")
