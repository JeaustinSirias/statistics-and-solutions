#UNIVERSIDAD DE COSTA RICA
#MODELOS PROBABILISTICOS DE SENALES Y SISTEMAS; GRUPO #1
#ESTUDIANTE: JEAUSTIN SIRIAS CHACON, CARNE B66861
#TAREA PROGRAMADA #1
#I SEMESTRE DE 2020



#+++++++++++++++++NOTA: DEBE CARGAR EL ARCHIVO 'lote.csv' EN EL MISMO DIRECTORIO DONDE ABRA ESTE .py+++++++++++++++++++++++++++


print("ELABORADO POR JEAUSTIN SIRIAS CHACON, CARNE B66861")
print("MODELOS PROBABILISTICOS DE SENALES Y SISTEMAS, GRUPO 1 TAREA 1")
#PREAUMBULO: CARGANDO EL ARCHIVO .csv e importado paquetes

import csv #este modulo me permite leer listas de datos en formato .csv y .txt
with open('lote.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        lote=list(reader) #convierto los datos .csv en una lista de elementos tipo string en la variable 'lote'.


espacio_muestral=len(lote) #estos son los 500 elementos del espacio de muestras del lote de produccion en una variable de tipo int
print("*********************************************************************")

while True: #defino un bucle infinito para asignar por menu cada inciso de la tarea
    
    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("Sabiendo que hay un lote de 500 elementos con caracteristica A, B, C Y D, entonces:") #ahora imprimame el espacio muestral en pantalla
    print("+Digite 1 para ver la probabilidad de ocurrencia en los eventos A, B, C y D")
    print("+Digite 2 para ver la probabilidad condicional de un evento dado otro")
    print("+Digite 3 para conocer si hay relaciones de dependencia o independencia entre los eventos")
    print("+Digite 4 para conocer la probabilidad de que D dado A ")
    print("+Digite 5 para finalizar el progama")
 
    entrada=input("VALOR A DIGITAR:")
    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")


    if entrada == 1: #***********PROBLEMA 1:Cual es la probabilidad de ocurrencia de cada caracteristica?



        count0=0 #Agrego este contador para evitar lineas de codigo repetidas para cada caracteristica y en lugar, usar la instruccion elif
        for j in [2,3,4,5]: #Este sera un bucle para evaluar las columnas de caracteristicas A:2, B:3, C:4 Y D:5
            count0 += 1
            elementos_favorables=0 #defino un contador auxiliar que me diga cuantos elementos son favorables en cada caracteristica
            for i in range(500): #Para un espacio de 500 elementos por cada columna A, B, C y D, indiqueme cuantos de ellos tienen un '1'   
                value=lote[i-1][j-1] #digame el valor puntual en la i-esima columna para la j-esima fila
                if value == '1': #si el valor puntual es 1 entonces aumente el contador en 1 hasta llegar al elemento 500 de la columna en proceso
                    elementos_favorables += 1
                    probabilidad = (elementos_favorables*1.0)/espacio_muestral # ejecute la probabilidad de ocurrencia para la i-esima columna (caracteristica)

            #Imprima en pantalla la probabilidad de ocurrencia y el numero de eventos favorables para cada caracteristica A, B, C o D
            if count0 == 1:
                PA=probabilidad
                print("El numero de resultados favorables de la caracteristica A es:" + " " +str(elementos_favorables)) #imprima en pantalla la probabilidad de ocurrencia de A
                print("La probabilidad de ocurrencia en A es:" + " " + str(PA))
                print("*********************************************************************")
            elif count0 == 2:
                PB=probabilidad
                print("El numero de resultados favorables de la caracteristica B es:" + " " +str(elementos_favorables)) #imprima en pantalla la probabilidad de ocurrencia de B
                print("La probabilidad de ocurrencia en B es:" + " " + str(PB))
                print("*********************************************************************")
            elif count0 == 3:
                PC=probabilidad
                print("El numero de resultados favorables de la caracteristica C es:" + " " +str(elementos_favorables)) #imprima en pantalla la probabilidad de ocurrencia de C
                print("La probabilidad de ocurrencia en C es:" + " " + str(PC))
                print("*********************************************************************")
            elif count0 == 4:
                PD=probabilidad
                print("El numero de resultados favorables de la caracteristica D es:" + " " +str(elementos_favorables)) #imprima en pantalla la probabilidad de ocurrencia de D
                print("La probabilidad de ocurrencia en D es:" + " " + str(PD))
                print("*********************************************************************")



#**********************ACTIVIDAD #2: En todos los pares posibles, cual es la probabilidad de una caracterastica dado otra? Ejemplo: P(C | D)*****************************

    elif entrada == 2:
        #Primero buscamos las combinaciones posibles por pares         
        comb=["A", "B", "C", "D"]
        print("Los pares de combinaciones posibles entre las caracteristicas A, B, C y D son:")
        for n in comb:
            for m in comb: #conjunto de for anidados para obtener la combinatoria
                if n != m: # excluya elementos repetidos
                    print (n,m) #deme todas las combinaciones posibles en pares entre los elementos A, B, C y D sin repetirse


        listRef=list(range(0,500)) #asigne una lista generica de referencia posicional de 500 elementos tipo int
        counter=0
        for z in [2, 3, 4, 5]:
            counter += 1
            mylist=[(lote[i-1][z-1]) for i in range(500)] #para las columnas de A, B, C y D del .csv cree una lista por separado para cada una con su contenido

            #Para cada columna listada comparela con la lista de referencia listRef y deje solo los valores posicionales que tienen un 1 y elimine los ceros
            # la funcion set() me va a convertir las listas filtradas en conjuntos {elementos}
            if counter == 1:
                lista=[int(j) for j in mylist]
                products = [a * b for a, b in zip(listRef, lista)]  #para obtener la lista de solo las posiciones de elementos favorables de la caracteristica A
                listadoA=[i for i in products if i != 0]
                A=set(listadoA)

            elif counter == 2:
                lista=[int(j) for j in mylist]
                products = [a * b for a, b in zip(listRef, lista)] #para obtener la lista de solo las posiciones de elementos favorables de la caracteristica B
                listadoB=[i for i in products if i != 0]
                B=set(listadoB)

            elif counter == 3:
                lista=[int(j) for j in mylist]
                products = [a * b for a, b in zip(listRef, lista)] #para obtener la lista de solo las posiciones de elementos favorables de la caracteristica C
                listadoC=[i for i in products if i != 0]
                C=set(listadoC)

            elif counter == 4:
                lista=[int(j) for j in mylist]
                products = [a * b for a, b in zip(listRef, lista)] #para obtener la lista de solo las posiciones de elementos favorables de la caracteristica D
                listadoD=[i for i in products if i != 0]
                D=set(listadoD)



        print("Las probabilidades condicionales posibles de una caracteristica dada otra son:")
        combs=0
        for s in A, B, C, D:
            for q in A, B, C, D: #Elabore la combitatoria por pares ahora con los conjuntos definidos anteriormente 
                if s != q:
                    combs += 1
                    z=s.intersection(q) #Haga la interseccion (s & q) de los conjuntos de cada combinacion de pares posible 
                    z1=len(z) # cuente el numero de elementos coincidentes en cada interseccion de los pares posibles
                    z2=(z1*1.0)/espacio_muestral #haga la operacion P(s & q) para cada interseccion en los pares posibles


                    #Para cada probabilidad P(s & q) dada calculeme la probabilidad condicional P(s|q) e imprima en pantalla cada resultado
                    if combs == 1:
                        print("P(B|A)="+str(z2/0.694))
                    elif combs == 2:
                        print("P(C|A)="+str(z2/0.694))
                    elif combs == 3:
                         print("P(D|A)="+str(z2/0.694))
                    elif combs == 4:
                         print("P(A|B)="+str(z2/0.306))
                    elif combs == 5:
                         print("P(C|B)="+str(z2/0.306))
                    elif combs == 6:
                         print("P(D|B)="+str(z2/0.306))
                    elif combs == 7:
                         print("P(A|C)="+str(z2/0.404))
                    elif combs == 8: 
                         print("P(B|C)="+str(z2/0.404))
                    elif combs == 9:
                         print("P(D|C)="+str(z2/0.404))
                    elif combs == 10:
                         print("P(A|D)="+str(z2/0.596))
                    elif combs == 11:
                         print("P(B|D)="+str(z2/0.596))
                    elif combs == 12:
                        print("P(C|D)="+str(z2/0.596))
    elif entrada ==3: #dos caracteristicas p y q son independientes si P(p|q)=P(p)

        print("Los pares de caracteristicas con relacion independiente son:")
        print("C|A")
        print("D|A")
        print("C|B")
        print("D|B")
        print("A|C")
        print("B|C")
        print("A|D")
        print("B|D")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Los pares de caracteristicas con relacion dependendiente son:")
        print("A|B")
        print("B|A")
        print("C|D")
        print("D|C")


    

    elif entrada == 4: #usando el arbol ramal de probabilidades se determina que P(A|D)=P(D|A)P(A)/(P(D|A)P(A)+P(D|B)P(B))
       
        pAD=(0.694*0.608069164265)/(0.694*0.608069164265+0.306*0.56862745098)
        print("La probabilidad de que la caracteristica D tambien la tenga A es:"+str(pAD))

    elif entrada == 5:
        print("+++++++++EL PROGRAMA HA FINALIZADO+++++++++")
        break;
                   

















    

        
        






