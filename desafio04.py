#Faça um programa que leia algo pelo teclado e mostra na tela seu tipo primitivo e todas as informações possiveis sobre ele.
n = input('Digite algo no teclado')
print('O tipo primitivo é:',type(n))
print('É letra:',n.isalnum())
print('Possui espaços:',n.isalpha())
print('Esta em maiuscula:',n.isupper())
print('Esta em minisculo:',n.islower())
print('É numero:',n.isnumeric())


