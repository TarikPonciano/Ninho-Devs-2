print('''
Produto                  Preço
100 Cachorro Quente      R$ 1.10
101 Bauru Simples        R$ 1.30
102 Bauru c/ovo          R$ 1.50
103 Hamburguer           R$ 1.10
104 Cheeseburguer        R$ 1.30
105 Refrigerante         R$ 1.00
106 Batata Frita         R$ 0.90
      ''')

codigo = input("Digite o código do produto: ")

quantidade = int(input("Digite quantas unidades serão adquiridas: "))

if(codigo == "100"):
    preco = 1.1
elif(codigo == "101"):
    preco = 1.3
elif(codigo == "102"):
    preco = 1.5
elif(codigo == "103"):
    preco = 1.1
elif(codigo == "104"):
    preco = 1.3
elif(codigo == "105"):
    preco = 1.0
elif(codigo == "106"):
    preco = 0.9
else:
    print("Código Inválido.")
    preco = 0
    
total = preco * quantidade

print(f"O valor do seu pedido é: R$ {total:.2f}")
    