''' Exercício 9: Reajuste salarial - Leia o salário atual de um funcionário. Calcule o aumento de 15% e mostre o valor do aumento e o novo salário. 
'''

salarioAtual = float(input(' Seu salário: R$'))
porcentagemAumento = salarioAtual * 0.15 #0.15 de 1.0 não esqueça
novoSalario = salarioAtual + porcentagemAumento
print("Valor do aumento: R$ {0:.2f}".format(porcentagemAumento))
print("Novo salário: R$ {0:.2f}".format(novoSalario))