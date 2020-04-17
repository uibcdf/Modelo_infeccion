import numpy as np


class Mundo2d():

    matriz = None
    n_filas = 0
    n_columnas = 0
    ocupacion = 1.0
    porcentaje_infectado = 0.0

    def __init__(self, n_filas, n_columnas, ocupacion = 0.3):

        self.n_filas = n_filas
        self.n_columnas = n_columnas
        self.ocupacion = ocupacion
        self.matriz = np.zeros((n_filas,n_columnas), dtype = int)
        self._aleatorizacion()
        self._promedio_vecinos()

    def _aleatorizacion(self):

        aa = []

        for i in range(self.n_filas):
            for j in range(self.n_columnas):
                aa.append([i,j])

        np.random.shuffle(aa)

        n_celdas_ocupadas = int(self.n_filas*self.n_columnas*self.ocupacion)

        for celda_elegida in aa[0: n_celdas_ocupadas]:
            fila_elegida = celda_elegida[0]
            columna_elegida = celda_elegida[1]
            self.matriz[fila_elegida,columna_elegida] = 1

    def representacion_grafica(self):
        
        import matplotlib.pyplot as plt
        from matplotlib.colors import LinearSegmentedColormap

        lista_colores = [(1,1,1), (0.6, 0.6, 0.6), (1, 0, 0)]
        cm = LinearSegmentedColormap.from_list("colorinfectados", lista_colores)
        plt.matshow(self.matriz, cmap = cm, vmax=2, origin = "lower")

        return plt.show()

    def infeccion_inicial(self):
        for i in range(self.n_filas): # para la columna 0-ésimo
            if self.matriz[i,0] ==1:
                self.matriz[i,0] =2

    def ciclo_propagacion(self):

        for j in range(1,self.n_columnas-1): #propagación para el resto de columnas

            #Propagación mirando a j-1
            if self.matriz[0,j] == 1:
                if (self.matriz[0,j-1]==2) or (self.matriz[1,j-1]==2)\
                or (self.matriz[1,j]==2) or (self.matriz[1,j+1]==2) or (self.matriz[0,j+1]==2):
                    self.matriz[0,j] = 2

            for i in range(1,self.n_filas-1):
                if self.matriz[i,j] == 1:
                    if (self.matriz[i-1,j-1]==2) or (self.matriz[i,j-1]==2) or (self.matriz[i+1,j-1]==2)\
                    or (self.matriz[i+1,j]==2) or (self.matriz[i-1,j]==2)\
                    or (self.matriz[i-1,j+1]==2) or (self.matriz[i,j+1]==2) or (self.matriz[i+1,j+1]==2):
                        self.matriz[i,j] = 2

            if self.matriz[self.n_filas-1,j] == 1:
                if (self.matriz[self.n_filas-1,j-1] == 2) or (self.matriz[self.n_filas-2,j-1] == 2)\
                or (self.matriz[self.n_filas-2,j]==2) or (self.matriz[self.n_filas-1,j+1] == 2) or (self.matriz[self.n_filas-2,j+1] == 2):
                    self.matriz[self.n_filas-1,j] = 2

        if self.matriz[0,self.n_columnas-1] == 1:
            if (self.matriz[0,self.n_columnas-2]==2) or (self.matriz[1,self.n_columnas-2]==2)\
            or (self.matriz[1,self.n_columnas-1]==2):
                self.matriz[0,self.n_columnas-1] = 2

        for i in range(1,self.n_filas-1):
            if self.matriz[i,self.n_columnas-1] == 1:
                if (self.matriz[i-1,self.n_columnas-2]==2) or (self.matriz[i,self.n_columnas-2]==2) or (self.matriz[i+1,self.n_columnas-2]==2)\
                or (self.matriz[i+1,self.n_columnas-1]==2) or (self.matriz[i-1,self.n_columnas-1]==2):
                    self.matriz[i,self.n_columnas-1] = 2

        if self.matriz[self.n_filas-1,self.n_columnas-1] == 1:
            if (self.matriz[self.n_filas-1,self.n_columnas-2] == 2) or (self.matriz[self.n_filas-2,self.n_columnas-2] == 2)\
            or (self.matriz[self.n_filas-2,self.n_columnas-1]==2):
                self.matriz[self.n_filas-1,self.n_columnas-1] = 2



    def propagacion(self):

        nuevos_infectados = True

        while nuevos_infectados==True:

            nuevos_infectados=False

            for j in range(1,self.n_columnas-1): #propagación para el resto de columnas

                #Propagación mirando a j-1
                if self.matriz[0,j] == 1:
                    if (self.matriz[0,j-1]==2) or (self.matriz[1,j-1]==2)\
                    or (self.matriz[1,j]==2) or (self.matriz[1,j+1]==2) or (self.matriz[0,j+1]==2):
                        self.matriz[0,j] = 2
                        nuevos_infectados=True

                for i in range(1,self.n_filas-1):
                    if self.matriz[i,j] == 1:
                        if (self.matriz[i-1,j-1]==2) or (self.matriz[i,j-1]==2) or (self.matriz[i+1,j-1]==2)\
                        or (self.matriz[i+1,j]==2) or (self.matriz[i-1,j]==2)\
                        or (self.matriz[i-1,j+1]==2) or (self.matriz[i,j+1]==2) or (self.matriz[i+1,j+1]==2):
                            self.matriz[i,j] = 2
                            nuevos_infectados=True

                if self.matriz[self.n_filas-1,j] == 1:
                    if (self.matriz[self.n_filas-1,j-1] == 2) or (self.matriz[self.n_filas-2,j-1] == 2)\
                    or (self.matriz[self.n_filas-2,j]==2) or (self.matriz[self.n_filas-1,j+1] == 2) or (self.matriz[self.n_filas-2,j+1] == 2):
                        self.matriz[self.n_filas-1,j] = 2
                        nuevos_infectados=True

            if self.matriz[0,self.n_columnas-1] == 1:
                if (self.matriz[0,self.n_columnas-2]==2) or (self.matriz[1,self.n_columnas-2]==2)\
                or (self.matriz[1,self.n_columnas-1]==2):
                    self.matriz[0,self.n_columnas-1] = 2
                    nuevos_infectados=True

            for i in range(1,self.n_filas-1):
                if self.matriz[i,self.n_columnas-1] == 1:
                    if (self.matriz[i-1,self.n_columnas-2]==2) or (self.matriz[i,self.n_columnas-2]==2) or (self.matriz[i+1,self.n_columnas-2]==2)\
                    or (self.matriz[i+1,self.n_columnas-1]==2) or (self.matriz[i-1,self.n_columnas-1]==2):
                        self.matriz[i,self.n_columnas-1] = 2
                        nuevos_infectados=True

            if self.matriz[self.n_filas-1,self.n_columnas-1] == 1:
                if (self.matriz[self.n_filas-1,self.n_columnas-2] == 2) or (self.matriz[self.n_filas-2,self.n_columnas-2] == 2)\
                or (self.matriz[self.n_filas-2,self.n_columnas-1]==2):
                    self.matriz[self.n_filas-1,self.n_columnas-1] = 2
                    nuevos_infectados=True

        self._obtener_porcentaje_infectado()

    def _promedio_vecinos(self):

        poblacion=0
        vecinos=0

        for j in range(1,self.n_columnas-1): #propagación para el resto de columnas
            for i in range(1,self.n_filas-1):
                if self.matriz[i,j]==1:
                    poblacion+=1
                    if self.matriz[i,j-1]==1: vecinos+=1
                    if self.matriz[i,j+1]==1: vecinos+=1
                    if self.matriz[i-1,j]==1: vecinos+=1
                    if self.matriz[i+1,j]==1: vecinos+=1
                    if self.matriz[i-1,j-1]==1: vecinos+=1
                    if self.matriz[i+1,j+1]==1: vecinos+=1
                    if self.matriz[i-1,j+1]==1: vecinos+=1
                    if self.matriz[i+1,j-1]==1: vecinos+=1

        if poblacion==0:
            self.vecinos_promedio = 0.0
        else:
            self.vecinos_promedio = (vecinos*1.0)/(poblacion*1.0)


    def _obtener_porcentaje_infectado(self):
        
        n_infectados = np.count_nonzero(self.matriz==2)
        n_no_infectados = np.count_nonzero(self.matriz==1)
        
        if (n_infectados + n_no_infectados) == 0:
            self.porcentaje_infectado = 0.0
        else:
            self.porcentaje_infectado = n_infectados / (n_infectados + n_no_infectados)




