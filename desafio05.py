#faca um programa que leia um numero e mostre na tela o seu sucessor e seu antecessor.
n1 = int(input('Digite um numero'))
s = n1 + 1
sub = n1 - 1
print('O numero é {},o sucessor é {}, o antecessor é {},'.format(n1, s, sub))

# outra formato

n1 = int(input('Digite um numero'))
print('O valor é {} , é sucessro é {}, o antecessor é {},'.format(n1, (n1-1),(n1+1)))