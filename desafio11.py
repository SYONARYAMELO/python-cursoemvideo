#faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pinta-lá,
# sabendo que cada litro de tinta, pintauma área de 2m².

larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
print('A parede tem a dimensão de {}x{} e sua área é de {}m²,'.format(larg, alt, area))
tinta = area/2
print('Para pintar a parede é necessário {} litros de tinta,'.format(tinta))
