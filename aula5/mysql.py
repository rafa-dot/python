
import MySQLdb

try:
	con = MySQLdb.connect(host='localhost', db='gotham', user='batman', password='Gotham@123')
	print('Conectou')
	cur = con.cursor()

except Exception as e:
	print('Erro: {}'.format(e))


# cur.execute('create table herois(id int primary key auto_increment, nome varchar(50), idade int);')
# cur.execute('insert into herois(nome,idade) values (\'batman\',80);')
# cur.execute('insert into herois(nome,idade) values (\'asa noturna\',30);')
cur.execute('update herois set nome=\'asa diurna\' where nome=\'asa noturna\';')
# cur.execute('delete from herois where nome=\'asa diurna\;')

cur.close()
con.commit()
con.close()