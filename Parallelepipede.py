import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
#from poly3d import Poly3DCollection

# classe parallelepipede
class Parallelepipede :
    def __init__(self) -> None:
        #super.__init__()   # initialisation de la classe mère           cette ligne est une erreur car la classe mere est une classe abstraite
        self.surface = 0 
        self.volume = 0
        self.longueur = 1
        self.largeur = 1
        self.hauteur = 1
        self.sommets = None # les sommets du parallelepipede
        self.faces = [] # les faces du parallelepipede


    # getter
    def getSurface(self) -> float:
            return self.surface

    def getVolume(self) -> float:
            return self.volume

    def getlongueur(self) -> float:
            return self.longueur

    def getLargeur(self) -> float:
            return self.largeur

    def getHauteur(self) -> float:
            return self.hauteur

    # setter
    def setsurface(self, surface : float ) -> None:
        if isinstance(surface, float) :
            self.surface = surface
        else :
            self.surface = 0

    def setvolume(self, volume : float ) -> None:
        if isinstance(volume, float) :
            self.volume = volume
        else :
            self.volume = 0

    def setLongueur(self, longueur : float ) -> None:
        if isinstance(longueur, float) :
            self.longueur = longueur
        else :
            self.longueur = 0
     
    def setLargeur(self, largeur : float ) -> None:
        if isinstance(largeur, float) :
            self.largeur = largeur
        else :
            self.largeur = 0

    def setHauteur(self, hauteur : float ) -> None:
        if isinstance(hauteur, float) :
            self.hauteur = hauteur
        else :
            self.hauteur = 0


    # calcul du volume d'une sphère
    def calcul_volume_parallelepipede(self)-> float :
        return (self.longueur * self.largeur * self.hauteur)

        # calcul de la surface d'un parallelepipede
    def calcul_surface_parallelepipede(self)-> float :
        return 2 * (self.longueur * self.largeur + self.longueur * self.hauteur + self.largeur * self.hauteur)



    # partie d'Angelo
    #fonctions d'affichage dans la classe Parallélépipède

    # initialisation des sommets et des faces du parallélépipède
    def init_sommets_Parallelepipede(self):
            self.sommets = np.array([
                                     [0, 0, 0],
                                     [self.largeur, 0, 0], 
                                     [self.largeur, self.longueur, 0], 
                                     [0, self.longueur, 0],
                                     [0, 0, self.hauteur], 
                                     [self.largeur, 0, self.hauteur], 
                                     [self.largeur, self.longueur, self.hauteur],
                                     [0, self.longueur, self.hauteur]
                                     ])
    

    def init_faces_Parallelepipede(self):
        self.faces = [
            [self.sommets[0], self.sommets[1], self.sommets[2], self.sommets[3]],
            [self.sommets[4], self.sommets[5], self.sommets[6], self.sommets[7]],
            [self.sommets[0], self.sommets[1], self.sommets[5], self.sommets[4]],
            [self.sommets[2], self.sommets[3], self.sommets[7], self.sommets[6]],
            [self.sommets[1], self.sommets[2], self.sommets[6], self.sommets[5]],
            [self.sommets[4], self.sommets[7], self.sommets[3], self.sommets[0]]
        ]

         

        # affichage du parallélépipède
    def plot_Parallelepipede(self):

        self.init_sommets_Parallelepipede()     # permet de s'assurer avant l'affichaqe que les sommets sont bien initialisés
        self.init_faces_Parallelepipede()       # permet de s'assurer avant l'affichaqe que les faces sont bien initialisés

        # Création de la figure et des axes 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # Définition des sommets du cube

        # Ajout des faces au graphique
        poly3d = Poly3DCollection(self.faces, alpha=.25, linewidths=1, edgecolors='r')
        ax.add_collection3d(poly3d)
        # Ajustement des limites des axes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_xlim([0, self.largeur])
        ax.set_ylim([0, self.longueur])
        ax.set_zlim([0, self.hauteur])
        # Affichage du modèle 3D
        plt.show()

    def plot_Parallelepipede_avec_forces(self, forces):

        self.init_sommets_Parallelepipede()     # permet de s'assurer avant l'affichaqe que les sommets sont bien initialisés
        self.init_faces_Parallelepipede()       # permet de s'assurer avant l'affichaqe que les faces sont bien initialisés

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Ajout des faces au graphique
        poly3d = Poly3DCollection(self.faces, alpha=0.25, linewidths=1, edgecolors='r')
        ax.add_collection3d(poly3d)
        # Ajout des forces au graphique
        for force in forces:
            direction, vector, magnitude = force
            start_point = [self.largeur / 2, self.longeur / 2, self.hauteur / 2]
            vector = np.array(vector) * magnitude / max(
                [magnitude for _, _, magnitude in forces])  # Ajustement de la longueur des vecteurs
            ax.quiver(
                start_point[0], start_point[1], start_point[2],
                vector[0], vector[1], vector[2],
                color='b', length= self.longueur, normalize=True
            )
        # Ajustement des limites des axes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_xlim([0, self.largeur])
        ax.set_ylim([0, self.longeur])
        ax.set_zlim([0, self.hauteur])
        # Affichage du modèle 3D
        plt.show()

