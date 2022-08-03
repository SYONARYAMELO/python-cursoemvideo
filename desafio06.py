#crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('Digite um numero'))
d = n1 * 2
t = n1 * 3
r = n1 **(1/2)
print('O valor é {}, o Dobro é {}, o triplo é {}, e a raiz quadrada é {}'.format(n1, d, t, r))

# outra forma
n1 = int(input('Digite um numero'))
print('O valor é {}, o dobro é {}'.format(n1, (n1*2)))
print('O triplo é {}, a raiz quadrada vale {}'.format(n1, pow(n1, (1/2))))
