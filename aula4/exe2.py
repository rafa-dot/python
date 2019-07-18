#!/usr/bin/python3.5
class User():
	def __init__(self,nome,sobrenome,username,passwd):
		self.nome = nome
		self.sobrenome = sobrenome
		self.username = username
		self.passwd = passwd
		self.tentativas = 0

	def descrever(self):
		print('{} {}'.format(self.nome,self.sobrenome))

	def saudacao(self):
		print('Ola {} {}'.format(self.nome,self.sobrenome))

	def reseta_tentativas(self):
		self.tentativas = 0
		print('Tentativas: {}'.format(self.tentativas))

	def incrementa_tentativas(self):
		self.tentativas += 1
		print('Tentativas: {}'.format(self.tentativas))

	def login(self,usuario,senha):
		if usuario == self.username and senha == self.passwd:
			print('Logado com sucesso')
			self.reseta_tentativas()
		else:
			self.incrementa_tentativas()

batman = User('Bruce','wayne','batman','123')

while True:
	user = input('Digite usuario: ')
	senha = input('Digite senha: ')

	batman.login(user,senha)
