''' Exercício 14: Troca de valores - Leia dois valores inteiros, armazene-os em A e B e troque seus conteúdos. Ao final, mostre os valores depois da troca.
'''
'''
a = int(input(' Digite um valor int para A: '))
b = int(input(' Digite um valor int para B: '))
c = a
print(' \n A: {0} \n B: {1} '.format(a, b))
a = b
b = c
print(' \n A: {0} \n B: {1} '.format(a, b))

#OU
'''
# Leitura dos valores originais:
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

print(f"\n[Original]  A = {a} | B = {b}")

# Primeira troca:
a, b = b, a
print(f"[1ª Troca]  A = {a} | B = {b}")

# Segunda troca (Verificação Final)
a, b = b, a 
print(f"[2ª Troca]  A = {a} | B = {b}")