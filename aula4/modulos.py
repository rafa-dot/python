#!/usr/bin/python3.5
import time,random
from datetime import datetime
from subprocess import run, PIPE
from pasta.som import qual_nota

b = False

while b == False:
	f = random.randint(264,528)
	b = qual_nota(f) 

exit()



# r = run(['apt','install','-y','sl'],stdout = PIPE,stderr =PIPE)
# #print(r)

# r = run(['ls','-l'],stdout=PIPE, stderr=PIPE)
# #print(r)

# if r.retourncode != 0:
# 	print("Deu ruim")
# else:
# 	print('ok')

# k = 0
# while k != 505:
# 	k = random.randint(100,999)
# 	#print(k)

# vogais = 'aeiouAEIOU'
# print(random.choice(vogais)) #TEMPO PARA EXECUTAR O PROXIMO COMANDO
# time.sleep(1)
# print(random.choice(vogais))

# print(datetime.now())


