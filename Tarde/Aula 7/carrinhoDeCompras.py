#Crie um programa que recebe o valor de 5 produtos, no final calcula o total da compra e determinar se o cliente terá desconto ou não. Se o valor total for maior que 200, 10% de desconto, senão, não há desconto. Imprima na tela, os valores inseridos, o total da compra, o valor descontado e o valor final da compra.
totalDaCompra = 0
historico = ""

for i in range(5):
    
    nomeDoProduto = input("Digite o nome do produto:")
    valorDoProduto = float(input("Digite o valor do produto:"))
    quantidade = int(input("Digite a quantidade:"))
    
    totalDaCompra += valorDoProduto * quantidade
    historico += f"{nomeDoProduto} - R$ {valorDoProduto:.2f} - x{quantidade} - R$ {(valorDoProduto*quantidade):.2f}\n"
    
if (totalDaCompra >= 200):
    desconto = 0.1
else:
    desconto = 0
    
valorDesconto = totalDaCompra * desconto

valorFinal = totalDaCompra - valorDesconto

print(f'''
---------- Nota Fiscal ----------

{historico}

Valor Original: R$ {totalDaCompra}

Valor do Desconto: - R$ {valorDesconto}

Valor Final: R$ {valorFinal} 
      ''')
    
    
    
    


