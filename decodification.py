
# Ingrese el texto binario a ser codificado
arr = input('Ingrese el texto binario a decodificar, la salida será el texto en bits decodificado: ')
print(arr)
m = len(arr)
r = 8


arr = arr[::-1]
res = ''
positions=[128,64,32,16,8,4,2,1,0]
j=0
for i in range(148,0,-1):
	if i != positions[j]:
		res = res + arr[i-1]
	else:	
		j+=1

print(res)
