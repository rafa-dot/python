
import psycopg2

try:
	con = psycopg2.connect('host=localhost dbname=gotham user=robin password=gotham123')
	print('Conectou')
	cur = con.cursor()

except Exception as e:
	print('Erro: {}'.format(e))

cur.execute('create table herois(id serial, nome varchar(50), idade int);')
cur.execute('insert into herois(nome,idade) values (\'batman\',80);')
cur.execute('insert into herois(nome,idade) values (\'asa noturna\',30);')
