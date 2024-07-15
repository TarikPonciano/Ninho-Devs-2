valorOriginal = float(input("Digite o valor da compra:"))

if (valorOriginal >= 200):
    desconto = 0.1
elif(valorOriginal >= 100 and valorOriginal < 200):
    desconto = 0.05
else:
    desconto = 0
    
valorDesconto = valorOriginal * desconto
valorFinal = valorOriginal - valorDesconto

print(f'''
----------Nota Fiscal------------
Valor da compra: R$ {valorOriginal:.2f}
Valor do desconto: R$ {valorDesconto:.2f}
Valor final da compra: R$ {valorFinal:.2f}      
      ''')

    
    