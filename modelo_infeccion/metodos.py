import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def creacion_sistema(n_filas,n_columnas,ocupacion = 0.3):
    n_celdas_ocupadas = int(n_filas*n_columnas*ocupacion)
    
    matriz = np.zeros((n_filas,n_columnas), dtype = int)
    
    aa = []
    
    for i in range(n_filas):
        for j in range(n_columnas):
            aa.append([i,j])
            
    np.random.shuffle(aa)
    
    for celda_elegida in aa[0: n_celdas_ocupadas]:
        fila_elegida = celda_elegida[0]
        columna_elegida = celda_elegida[1]
        matriz[fila_elegida,columna_elegida] = 1
        
    return matriz


def representacion_grafica(matriz):

    lista_colores = [(1,1,1), (0.6, 0.6, 0.6), (1, 0, 0)]
    cm = LinearSegmentedColormap.from_list("colorinfectados", lista_colores)

    plt.matshow(matriz, cmap = cm, origin = "lower")

    return plt.show()


def infeccion_inicial(matriz):
    n_filas = matriz.shape[0]
    for i in range(n_filas): # para la columna 0-ésimo
        if matriz[i,0] ==1:
            matriz[i,0] =2


def propagacion(matriz):

    n_filas = matriz.shape[0]
    n_columnas = matriz.shape[1]

    nuevos_infectados = True

    while nuevos_infectados==True:

        nuevos_infectados=False

        for j in range(1,n_columnas-1): #propagación para el resto de columnas

            #Propagación mirando a j-1
            if matriz[0,j] == 1:
                if (matriz[0,j-1]==2) or (matriz[1,j-1]==2)\
                or (matriz[1,j]==2) or (matriz[1,j+1]==2) or (matriz[0,j+1]==2):
                    matriz[0,j] = 2
                    nuevos_infectados=True

            for i in range(1,n_filas-1):
                if matriz[i,j] == 1:
                    if (matriz[i-1,j-1]==2) or (matriz[i,j-1]==2) or (matriz[i+1,j-1]==2)\
                    or (matriz[i+1,j]==2) or (matriz[i-1,j]==2)\
                    or (matriz[i-1,j+1]==2) or (matriz[i,j+1]==2) or (matriz[i+1,j+1]==2):
                        matriz[i,j] = 2
                        nuevos_infectados=True

            if matriz[n_filas-1,j] == 1:
                if (matriz[n_filas-1,j-1] == 2) or (matriz[n_filas-2,j-1] == 2)\
                or (matriz[n_filas-2,j]==2) or (matriz[n_filas-1,j+1] == 2) or (matriz[n_filas-2,j+1] == 2):
                    matriz[n_filas-1,j] = 2
                    nuevos_infectados=True

        if matriz[0,n_columnas-1] == 1:
            if (matriz[0,n_columnas-2]==2) or (matriz[1,n_columnas-2]==2)\
            or (matriz[1,n_columnas-1]==2):
                matriz[0,n_columnas-1] = 2
                nuevos_infectados=True

        for i in range(1,n_filas-1):
            if matriz[i,n_columnas-1] == 1:
                if (matriz[i-1,n_columnas-2]==2) or (matriz[i,n_columnas-2]==2) or (matriz[i+1,n_columnas-2]==2)\
                or (matriz[i+1,n_columnas-1]==2) or (matriz[i-1,n_columnas-1]==2):
                    matriz[i,n_columnas-1] = 2
                    nuevos_infectados=True

        if matriz[n_filas-1,n_columnas-1] == 1:
            if (matriz[n_filas-1,n_columnas-2] == 2) or (matriz[n_filas-2,n_columnas-2] == 2)\
            or (matriz[n_filas-2,n_columnas-1]==2):
                matriz[n_filas-1,n_columnas-1] = 2
                nuevos_infectados=True


def porcentaje_infectado(matriz):
    
    n_infectados = np.count_nonzero(matriz==2)
    n_no_infectados = np.count_nonzero(matriz==1)
    
    if (n_infectados + n_no_infectados) == 0:
        return 0.0
    else:
        return n_infectados / (n_infectados + n_no_infectados)



