nome = input('Qual é o seu nome')
print('Prazer em te conhecer {}!'.format(nome))

#

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},a multiplicação é {}, a divisão é {:.3f},'.format(s, m, d))
print('Divisão inteira é {}, e potencia é {}'.format(di, e))
