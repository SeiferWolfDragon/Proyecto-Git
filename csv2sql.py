import csv
import json
import time
#import SQL

from pathlib import Path
Conf=None
with open("configuracion.json") as jsonfile:
    Conf=json.load(jsonfile)
ArchivoEntrada=Conf['ArchivoEntrada']#lleva corchete porqu estamos en diccionario
ArchivoSalida=Conf['ArchivoSalida']
Tabla=Conf['Tabla']
Columnas=Conf["Columnas"]


#############Definir cuales son las columnas a usar
def numColumna():
    contadorcol=0
    for c in Columnas:
        contadorcol+=1
        #print(c["posicion"],c["tipo"])
    #print(contadorcol)
    return contadorcol
    #return  #(c["posicion"])

def numFilas():
    contadorlinea = 0
    RutaArchivoEntrada = Path(ArchivoEntrada)
    with RutaArchivoEntrada.open() as archivocsv:
        lectorCSV = csv.reader(archivocsv, delimiter=',')
        archivocsv.readline()
        for fila in lectorCSV:
            contadorlinea += 1
    #print(contadorlinea)
    return contadorlinea
    #return contador

############definir la cantidad de inserts a usar (deben ser 19)

def dictArray():
    for c in Columnas:
        Lista.append([c["posicion"], c["tipo"]])

def crearFilas():

    RutaArchivoEntrada = Path(ArchivoEntrada)
    with RutaArchivoEntrada.open() as archivocsv:
        archivocsv.readline()
        LectorCSV = csv.reader(archivocsv, delimiter=',')
        for fila in LectorCSV:
            Filas.append(fila)
"""  for i in range(0,len(Filas),1):
            for j in range(0,len(Lista),1):
                dato=Lista[j][0]
                print(Filas[i][dato], end=" ")
                time.sleep(0.5)"""


def convCadaInt(Cad):
    if Cad == '':
        Cad = '0'
    return int(Cad)

def imprimir(a,b):
    dato = Lista[b][0]
    if (Lista[b][1] == "Entero"):
       # print(convCadaInt(Filas[i][dato].replace(",", "").replace("22 ", "")), end=" ")
        return convCadaInt(Filas[a][dato].replace(",", "").replace("22 ", ""))
    else:
       #print('"' + str(Filas[i][dato].replace(",", "")) + '"', end=" ")
        return '"' + str(Filas[a][dato].replace(",", "")) + '"'



Lista=[]
Filas = []
dictArray()
matriz=[]
#print(Lista, type(Lista), len(Lista))
crearFilas()
for i in range(0, len(Filas), 1):
    for j in range(0, len(Lista), 1):
       print(imprimir(i,j), end=' ')
    print()

"""print(f"abriendo archivo: {ArchivoEntrada}...")
RutaArchivoEntrada = Path(ArchivoEntrada)
if RutaArchivoEntrada.exists():
    with RutaArchivoEntrada.open() as archivocsv:
        print("Se ha Encontrado el archivo")
        lectorCSV=csv.reader(archivocsv,delimiter=',')
        for fila in lectorCSV:
            print(fila)
            contador+=1
else:
    print("no pude abrir el archivo {}".format(ArchivoEntrada))
print(contador)"""