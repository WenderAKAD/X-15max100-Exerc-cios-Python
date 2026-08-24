'''Exercício 5: Conversão de medidas - Leia uma medida em metros e mostre o equivalente em centímetros e milímetros. 
'''
n1 = float(input(' Digite um valor (metros): '))
centimetro = n1 * 100
milimetro = n1 * 1000
print(' O valor escolhido em metros foi {0:.2f} \n O valor equivale a {1:.2f} centímetros e a {2:.2f} milímetros. '.format(n1, centimetro, milimetro))