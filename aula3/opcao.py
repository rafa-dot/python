#!/usr/bin/python3.5

#0 sair do sistema
#1 adicionar um cadastro (nome,cpd,estado)
#2 buscar um cadastro - (cpf)

# 1. perguntar se o usuario deseja adicionar um cadastro ou fechar o sistema oiu busca um cadastro
# 2. adicionar um cadastro contendo nome, cpf e estado)

def busca (cpf):
	dic = {}
	k = 0
	chaved = ['cpf','estado','nome']
	with open(arq,'r') as arquivo:
		for linha in arquivo:
			itens = linha.split('\t')

			itens[-1] = itens[-1][:-1] #corrigir o \n

			# for item in itens:
			# 	dic[chaved[k]] = item
			# 	# print
			# 	k += 1
			# 	if k == 3:
			# 		k = 0

		# if dic[chaved[0]] == cpf:
		# 	print("{}\t{}\t{}\n".format(dic[cpf,dic['estado'],dic[nome]]))

			if itens[0] == str(cpf):
				print("{}\t{}\t{}\n".format(itens[0],itens[1],itens[2]))
				break
		else:
			print('CPF não encontrado')


arq = 'arquivo.txt'

def cadastrar(**kwargs):
	with open(arq,'a') as arquivo:
		arquivo.write("{}\t{}\t{}\n".format(kwargs['cpf'],kwargs['nome'],kwargs['estado']))

	print('\nAdicionado com sucesso!')

while True:
	opt = int(input('Opções:\n0 - sair\n1 - cadastrar\n2 - buscar\n\nDigite a opção: '))
	if opt == 0:
		exit()
	elif opt == 1:
		lista = input('Digite'' nomem,estado,cpf: ').split(',')
		cadastrar(nome=lista[0],estado=lista[1],cpf=lista[2])
	else:
		cpf = input('cpf: ')
		busca(cpf)



















 