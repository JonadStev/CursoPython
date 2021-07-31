
arreglo = ["steven", "jose", "fracisco"]
# Indice        0       1        2

print("PRIMERA forma de recorrer un arreglo")
contador = 0
for i in arreglo:
    print(str(contador)+") "+i)
    contador += 1

print("SEGUNDA forma de recorrer un arreglo")
for i in range(len(arreglo)):
    print(str(i)+") "+arreglo[i])

print("TERCERA forma de recorrer un arreglo CON WHILE")
contador2 = 0
while contador2 < len(arreglo):
    print(str(contador2)+" "+arreglo[contador2])
    contador2 += 1

numero = 1
presentar = "Soy el programador numero "+str(numero)
print(presentar)
