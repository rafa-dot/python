#!/usr/bin/python3.5

#Trocar todas as vogais por asterisco.

palavra = input('Digite a palavra: ')

vogais = 'aeiouAEIOU ãààâéêèíóôòúùũ'

for k in palavra:
	if k in vogais:
		palavra = palavra.replace(k,'*')

print(palavra)


exit()

palavra = input('Digite a palavra: ')
vogais = 'aeiouAEIOU ãààâéêèíóôòúùũ'
troca = ''

for k in palavra:
	if k in vogais:
		troca += '*'
	else:
		troca += k

print(palavra)

