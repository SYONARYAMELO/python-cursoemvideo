#faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.
salario = float(input('Digite o salario do funcionário R$'))
aumento = salario + (salario * 15 / 100)
print('O salario é R${:.2f}, e com aumento de 15% passa para R${:.2f}'.format(salario, aumento))