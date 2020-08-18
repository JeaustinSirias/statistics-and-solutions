UNA SOLUCION A LA TAREA 3 POR JEAUSTIN SIRIAS
=============================================

Para clonar este repositorio en su computadora usando una distribucion GNU/LINUX [bash](https://es.wikipedia.org/wiki/Bash) copie y pegue la siguiente linea en su terminal:


	git clone https://github.com/JeaustinSirias/Tarea3_B66861.git

Si no cuenta con el paquete [git](https://git-scm.com/) en su ordenador, entonces digite las siguientes lineas en la terminal:

	sudo apt-get update
	sudo apt-get install git

Una vez clonado puede encontrar el codigo fuente en el archivo [TAREA_3.py](https://github.com/JeaustinSirias/Tarea3_B66861/blob/master/TAREA_3.py). Recuerde correrlo si cuenta con las siguientes librerias instaladas en su interprete de Python3:

	import csv
	import matplotlib.pyplot as plt
	import numpy as np
	from scipy.optimize import curve_fit
	import scipy.stats as stats
	import math

### Un breve resumen:

Este repositorio corresponde a la Tarea 3 del curso Modelos Probabilisticos de Senales y Sistemas de la Escuela de Ingenieria Electrica en la Universidad de Costa Rica para el I-2020. Se presenta una solucion programada para aplicar los conceptos de funcion de densidad marginal, independencia, funcion de densidad conjunta, correlacion, covarianza y coeficiente de Pearson, a partir de un frasco de datos con registros de frecuencia relativa.


### INCISO 1: MODELOS PROBABILISTICOS HALLADOS PARA LAS FUNCIONES DE DENSIDAD MARGINALES EN X, Y

Se han definido los modelos a partir de hallar los parametros 'mu' y 'sigma' de la distribucion normal/gausseana a partir de implementar una funcion en Python3 como sigue:


	def gaussian(x, mu, sigma):
    		return (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(x-mu)**2/(2*sigma**2))


Las curvas de los datos crudos para X y Y puede apreciarlas en el archivo en .png presente en este repositorio, con el nombre [MarginalesXY.png](https://github.com/JeaustinSirias/Tarea3_B66861/blob/master/MarginalesXY.png). A partir de las siguientes lineas se comparan las frecuencias relativas en X y X para obtener los parametros de los modelos:
	
	X=range(5, 16) 
	Y=range(5,26)
	param1, _ = curve_fit(gaussian, X, Xsum) 
	param2, _ = curve_fit(gaussian, Y, Ysum)

Los resultados obtenidos son un par de vectores de la forma [mu, sigma] para la densidad marginal en X y en Y, respectivamente: [9.904843, 3.299443], [15.079460, 6.029377]


### INCISO 2: ASUMIENDO INDEPENDENCIA EN X,Y HALLAR LA FUNCION DE DENSIDAD CONJUNTA

A partir de los [conceptos estudiados](https://es.wikipedia.org/wiki/Distribuci%C3%B3n_conjunta) se determina que la funcion de densidad conjunta es el producto de los modelos gausseanos marginales encontrados anteriormente:'

	fXY(x, y) = fX(x) * fY(y) 
	fXY(x, y) = 0.008*np.exp((-(x-9.905)**2)/21.773)*np.exp((-(y-15.079)**2)/72.648)
		
Este desarrollo puede observase de forma [grafica](https://github.com/JeaustinSirias/Tarea3_B66861/blob/master/DenConjuntaXY.png) en el repositorio.

### INCISO 3: HALLANDO LA CORRELACION, LA COVARIANZA Y EL COEFICIENTE DE PEARSON

#### CORRELACION

Para este apartado se calcula la [correlacion](https://es.wikipedia.org/wiki/Correlaci%C3%B3n) a partir del frasco de datos 'xyp.csv' dado a que tiene una organizacion [x y p], de este modo se busca realizar el producto de cada fila y sumar los elementos resultantes; para ello se hizo el siguiente procedimiento progamado:

	Plst = []
	for i in range(0, 231):
		array = listado[i]
		listZ = [float(j) for j in array] #CONVERTIMOS EN FLOATS LOS ELEMENTOS DEL FRASCO xyp.csv COMO UNA LISTA en la variable 'Plst'
		Plst.append(listZ)


	product = []
		for i in range(0, 231):
		result1 = np.prod(Plst[i]) #MULTIPLICAMOS TODAS LAS FILAS DE LA LISTA Y GUARDAMOS EL RESULTADO EN product
		product.append(result1)

	correlacion = sum(product)	#la correlacion en la suma de todos los productos que ahora son elementos en 'product'

Al final la correlacion arroja un valor de 149.5428 La interpretacion de este valor depende del valor del coeficiente de relacion de Pearson que se expone a continuacion.

#### COVARIANZA

Para hallar la [covarianza](https://es.wikipedia.org/wiki/Covarianza#:~:text=En%20probabilidad%20y%20estad%C3%ADstica%2C%20la,aleatorias%20respecto%20a%20sus%20medias.) se usa la formula para el caso discreto en sumatoria [SUM][SUM](x - Xmu)(y - Ymu)f(x,y) = covarianza; Xmu y Ymu son las medias respectivas halladas en los modelos marginales gausseanos. En Python3 a partir de los datos 'xyp.csv' se programa bajo las siguientes lineas:

	for i in range(0,231):
		#agarramos 'xyp.csv' como float en lista y le restamos a la columna x la Xmu y en la columna y, la Ymu de los modelos
		Plst[i][0] = Plst[i][0] - 9.90484381 #9.904... es la media del modelo gaussiano de la densidad marginal en X
		Plst[i][1] = Plst[i][1] - 15.0794609 #15.079... es la media del modelo gaussiano de la densidad marginal en Y 


	#Ahora ejecutamos el producto en cada fila y lo guardamos en una nueva lista 'covarianza_prod'
	covarianza_prod=[]
	for i in range (0,231):
  		covarianza_prod.append(np.prod(Plst[i]))
	covarianza = sum(covarianza_prod) #hacemos la sumatoria de los elementos 

Al final el valor de la covarianza es 0.066691. La covarianza para este caso es mayor que cero, por lo que se interpreta como una dependencia positiva: valores grandes de la variable aleatoria de X se asocian tambien a valores grandes de la VA en Y; es decir, una es proporcional a la otra.

#### COEFICIENTE DE PEARSON

El [Coeficiente de Pearson](https://es.wikipedia.org/wiki/Coeficiente_de_correlaci%C3%B3n_de_Pearson) se puede obtener a partir de la covarianza y las desviaciones estandar Xsigma y Ysigma halladas en los modelos marginales Gausseanos del INCISO 1 analiticamente como PEARSON = COVARIAZA/des_estandarX * desv_estandarY. De forma programada entonces:

	pearson = covarianza/(3.29944286*6.02639775)
	print('El coeficiente de Pearson es:' +  str(pearson)) #IMPRIMA EL COEFICIENTE DE PEARSON

Al final el coeficiente de Pearson es 0.0033540. Como dicho parametro se halla entre 0 y 1, entonces segun la [interpretacion](https://support.minitab.com/es-mx/minitab/18/help-and-how-to/statistics/basic-statistics/how-to/correlation/interpret-the-results/key-results/) significa que hay correlacion directa o positiva, pero moderada.
### INCISO 4: GRAFICAS

Se despliegan las graficas de interes para los datos crudos, los modelos gausseanos y la densidad marginal:

- [Graficas de densidad marginal a partir de los datos crudos](https://github.com/JeaustinSirias/Tarea3_B66861/blob/master/MarginalesXY.png)
- [Modelo gausseano a partir de la densidad marginal en X](https://github.com/JeaustinSirias/Tarea3_B66861/blob/master/GausseanaX.png)
- [Modelo gausseano a partir de la densidad marginal en Y](https://github.com/JeaustinSirias/Tarea3_B66861/blob/master/GausseanaY.png)
- [Modelo de densidad conjunta](https://github.com/JeaustinSirias/Tarea3_B66861/blob/master/DenConjuntaXY.png)


