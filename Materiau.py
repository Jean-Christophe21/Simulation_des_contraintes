from re import M
from typing import Any
from abc import ABC, abstractmethod
import numpy as np


# Classe abstraite Materiau
class Materiau(ABC):
    #constructeur de la classe
    def __init__(self):
        self.E = 0 # module de Young
        self.nu = 0 # coefficient de Poisson
        #les coefficient de Lame
        self.lame = 0
        self.mu = 0
        #self.surface = 0 # surface de la section
        self.G = 0 #module de cisaillement

       
    """
    # les differentes methodes du code autre que les getters et les setters
    @abstractmethod
    def appliquerMaillage(self) :
        pass
    """

    def calculer_tenseur_contraintes_et_deformation(self, solide , E , nu, forces ,surface ) :
        self.nu = nu
        self.E = E
        # coefficients de Lame
        self.lame = (E * self.nu) / ((1 + self.nu) * (1 - 2 * self.nu)) 
        self.mu = E / (2 * (1 + self.nu))
        # Initialiser les tenseurs de contrainte et de deformation
        tenseur_deformation = np.zeros((3, 3))
        tenseur_contrainte = np.zeros((3, 3))
    

        if solide == "parallelepipede" :
            deformation = np.zeros((3, 3)) # Initialiser le tenseur de deformation
            # Boucle sur chaque force pour calculer les deformations et les contraintes
            for force in forces:
                direction, vector, magnitude = force

                # Calcul de la contrainte (en Pa)
                sigma = magnitude / self.surface

                # Deformation basee sur la direction de la force
                if direction == 'x':
                    epsilon_xx = sigma / E
                    epsilon_yy = -nu * epsilon_xx
                    epsilon_zz = -nu * epsilon_xx
                    epsilon_xy = sigma / (2 * self.mu)
                    epsilon_xz = sigma / (2 * self.mu)
                    epsilon_yz = sigma / (2 * self.mu)
                    deformation = np.array([
                        [epsilon_xx, epsilon_xy, epsilon_xz],
                        [epsilon_xy, epsilon_yy, 0],
                        [epsilon_xz, 0, epsilon_zz]
                ])
                elif direction == 'y':
                    epsilon_xx = -nu * sigma / E
                    epsilon_yy = sigma / E
                    epsilon_zz = -nu * sigma / E
                    epsilon_xy = sigma / (2 * self.mu)
                    epsilon_xz = sigma / (2 * self.mu)
                    epsilon_yz = sigma / (2 * self.mu)
                    deformation = np.array([
                        [epsilon_xx, epsilon_xy, 0],
                        [epsilon_xy, epsilon_yy, epsilon_yz],
                        [0, epsilon_yz, epsilon_zz]
                    ])
                elif direction == 'z':
                    epsilon_xx = -nu * sigma / E
                    epsilon_yy = -nu * sigma / E
                    epsilon_zz = sigma / E
                    epsilon_xy = sigma / (2 * self.mu)
                    epsilon_xz = sigma / (2 * self.mu)
                    epsilon_yz = sigma / (2 * self.mu)
                    deformation = np.array([
                        [epsilon_xx, 0, epsilon_xz],
                        [0, epsilon_yy, epsilon_yz],
                        [epsilon_xz, epsilon_yz, epsilon_zz]
                    ])
            
                tenseur_deformation += deformation

        elif solide == "cylindre" :
            deformation = np.zeros((3, 3)) # Initialiser le tenseur de deformation

            # Boucle sur chaque force pour calculer les deformations et les contraintes
            for force in forces:
                direction, magnitude = force

                #Calcul de la surface en fonction de la direction
                if direction == 'axial':
                    surface = np.pi * self.rayon**2
                elif direction == 'radial':
                    surface = 2 * np.pi * self.rayon * self.hauteur
                else:
                    continue

                # Calcul de la contrainte (en Pa)
                sigma = magnitude / surface

                # Deformation basee sur la direction de la force
                if direction == 'axial':
                    epsilon_zz = sigma / E
                    epsilon_rr = -nu * epsilon_zz
                    epsilon_tt = -nu * epsilon_zz
                    deformation = np.array([
                        [epsilon_rr, 0, 0],
                        [0, epsilon_tt, 0],
                        [0, 0, epsilon_zz]
                    ])
                elif direction == 'radial':
                    epsilon_rr = sigma / E
                    epsilon_tt = -nu * epsilon_rr
                    epsilon_zz = -nu * epsilon_rr
                    deformation = np.array([
                        [epsilon_rr, 0, 0],
                        [0, epsilon_tt, 0],
                        [0, 0, epsilon_zz]
                    ])
            
                tenseur_deformation += deformation

        elif solide == "sphere" :
            deformation = np.zeros((3, 3)) # Initialiser le tenseur de deformation

            # Boucle sur chaque force pour calculer les deformations et les contraintes
            for force in forces:
                direction, magnitude = force

                '''# Calcul de la surface en fonction de la direction
                if direction == 'radial':
                    surface = 4 * np.pi * rayon**2
                else:
                    continue'''

                # Calcul de la contrainte (en Pa)
                sigma = magnitude / surface

                # Deformation basee sur la direction de la force
                epsilon_rr = sigma / E
                epsilon_tt = -nu * epsilon_rr
                epsilon_pp = -nu * epsilon_rr
                deformation = np.array([
                    [epsilon_rr, 0, 0],
                    [0, epsilon_tt, 0],
                    [0, 0, epsilon_pp]
                ])
            
                tenseur_deformation += deformation

        # Calcul du tenseur de contrainte
        tenseur_contrainte = self.lame * np.trace(tenseur_deformation) * np.eye(3) + 2 * self.mu * tenseur_deformation

        return tenseur_contrainte, tenseur_deformation



    # getter
    def getE(self) -> float:  # get le module de Young
        return self.E
    def getnu(self) -> float: #get le coefficient de Poisson
        return self.nu
    def getlame(self) -> float: #get le coefficient de Lame
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


    # calculer les coefficients de Lame
    def calculer_coefficient_lambda(self) -> float:
        return self.E * self.nu / ((1 + self.nu) * (1 - 2 * self.nu))

    def calculer_coefficient_mu(self) -> float:
        return self.E / ( 2 * (1 + self.nu))

 