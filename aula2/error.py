#!/usr/bin/python3.5 



######

exit()

while True:
	n1 = int(input("Digite: "))
	n2 = int(input("Digite: "))

	try:
		r = n1/n2

	except ZeroDivisionError as e:
		print("imposivel dividir por zero")

	else:
		print(r)

exit()
try:
	print(5/0)
except ZeroDivisionError as e:
	print("erro: {}".format(e))