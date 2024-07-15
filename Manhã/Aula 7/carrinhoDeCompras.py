#Crie um programa que recebe o valor de 5 produtos, no final calcula o total da compra e determinar se o cliente terá desconto ou não. Se o valor total for maior que 200, 10% de desconto, senão, não há desconto. Imprima na tela, os valores inseridos, o total da compra, o valor descontado e o valor final da compra.
totalDaCompra = 0
historico = ""

for i in range(5):
    nomeProduto = input("Digite o nome do produto:")
    valorProduto = float(input("Digite o valor do produto:"))
    quantidade = int(input("Digite a quantidade:"))
    
    totalDaCompra += valorProduto*quantidade
    historico += f"{nomeProduto} - R$ {valorProduto} - x{quantidade} - R${valorProduto*quantidade} \n"

if (totalDaCompra >= 200):
    desconto = 0.1
else:
    desconto = 0
    
valorDescontado = totalDaCompra * desconto
totalFinal = totalDaCompra - valorDescontado

print(f'''
--------- Nota Fiscal ---------
{historico}
Valor Original: R$ {totalDaCompra}
Valor do Desconto: - R$ {valorDescontado}
Valor Final: R$ {totalFinal}
      ''')