import seaborn as sns
import numpy as np
import pandas as pd
import statistics 
from scipy import stats
import matplotlib.pyplot as plt
import csv  #este modulo me permite leer listas de datos en formato .csv y .txt
with open('datos.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        lote = list(reader)

mylist = [(lote[i][0]) for i in range(4999)]
#print(mylist)
#print(len(mylist))
lista = [float(j) for j in mylist]
lista.insert(0, 67.5142)


#esto es lo que me interesa para evaluar el modelo
a, b =stats.rayleigh.fit(lista)

print('mean=', str(a))
print('STD=', str(b))

model=stats.rayleigh(a,b)
print('P=', str(model.cdf(68)-model.cdf(61)))
#print(len(lista))

'''
ax=sns.distplot(lista, bins=50, fit=stats.rayleigh, color='y')

ax.set_ylabel('Probabilidad')
ax.legend(labels=['Rayleigh', 'distplot'])
#plt.show()
plt.savefig('nuevo.png')
'''


order=sorted(lista) #ordenar en forma ascendente 1, 2, 3 ....
listadoA=[i for i in order if i >= 61 and i <= 68] #mi carne es B66861
print(len(listadoA)) 
print('Prob=', str(len(listadoA)/5000))

m,s,v,k=model.stats(moments='msvk')

#momentos para el modelo
print('media=', model.stats(moments = 'm'))

print('skew=', model.stats(moments = 's'))


print('varianza=', model.stats(moments = 'v'))

print('kurtosis=', model.stats(moments = 'k'))

print('*****************************************************')
#momentos de los datos

print('media_2=', np.mean(lista))
print('skewness=', stats.skew(lista))
print('varianza=', statistics.variance(lista))
print('kurt_2=', stats.kurtosis(lista))
'''
N=5000
X=[0]*N
Y=[0]*N

for i in range(N):
  X[i]=lista[i]
  Y[i]=np.sqrt(X[i])
'''
#print(Y)

square=np.sqrt(lista)
HIST=plt.hist(square,50, color='#008000', alpha=0.7, rwidth=0.85)
#plt.grid(axis='y', alpha=0.75)
plt.xlim(left=0)
plt.xlim(right=12.5)
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.savefig('hist3.png')












'''
a,b,c=plt.hist(L,50, color='#FF0000', alpha=0.7, rwidth=0.85)
#plt.grid(axis='y', alpha=0.75)
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
'''
