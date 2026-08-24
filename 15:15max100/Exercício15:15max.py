''' Exercício 15: Custo final da compra - Leia o preço unitário de um produto, a quantidade comprada e o valor do frete. Mostre o subtotal dos produtos e o valor total da compra. 
'''

precoUnitario = float(input("Digite o preço unitário do produto: R$ "))
quantidade = int(input("Digite a quantidade comprada: "))
frete = float(input("Digite o valor do frete: R$ "))

subtotal = precoUnitario * quantidade
total = subtotal + frete

print("\nSubtotal dos produtos: R$ {0:.2f}".format(subtotal))
print("Valor total da compra: R$ {0:.2f}".format(total))