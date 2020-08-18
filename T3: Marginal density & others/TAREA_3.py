#UNIVERSIDAD DE COSTA RICA
#MODELOS PROBRABILISTICOS DE SENALES Y SISTEMAS, GRUPO #01
#UNA SOLUCION PROGRAMADA A LA TAREA 3
#ELABORADA POR JEAUSTIN SIRIAS CHACON, CARNE B66861
#I-2020

#import seaborn as sb
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit	#IMPORTAMOS LAS LIBRERIAS DE NOS SON DE INTERES
import scipy.stats as stats
import math


with open('xy.csv', 'r') as file:
    reader = csv.reader(file)		#IMPORTAMOS EL FRASCO DE DATOS
    for row in reader:
        lote = list(reader)

with open('xyp.csv', 'r') as file:
	reader1 = csv.reader(file)	#IMPORTAMOS EL FRASCO DE DATOS EN ORDEN DE COLUMNA X, Y, P
	for row in reader1:
		listado = list(reader1)



#******************************************INCISO #1

#PARA HALLAR LA FUNCION DE DENSIDAD MARGINAL EN X
lst=[]
for i in range(0,11):
	mylist = [(lote[i][j]) for j in range(0,21)]
	lista = [float(j) for j in mylist]		#creamos un vector fila para los X
	lst.append(lista)

Xsum = []
for i in range(0,11):	#sumamos el vector fila X
	P=sum(lst[i])
	Xsum.append(P)
	#Xsum es la funcion de densidad marginal en X

print(Xsum) #Xsum es el vector de puntos de la de densidad marginal en X a partir de los datos

#PARA HALLAR LA FUNCION DE DENSIDAD MARGINAL EN Y
Ylst=[]
for j in range(0,21):
	mylistY = [(lote[i][j]) for i in range(0,11)]
	listaY = [float(j) for j in mylistY]
	Ylst.append(listaY)

Ysum = []
for i in range(0,21):
	Q=sum(Ylst[i])
	Ysum.append(Q)

print(Ysum)	#Ysum es el vector de puntos de la de densidad marginal en Y a partir de los datos

#ESTOS VECTORES X, Y son un linspace
X=range(5, 16)
Y=range(5,26)

#PLOTEAMOS AMBAS FUNCIONES DE DENSIDAD MARGINAL Y VEMOS QUE SE ASEMEJAN A LA DISTRIBUCION NORMAL


plt.plot(Y, Ysum, label = 'Densidad marginal en Y', color = 'y')
plt.plot(X, Xsum, label = 'Densidad marginal en X')
plt.xlabel('Muestras')
plt.ylabel('Probabilidad')
plt.legend(framealpha=1, frameon=True);
#plt.savefig('MarginalesXY.png')
plt.show()


#GENERAMOS UNA FUNCION DE DISTRIBUCION NORMAL
def gaussian(x, mu, sigma): #x: es la muestra de datos, mu: es la media, sigma: desv. estandar
    return (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(x-mu)**2/(2*sigma**2))

#usamos la funcion curve_fit de scipy para hallar mu y sigma para los modelos de la marginal en X y Y
param1, _ = curve_fit(gaussian, X, Xsum)
param2, _ = curve_fit(gaussian, Y, Ysum)
print('Los parametros mu y sigma para X son:' + str(param1))
print('Los parametros mu y sigma para Y son:' + str(param2))

#*****************************************INCISO #2

#LA FUNCION DE DE DENSIDAD CONJUNTA QUE MODELA LOS DATOS ES:

def densidad_conjunta(x, y):
  return 0.008*np.exp((-(x-9.905)**2)/21.773)*np.exp((-(y-15.079)**2)/72.648)



#******************************************INCISO #3

#VAMOS A HALLAR LA CORRELACION

Plst = []
for i in range(0, 231):
	array = listado[i]
	listZ = [float(j) for j in array] #CONVERTIMOS EN FLOATS LOS ELEMENTOS DEL FRASCO xyp.csv COMO UNA LISTA en la variable 'Plst'
	Plst.append(listZ)

#print(Plst)


product = []
for i in range(0, 231):
	result1 = np.prod(Plst[i]) #MULTIPLICAMOS TODAS LAS FILAS DE LA LISTA Y GUARDAMOS EL RESULTADO EN product
	product.append(result1)

correlacion = sum(product)	#la correlacion en la suma de todos los productos que ahora son elementos en 'product'

print('La correlacion es:' + str(correlacion)) #IMPRIMA LA CORRELACION


#VAMOS A HALLAR LA COVARIANZA [SUM][SUM](x - X)(y - Y)f(x,y) = covarianza
for i in range(0,231):
	#agarramos 'xyp.csv' como float en lista y le restamos a la columna x la Xmu y en la columna y, la Ymu de los modelos
	Plst[i][0] = Plst[i][0] - 9.90484381 #9.904... es la media del modelo gaussiano de la densidad marginal en X
	Plst[i][1] = Plst[i][1] - 15.0794609 #15.079... es la media del modelo gaussiano de la densidad marginal en Y

#print(Plst)

#Ahora ejecutamos el producto en cada fila y lo guardamos en una nueva lista 'covarianza_prod'
covarianza_prod=[]
for i in range (0,231):
  #np.prod(Plst[i])
  covarianza_prod.append(np.prod(Plst[i]))

covarianza = sum(covarianza_prod) #hacemos la sumatoria de los elementos
print('La covarianza es:' + str(covarianza)) #IMPRIMA LA COVARIANZA

#VAMOS A HALLAR EL COEFICIENTE DE PEARSON = COVARIAZA/des_estandarX * desv_estandarY
pearson = covarianza/(3.29944286*6.02639775)
print('El coeficiente de Pearson es:' +  str(pearson)) #IMPRIMA EL COEFICIENTE DE PEARSON

'''
#*********************************INCISO 4: GRAFICAS PARA LAS FUNCIONES DE DENSIDAD MARGINALES, SUS MODELOS Y DENSIDAD CONJUNTA


plt.plot(X, Xsum, label = 'Densidad marginal en X', color = 'b')
mu=9.90484381
sigma=3.29944286
plt.plot(X, stats.norm.pdf(X, mu, sigma), label = 'Modelo Gausseano', color = 'r')	#DENSIDAD MARGINAL EN X A PARTIR DEL MODELO GAUSSEANO
plt.xlabel('muestras')
plt.ylabel('Probabilidad')
plt.legend(framealpha=1, frameon=True);
plt.savefig('GausseanaX.png')
plt.show()




plt.plot(Y, Ysum, label = 'Densidad marginal en Y', color = 'b')
mu=15.0794609
sigma=6.02693775
plt.plot(Y, stats.norm.pdf(Y, mu, sigma), label = 'Modelo Gausseano', color = 'g')	#DENSIDAD MARGINAL EN Y A PARTIR DEL MODELO GAUSSEANO
plt.xlabel('Datos')
plt.ylabel('Probabilidad')
plt.legend(framealpha=1, frameon=True);
plt.savefig('GausseanaY.png')
plt.show()


#DENSIDAD CONJUNTA

x=range(5, 16)
y=range(5,26)

X, Y = np.meshgrid(x, y)
Z = densidad_conjunta(X, Y)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_wireframe(X, Y, Z, color='red')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.savefig('DenConjuntaXY.png')
plt.show()
'''
