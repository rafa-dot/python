#!/usr/bin/python3.5

def quadrado (n):
	return n ** 2
def raiz(n):
	return n ** (0.5)

f = [quadrado,raiz]

for k in range(0,26):
	valores = list(map(lambda x : x(k), f))
	print(valores)

print('\n')

[print(list(map(lambda x : x(k),f))) for k in range(0,26)]


exit()

n1 = [1,2,3]
n2 = [4,5,6]

r = list(map(lambda x,y : x * y, n1,n2))
print(r)

exit()

import math

l1 = [1,4,9,16,25]
l2 = list(map(math.sqrt, l1))
print(l2)

exit()
def dobro(b):
	return 2 * n

num = (1,2,3,4,5)
r = list(map(dobro,num))
print(r)

exit()

# exemplo 2
tamanhp = lambda frasee : [len(palavra) for palavra in frase]

frase = 'joao foi para a escola'.split()
print(tamanho(frase))

#exemplo 1
def tamanho(frase):
	return [len(palavra) for palavra in frase]

frase = 'joao foi para a escola'.split()
print(frases)
print(tamanho(frase))

exit()

def multiplica(n):
	return lambda a : a * n

dobro = multiplica(2)
triplo = multiplica()

print(dobro(12))
print(triplo(12))

exit()
x = lambda a,b : a + b
a = x(5,3)
print(a)

exit()

def exemplo(a):
	return a + 10

x = lambda a : a + 10

print(x(5))

#########
exit()

calcula = {
	'+' : lambda x,y : x + y,
	'-' : lambda x,y : x - y,
	'/' : lambda x,y : x / y,
	'*' : lambda x,y : x * y,
}
operadores = '+-*/'
operacao = input('Digite: ')

for k in operacao:
	if k in operadores:
		o = k
		a,b = operacao.split(k)
		a = int(a)
		b = int(b)

print(calcula[o(a,b)])
exit()



