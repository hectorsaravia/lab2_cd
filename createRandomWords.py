import random

#utilizacion de la seed basada en la hora del pc
random.seed()

#se crea la lista que va a contener las 30 palabras de 20 caracteres
seq = []

#for para crear los 30 archivos
for i in range (0,30):
    
    #se obtienen 20 caracteres pseudo-aleatorios
    randomCharacterList = random.choices('abcdefghijklmnopqrstuvwxyz', k = 20)
    myWord = ""

    #se conforma la palabra con los caracteres
    for k in range (len(randomCharacterList)):
        myWord = myWord + randomCharacterList[k]
    print(myWord)
    
    #newFile es el string con el nombre del archivo a crear. ejemplo: file 0, file 1...
    newFile = "file {}".format(i)

    #se abre, escribe y posteriormente se cierra el archivo
    f = open(newFile, "w")
    f.write(myWord)
    f.close()