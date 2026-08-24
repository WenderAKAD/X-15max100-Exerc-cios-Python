''' Exercício 3 = Antecessor e Sucessor - Leia um número inteiro e mostre seu antecessor e seu sucessor. 
'''

n1 = int(input(' Digite um número inteiro: '))
antecessor = n1 - 1
sucessor = n1 + 1
print(' O número escolhido foi {0}, portanto o número que o antecede é {1} e o número que sucede o número escolhido é {2}. '.format(n1, antecessor, sucessor))
