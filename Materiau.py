from re import M
from typing import Any
from abc import ABC, abstractmethod
import numpy as np


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

    





    def calcul_tenseurs(self, solide , E =0, nu=0, forces = [] ,surface=0) :
        # coefficients de Lamé
        lambda_lame = (E * self.nu) / ((1 + self.nu) * (1 - 2 * self.nu)) 
        mu = E / (2 * (1 + self.nu))
        # Initialiser les tenseurs de contrainte et de déformation
        tenseur_deformation = np.zeros((3, 3))
        tenseur_contrainte = np.zeros((3, 3))
    

        if solide == "parallelepipede" :
            # Boucle sur chaque force pour calculer les déformations et les contraintes
            for force in forces:
                direction, magnitude = force

                # Calcul de la contrainte (en Pa)
                sigma = magnitude / self.surface

                # Déformation basée sur la direction de la force
                if direction == 'x':
                    epsilon_xx = sigma / E
                    epsilon_yy = -nu * epsilon_xx
                    epsilon_zz = -nu * epsilon_xx
                    epsilon_xy = sigma / (2 * mu)
                    epsilon_xz = sigma / (2 * mu)
                    epsilon_yz = sigma / (2 * mu)
                    deformation = np.array([
                        [epsilon_xx, epsilon_xy, epsilon_xz],
                        [epsilon_xy, epsilon_yy, 0],
                        [epsilon_xz, 0, epsilon_zz]
                ])
                elif direction == 'y':
                    epsilon_xx = -nu * sigma / E
                    epsilon_yy = sigma / E
                    epsilon_zz = -nu * sigma / E
                    epsilon_xy = sigma / (2 * mu)
                    epsilon_xz = sigma / (2 * mu)
                    epsilon_yz = sigma / (2 * mu)
                    deformation = np.array([
                        [epsilon_xx, epsilon_xy, 0],
                        [epsilon_xy, epsilon_yy, epsilon_yz],
                        [0, epsilon_yz, epsilon_zz]
                    ])
                elif direction == 'z':
                    epsilon_xx = -nu * sigma / E
                    epsilon_yy = -nu * sigma / E
                    epsilon_zz = sigma / E
                    epsilon_xy = sigma / (2 * mu)
                    epsilon_xz = sigma / (2 * mu)
                    epsilon_yz = sigma / (2 * mu)
                    deformation = np.array([
                        [epsilon_xx, 0, epsilon_xz],
                        [0, epsilon_yy, epsilon_yz],
                        [epsilon_xz, epsilon_yz, epsilon_zz]
                    ])
            
                tenseur_deformation += deformation

        elif solide == "cylindre" :
            # Boucle sur chaque force pour calculer les déformations et les contraintes
            for force in forces:
                direction, magnitude = force

                '''Calcul de la surface en fonction de la direction
                if direction == 'axial':
                    surface = np.pi * rayon**2
                elif direction == 'radial':
                    surface = 2 * np.pi * rayon * hauteur
                else:
                    continue'''

                # Calcul de la contrainte (en Pa)
                sigma = magnitude / self.surface

                # Déformation basée sur la direction de la force
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

            # Boucle sur chaque force pour calculer les déformations et les contraintes
            for force in forces:
                direction, magnitude = force

                '''# Calcul de la surface en fonction de la direction
                if direction == 'radial':
                    surface = 4 * np.pi * rayon**2
                else:
                    continue'''

                # Calcul de la contrainte (en Pa)
                sigma = magnitude / surface

                # Déformation basée sur la direction de la force
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
        tenseur_contrainte = lambda_lame * np.trace(tenseur_deformation) * np.eye(3) + 2 * mu * tenseur_deformation

        return tenseur_contrainte, tenseur_deformation
















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


    # calculer les coefficients de Lamé
    def calculer_coefficient_lambda(self) -> float:
        return self.E * self.nu / ((1 + self.nu) * (1 - 2 * self.nu))

    def calculer_coefficient_mu(self) -> float:
        return self.E / ( 2 * (1 + self.nu))

 