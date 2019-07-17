#!/usr/bin/python3.5 

# Aluno tem 4 notas , calcular a media
# nome do aluno - input
# printar nome do aluno + media
# se a media for maior que 5 esta aprovado
# se a media for menor que 5 esta reprovado
# se ficar entre 5 e 7 pede uma nova nota

aluno = input('Nome: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))
media1 = nota1+nota2+nota3+nota4
media2 = media1 / 4
print('Aluno: '+str(aluno)+' média '+str(media2))

if media2 >= 7:
	print('Aprovado')
elif media2 >= 5:
	print('Exame')
	nota5 = float(input('Digite a nota do exame: '))
	media2 = (media2 + nota5) / 2
	
	if media2 >= 5:
		print('Aprovado')
	else:
		print('Reprovado')
else:
	print('Reprovado')

exit()


########################################################

# Abaixo de 200 min cobra R$. 0.20 por min
# entre 200 a 400 min cobra R$. 0.18
# acima de 400 o preco é R$. 0.15

# minutos = int(input('minutos utilizados: '))
# if minutos < 200:
#	preco = 0.20
# elif minutos <= 400
#	preco = 0.18
# else:
#	preco = 0.15

# print('Conta R$ {:.2f}')