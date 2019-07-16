#!/usr/bin/python3.5 
#Informar o codigo qual binario deve utilizar para execução.



exit()

########################################################

#Condicao

idade = int(input('Digite idade: '))
habilitacao = input('Possui habilitação: ')
h = False
if habilitacao.lower().strip() == 'sim':
	h = True
if idade >= 18 and h == True:
	print('Pode Dirigir')
else:
	print('Não pode dirigir')

########################################################

velocidade = int(input('Informe Velocidade: '))
if velocidade > 110:
	multa = (velocidade - 110) * 5
	print('multa: R$ {:.2f}'.format(multa))

########################################################

# Aluno tem 4 notas , calcuular a media
# nome do aluno - input
# calcular a media 
# printar nome do aluno + media

aluno = input('Npme: ')
nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))
nota4 = int(input('Nota 4: '))
media1 = nota1+nota2+nota3+nota4
print(media1)
media2 = media1 / 4
print('Aluno '+str(aluno)+' média '+str(media2))

########################################################

nome = input('Digite nome: ')
idade = input('Digite idade: ')

print('Seu nome é ' +nome+ ' e sua idade é ' +idade)

########################################################

a,b = 10,3
print(a * b)

########################################################

nome = 'joao'
idade = 20
mensagem = nome + ' tem ' + str(idade) + ' anos '
print(mensagem)

########################################################

nome = 'mcdonald\'s\n\t'
sobrenome = 'maddog'

completo = nome.title() + ' ' +sobrenome.title()
print(completo)

########################################################

nome = '      maDdog  '

print(nome.split())
print(nome.title())
print(nome.upper())
print(nome.lower())
print(nome.lstrip())

########################################################

# a =.__dir__() #Saber o que se pode fazer com uma variavel

mensagem = 'ola mundo'
print(mensagem)

mensagem = 'bem vindo'
print(mensagem)

########################################################

# chmod +x *.py #adicionar permissão "x" executar em qualquer arquivo .py
