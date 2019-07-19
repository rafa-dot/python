# from conexao import + 

def cria_tabela():
	cur.execute('create table usuarios(id int primary key auto_increment, nome varchar(50), cpf int, estado char(2);')

def drop_tabela():
	cur.execute('drop table usuarios')
	print('tabela dropada')

def busca():
	nome = input('Digite nome: ')
	cur.execute('select * from usuarios where nome=\'{}\':'.format(nome))
	tuplas = cur.fetchall()

	for k in tuplas:
		print('{}'.format(k))

def cadastro():
	nome = input('Digite nome: ')
	cpf = input('Digite cpf: ')
	estado = input('Digite estado: ')

	query = 'selec * from usuarios where cpf={}'.format(cpf)

	if cur.execute(query):
		print('Cadastro existente')
	else:
		cur.execute('insert into usuarios(nome,cpf,estado) values (\'{}\',{}\'{}\');'.format(nome,cpf,estado))
	con.commit()

def atualização():
	while True:
		uid = input('uid: ')
		print('1 - nome\n2- cpf\n3 - estado')
	o = int(input('Digite: '))

	if o == 1:
		nome = input('Digite nome: ')
		cur.execute('update usuarios set nome =\'{}\' where id={};'.format(nome,uid))
	elif o == 2:
		cpf = int(input('digite cpf: '))
		cur.execute('update usuarios set cpf={} where id={};'.format(cpf,uid))
	else:
		estado = input('digite o estado: ')
		cur.execute('update usuarios set estado=\'{}\' where id={};'.format(estado,uid))

	con.commit()

def delecao():
	while True:
		uid = int(input('uid: '))

	cur.execute('delete from usuarios where id={}'.format(uid))
	con.commit()

def sair():
	print('saindo')
	exit()