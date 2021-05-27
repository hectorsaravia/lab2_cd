#script que añade errores basada en probabilidad

import random

#utilizacion de la seed basada en la hora del pc
random.seed()

#se ingresa un valor para probabilidad
prob_rang = True
while(prob_rang):
    prob = input('Añada probabilidad de error: ')
    try:
        prob = float(prob)
        if (prob <= 0 or prob >= 1):
            print('No está en el rango permitido')
        else:
            prob_rang = False
    except:
        print('Valor ingresado incorrecto')


#se crean listas vacías, una con cada caracter de todos los archivos
seq = input('Ingrese bits a añadir error: ')
newSeq = ''

#bucle for que busca los 30 archivos y los guarda en la lista seq en bits

#se cambian los caracteres basados en la probabilidad
for i in range(len(seq)):        
    randomSelected = random.choices([True, False] , [prob, 1-prob])
    if randomSelected == [True]:
        if seq[i]=='0':
            newSeq = newSeq + '1'
        else:
            newSeq = newSeq + '0'
    else:
        newSeq = newSeq + seq[i]

print(seq)
print(newSeq)