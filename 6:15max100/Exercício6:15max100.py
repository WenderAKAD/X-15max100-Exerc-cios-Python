''' Exercício 6:  Área e perímetro do retângulo - Leia a largura e a altura de um retângulo. Mostre a área e o perímetro. 
'''
print(' Vamos calcular a área de um retângulo. ')
altura = float(input(' Digite a altura: '))
largura = float(input(' Digite a largura: '))
areaRetangulo = altura * largura
perimetroRetangulo = 2 * (altura + largura)

print(' Altura: {0}\n Largura: {1}'.format(altura, largura))
print(' Com esses números temos a área {0} e seu perímetro foi é de {1} '.format(areaRetangulo, perimetroRetangulo))