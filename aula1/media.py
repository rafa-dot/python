#!/usr/bin/python3.5 

# Aluno tem 4 notas , calcuular a media
# nome do aluno - input
# calcular a media 
# printar nome do aluno + media

aluno = input('Nome: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))
media1 = nota1+nota2+nota3+nota4
media2 = media1 / 4
print('Aluno '+str(aluno)+' média '+str(media2))

exit()