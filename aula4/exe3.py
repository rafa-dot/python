#!/usr/bin/python3.5
# Dado o cenario abaixo abstraia uma conta bancaria
# utilizando programação orientada a objetos
# crie metodos para transferencia saque e deposito
# e utilize herança se necessario também.

# joao possuia 30k em sua CC e uma poupamça com saldo zerado, 
# então ele transferiu 3k para CC de maria que ja possuia 2k 
# em sua CC e depois disso joao transferiu 5k para sua poupança
# apos um mes a poupanca de joao rendeu 0.6% do valor de seu saldo

class Conta():
	def __init__(self,titular,numero,saldo):
		self.titular = titular
		self.numero = numero
		self.saldo = saldo

	def descrever(self):
		print(('Titular: {}\nCC: {}\nSaldo: {}\n').format(self.titular,self.numero,self.saldo))

	def saque(self,valor):
		self.saldo -= valor
		return self.saldo

	def deposito(self,valor):
		self.saldo += valor
		return self.saldo

	def transferir(self,valor,conta):
		self.sque(Valor)
		conta.deposito(Valor)

class Poupanca(Conta):
	def __init__(self,titular,numero,saldo):
		super().__init(titular,numero,saldo)
		self.juros = 1.006

	def descrever(self):
		print(('Titular: {}\nPoupanca: {}\n Saldo: {}\n').format(self.titular,self.numero,self.saldo))

	def render(self):
		self.saldo *= self.juros
		return self.saldo

	



















