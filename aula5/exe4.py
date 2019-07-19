
# 0 Sair
# 1 buscar pelo nome
# 2 cadastrar
# 3 atualizar
# 4 deletar
# 5 criar tabela 'usuarios'
# 6 dropar tabela 'usuarios' 




import MySQLdb

try:
	con = MySQLdb.connect(host='localhost', db='gotham', user='batman', password='Gotham@123')
	print('Conectou')
	cur = con.cursor()

except Exception as e:
	print('Erro: {}'.format(e))

while True:
	opcao = int(input('opções:\n0 - Sair\n1 - Buscar nome\n2 - Cadastrar\n3 - Atualizar\n4 - Deletar\n5 - Cria tabela usuarios\n6 - Deletar tabela usuarios\nDigite: '))
	if opcao == 0:
		exit()
	elif opcao == 1:
		nome = input('Digite o nome procurado: ')


# print(opcao)