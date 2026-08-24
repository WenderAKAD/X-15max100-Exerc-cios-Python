''' Exercício 4: Dobro, Triplo e Metade - Leia um número real e mostre o dobro, o triplo e a metade deste valor. 
'''
n1 = float(input(' Digite um número inteiro: '))
nDobro = n1 * 2
nTriplo = n1 * 3
nMetade = n1 / 2
print('O número digitado foi {0}'.format(n1))
print('O dobro deste número é {0:.2f}'.format(nDobro))
print('O triplo deste número é {0:.2f}'.format(nTriplo))
print('A metade deste é {0:.2f}'.format(nMetade))