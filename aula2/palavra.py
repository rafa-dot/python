#!/usr/bin/python3.5
# verifica se a palavra é igual de tras para frente

palavra = str(input('Escreva uma palavra: '))

if palavra == palavra[::-1]: 
	print(palavra + ' é palindrome')
else :
	print(palavra + ' não é palindrome')

