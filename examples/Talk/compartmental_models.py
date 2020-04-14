import networkx as nx
import pandas as pd
import numpy as np
import scipy.integrate

class SI_Model():

    def __init__(self, poblacion, infectados, beta=None):

        self.transitions = nx.MultiDiGraph()
        self.transitions.add_edge('S', 'I', agent='I', rate=beta)
        self.S0 = poblacion-infectados
        self.I0 = infectados
        self.poblacion = poblacion
        self.dataframe = None

    def _new_cases(self, population, time, pos):

        diff = np.zeros(len(pos))
        N = np.sum(population)

        for edge in self.transitions.edges(data=True):
            source = edge[0]
            target = edge[1]
            trans = edge[2]

            rate = trans['rate']*population[pos[source]]

            if 'agent' in trans:
                agent = trans['agent']
                rate *= population[pos[agent]]/N

            diff[pos[source]] -= rate
            diff[pos[target]] += rate

        return diff

    def integrate(self, timesteps):

        pos = {'S':0,
               'I':1}
        population=np.zeros(2)
        population[0] = self.S0
        population[1] = self.I0

        time = np.arange(1, timesteps, 1)

        self.dataframe = pd.DataFrame(scipy.integrate.odeint(self._new_cases, population, time, args=(pos,)), columns=pos.keys(), index=time)
        self.dataframe['tiempo']=time

class SIR_Model():

    def __init__(self, poblacion, infectados, recuperados=0, beta=None, mu=None):

        self.transitions = nx.MultiDiGraph()
        self.transitions.add_edge('S', 'I', agent='I', rate=beta)
        self.transitions.add_edge('I', 'R', rate=mu)
        self.S0 = poblacion-infectados
        self.I0 = infectados
        self.R0 = recuperados
        self.poblacion = poblacion
        self.dataframe = None

    def _new_cases(self, population, time, pos):

        diff = np.zeros(len(pos))
        N = np.sum(population)

        for edge in self.transitions.edges(data=True):
            source = edge[0]
            target = edge[1]
            trans = edge[2]

            rate = trans['rate']*population[pos[source]]

            if 'agent' in trans:
                agent = trans['agent']
                rate *= population[pos[agent]]/N

            diff[pos[source]] -= rate
            diff[pos[target]] += rate

        return diff

    def integrate(self, timesteps):

        pos = {'S':0,
               'I':1,
               'R':2}
        population=np.zeros(3)
        population[0] = self.S0
        population[1] = self.I0
        population[2] = self.R0

        time = np.arange(1, timesteps, 1)

        self.dataframe = pd.DataFrame(scipy.integrate.odeint(self._new_cases, population, time, args=(pos,)), columns=pos.keys(), index=time)
        self.dataframe['tiempo']=time




