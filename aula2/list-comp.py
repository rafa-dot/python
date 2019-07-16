#!/usr/bin/python3.5

# DICIONARIO DENTRO DE UM DICIONARIO
herois = {'batman':{'identidade':'bruce wayne','cidade':'gotham'},
'superman':{'identidade':'clark kent','cidade':'metropolis'}}

print(herois['batman']['identidade'])

# LISTA DENTRO DE UM DICIONARIO
lanche = {'pão':['integral','4 queijos','italiano']
'queijo':['prato','cheddar','suiço'],
'recheio':['frango','carne','almndega']

print(lanche[lanche['pao'][1]])

exit()

koppa1 = {'cpr':'vermelho','pontos':30}
koppa2 = {'cpr':'verde','pontos':50}
koppa3 = {'cpr':'azul','pontos':100}

koppa = [koppa1,koppa2,koppa3]
print(koppal[1]['cor'])

lista = []

for k in range(10):
	lista.append(koppa1)

exit ()

##########################################

usuario = {'username':'exemplo1','nome':'joao','sobrenome':'silva'}

print(usuario)
for chave,valor in usuario.items():
	print('chave: {}'.format(chave))
	print('valor: {}'.format(valor))

for chave in usuario.keys():
	print('chave: {}'.format(chave))

for valor in usuario.values():
	print('valor: {}'.format(valor))

exit ()

##########################################

koppal = {'cpr':'vermelho','pontos':30}

pontos = koppal ['pontos']
# print (pontos)

##########################################

koppal['eixo_x'] = 5
koppal['eixo_y'] = 15
koppal['velocidade'] = 'rapido'

print(koppal)

if koppal['velocidade'] == 'lento':
	anda_x = 1
elif koppal['velocidade'] == medio:
	anda_x = 2
else:
	anda_x = 3

koppal['eixo_x'] += anda_x

print(koppal)

exit()

##########################################

cores = {'red':'vermelho','blue':'azul','green':'verde'}
# print (cores['red'])

##########################################

retangulo = (100,50)
print(retangulo[0],retangulo[1])

retangulo = (30,50)
print(retangulo[0],retangulo[1])
x = list(retangulo)
# x[0 = 300]
print (x)

exit()

##########################################

pot = [valor for valor in range(1,11) if valor % 2 == 0]

print(pot)

exit() 

pot = []

for valor in range(1,11):
	if valor % 2 == 0:
		pot.append(valor)
print(pot)