#!/usr/bin/python3.5 
# Calculadora +-*/
# receber entrada pelo input

#Executar comandos do servidor

import sys
print(sys.argv)

for k in range(len(sys,argv)):
	print('Parametro {}: {}'.format(k,sys.argv[k]))


##############################################

exit()

def descobre_dic(**kwargds):
	print(kwargs)

	for k in kwargds.keys():
		print('chove: {}'.format(k))
		print('valor: {}'.format(kwargds))

descobre_dic(nome="servidor",ip="192.168.16.1",dominio="4linux.com.br")
print("\n")
descobre_dic(user="joaozinho",nome="joao",sobrenome="silva",idade="20")



##############################################

#Calculadora
def soma(a,b):
	return a + b
def sub(a,b):
	return a - b
def mult(a,b):
	return a + b
def divisao(a,b):
	return a / b

operadores = '+-*/'
operacao = input('Digite: ')

for k in operacao:
	if k in operadores:
		o = k
		a,b = operacao.split(k)
		a = int(a)
		b = int(b)

dic = {'+':soma,'-':sub,'*':mult,'/':divisao}

z = dic[o](a,b)
print(z)

exit()
##############################################


operadores = '+-*/'
operacao = input('Digite: ')
for k in operacao:
	if k in operadores:
		a,b = operacao.split(k)
		a = int(a)
		b = int(b)

if k == "+":
	print(a+b)
elif k == '-':
	print(a-b)
elif k == '*':
	print(a*b)
elif k == '/':
	print(a/b)

exit()

