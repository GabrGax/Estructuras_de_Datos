import numpy as np
import random
# 30 REPRESENTANTES
arreglo = np.empty(30)

print("PROGRAMA QUE REALIZA UNA VOTACION ALEATORIA Y ORDENA LOS REPRESENTANTES ")
print("----------------------------------------------------------------------")
#VOTAR
for n in range(5000):
    numero_aleatorio = random.randint(0, 29)
    arreglo[numero_aleatorio]= arreglo[numero_aleatorio]+1;

#print(arreglo);

arreglo.sort
representantes = np.argsort(arreglo)[::-1]

for i in range(30):
    print("El representante numero ", representantes[i], "obtuvo ", arreglo[representantes[i]] , "votos ")



print("GABRIEL DAVID CASTILLO RODRIGUEZ --- 2220055")
