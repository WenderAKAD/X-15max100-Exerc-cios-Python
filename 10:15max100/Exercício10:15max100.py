''' Exercício 10: Salário com comissão - Leia o salário fixo de um vendedor e o total vendido no mês. Calcule uma comissão de 4% sobre as vendas e mostre a comissão e o salário total.
'''
print(' Vamos calcular suas comissões! ') #Para ficar mais estético.
salarioBase = float(input(' Informe seu salário: R$'))
totalVendasMes = float(input(' Informe o valor total de suas vendas deste mês: R$'))
comissaoVendasMes = totalVendasMes * 0.04
#print(comissaoVendasMes) #Testando fórmula 
salarioComComissao = salarioBase + comissaoVendasMes
print(' Seu salário base é R${0:.2f} e você vendeu o total de R${1:.2f}. '.format(salarioBase, totalVendasMes))
print(' O valor da comissão é de R${0:.2f} portanto seu salário somado a comissão será de R${1:.2f} '.format(comissaoVendasMes, salarioComComissao))