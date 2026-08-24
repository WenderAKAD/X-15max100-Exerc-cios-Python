''' Exercício 8: Leia um preço de um produto, calcule um desconto de 10% e mostre o valor do desconto e o preço final. 
'''
valorProduto = float(input(' Valor original do produto: R$'))
valorDesconto = valorProduto / 10
valorFinal = valorProduto - valorDesconto
#print(valorProduto, valorDesconto, valorFinal) - Testando fórmulas
print(' O valor original do produto é R${0:.2f}\n O desconto de 10 por cento equivale a {1:.2f} portanto o valor a ser pago será de R${2:.2f} '.format(valorProduto, valorDesconto, valorFinal))