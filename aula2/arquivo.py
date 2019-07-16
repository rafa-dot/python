#!/usr/bin/python3.5 

arq = 'arquivo.txt'
nomes = ['robin\n','mulher maravilha\n','superman\n']
with open(arq,"a") as arquivo:
	arquivo.write(nomes)

#####

#ESCREVER NO FINAL DO ARQUIVO "a"
arq = 'arquivo.txt'
with open(arq,"a") as arquivo:
	arquivo.write('Lanterna Verde\n')

exit()
#####

#SOBRESCREVER TUDO POR BATMAN
arq = 'arquivo.txt'
with open(arq,"w") as arquivo:
	arquivo.write('Batman\n')

#####

#Adicionar tudo em uma lista
with open('arquivo.txt') as arquivo:
	linhas = arquivo.readlines()

print(linhas)

#####

with open('arquivo.txt') as arquivo:
	for linha in arquivo:
		print(linha)

#####

#LER E FECHAR AUTOMATICAMENTE
with open('arquivo.txt') as arquivo:
	conteudo = arquivo.read()
	print(conteudo)

#####

arquivo = open('arquivo.txt,"r')
print(arquivo.read())
arquivo.close()