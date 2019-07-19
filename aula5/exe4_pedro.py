
# 0 Sair
# 1 buscar pelo nome
# 2 cadastrar
# 3 atualizar
# 4 deletar
# 5 criar tabela 'usuarios'
# 6 dropar tabela 'usuarios' 

import os
from funcoes import *

opções = {0:sair,1:busca,2:cadastro,3:atualização,4:delecao,5:cria_tabela,6:drop_tabela}

while True:
	try:
		os.system('clear')
		menu = open('menu.txt').read()
		print(menu)
		opt = int(input('Digite a opcao :'))
		opcoes[opt]()
		opt = int(input('precione qualquer tecla para contiuar :'))
	except KeyboardInterrupt:
		sair()
	except Exception as e:
		print(e)
