valor = float(input("Digite o valor da sua compra:"))

if (valor<0):
    print("Digite um número válido!")
else:
    if (valor>=200):
        desconto = 0.1
    elif(valor>= 100 and valor < 200):
        desconto = 0.05
    else:
        desconto = 0
        
    valorDoDesconto = valor * desconto
    valorFinal = valor - valorDoDesconto

    print(f'''
---------Nota Fiscal---------

Valor original: R$ {valor:.2f}
Valor do desconto: R$ {valorDoDesconto:.2f}
Valor final: R$ {valorFinal:.2f}
          ''')
    


    
        