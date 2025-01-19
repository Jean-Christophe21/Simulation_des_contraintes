from re import M
from typing import Any
from abc import ABC, abstractmethod

# Classe abstraite Materiau
class Materiau:
    #constructeur de la classe
    def __init__(self):
        self.E = 0 # module de Young
        self.nu = 0 # coefficient de Poisson
        #les coefficient de Lamé
        self.lame = 0
        self.mu = 0
        #self.surface = 0 # surface de la section
        self.G = 0 #module de cisaillement
       
    # les différentes méthodes du code autre que les getters et les setters
    @abstractmethod
    def appliquerMaillage(self) -> None:
        pass



    # getter
    def getE(self) -> float:  # get le module de Young
        return self.E
    def getnu(self) -> float: #get le coefficient de Poisson
        return self.nu
    def getlame(self) -> float: #get le coefficient de Lamé
        return self.lame
    def getmu(self) -> float: #get le module de cisaillement
        return self.mu
    #def getsurface(self) -> float: #get la surface de la section

    # setter
    def setE(self, E: float) -> None:
        if isinstance(E, float) :
            self.E = E
        else :
            self.E = 0

    def setnu(self, nu: float) -> None:
        if isinstance(nu, float) :
            self.nu = nu
        else :
            self.nu = 0

    def setlame(self, lame : float)-> None:
        if isinstance(lame, float) :
            self.lame = lame
        else :
            self.lame = 0


    def setmu(self, mu : float)-> None:
        if isinstance(mu, float) :
            self.mu = mu
        else :
            self.mu = 0



    def setG(self, G : float)-> None:
        if isinstance(G, float) :
            self.G = G
        else :
            self.G = 0

    

 