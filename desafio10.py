#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
#considere US$1,00=R$3,27
real = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = real / 5.27
print('com R${:.2f} voce tem pode comprar US${:.2f}'.format(real, dolar,))