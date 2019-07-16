#!/usr/bin/python3.5 

def calcular_fig_geometrica(*args):
	if len(args) == 1:
		print('area do quadrado: {}'.format(args[0]**2))
	elif len(args) == 2:
		print('area do retangulo: {}'.format(args[0]*args[1]))

	else:
		print('volume: {}'.format(args[0]*args[1]*args[2]))

calcular_fig_geometrica(2)
calcular_fig_geometrica(2,10)
calcular_fig_geometrica(2,10,10)


exit()

def animal(tipo='cachorro',nome='rex'):
	print('eu tenho um {} que se chama {}'.format(tipo,nome))

animal(tipo,nome)

exit()

def diga_ola(n)
	print('ola ' + nome)

def pergunta():
	nome = input('digite nome: ')

x = pergunta()
diga_ola(x)

exit()
def diga_ola():
	print('ola')

diga_ola()