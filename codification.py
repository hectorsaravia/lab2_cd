def posRedundantBits(data):

	positions = [1,2,4,8,16,32,64,128,256]
    
	j = 0
	k = 1
	res = ''
    
	for i in range(1, 149):
		if(i == positions[j]):
			res = res + '0'
			j += 1
		else:
			res = res + data[-1 * k]
			k += 1

	return res[::-1]


def calcParityBits(arr, r):
	n = len(arr)
    
	for i in range(r):
		val = 0

		for j in range(1, n + 1):
			if(j & (2**i) == (2**i)):
				val = val ^ int(arr[-1 * j])

		arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
	return arr

# Ingrese el archivo a ser codificado
myfile = input('Ingrese el archivo a codificar, la salida será el archivo en bits codificado: ')

#se lee el archivo y se obtiene el string
f = open(myfile, 'r')
rawdata = f.read()
data = ''

#se transforma el archivo a un string de bits
for i in rawdata:
    temp = ord(i)
    temp = format(temp, 'b')
    data = data + temp

print('Linea sin codificar: ' ,data)

# Calcula los bits de redundancia
m = len(data)
r = 8

# Determine la posición de los bits de redundancia
arr = posRedundantBits(data)

# Determine the parity bits
arr = calcParityBits(arr, r)

# Data to be transferred
print('Linea codificada: ',arr)
