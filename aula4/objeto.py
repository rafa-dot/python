#!/usr/bin/python3.5

class Carro():
	def __init__(self,marca,modelo,ano):
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.hodometro = 0

	def descrever(self):
		print('{} {} {}'.format(self.marca,self.modelo,self.ano,))

	def ler_hodometro(self):
		print('Esse carro rodou {} km'.format(self.hodometro))

	def atualiza_hodometro(self,kms):
		if kms >= self.hodometro:
			self.hodometro = kms
		else:
			print('Não é possivel diminuir km')

	def incrementa_hodometro(self,kms):
		if kms >= 0:
			self.hodometro += kms
		else:
			print('não é possivel diminuir km')

class Eletrico(carro):
	def __init__(self,marca,modelo,ano):
		super().__init__(marca,modelo,ano) #herança
		self.bateria = 0

	def descrever_bateria(self):
		print('bateria> {}'.format(self.bateria))

	def enche_tanque(self):
		print('Esse carro é eletrico')

c1 = Carro('VW','fusca','1980')
c2 = Eletrico('Tesla','model','2016')

print('c1: {}'.format(c1.gasolina))
c1.enche_tanque()
print('c1: {}'.format(c1.gasolina))

c2.descrever_bateria()
print('c2 '{}.format(c2.gasolina))
c2.enche_tanque()

meu_carro = Carro('VW','fusca','1980')
meu_carro.descrever()
meu_carro.atualiza_hodometro(30000)
meu_carro.ler_hodometro()
meu_carro.incrementa_hodometro(100)
meu_carro.ler_hodometro()

exit()