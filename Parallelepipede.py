import matplotlib.pyplot as plt
import numpy as np
from poly3d import Poly3DCollection

# classe parallelepipede
class Parallelepipede :
    def __init__(self) -> None:
        super.init__()   # initialisation de la classe mère
        self.surface = 0 
        self.volume = 0
        self.longueur = 0
        self.largeur = 0
        self.hauteur = 0


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
        return self.longueur * self.largeur * self.hauteur

        # calcul de la surface d'un parallelepipede
    def calcul_surface_parallelepipede(self)-> float :
        return 2 * (self.longueur * self.largeur + self.longueur * self.hauteur + self.largeur * self.hauteur)



    # partie d'Angelo
    #fonctions d'affichage dans la classe Parallélépipède
    def plot_Parallelepipede(self):
        # Création de la figure et des axes 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        sommets = np.array([[0, 0, 0], [self.largeur, 0, 0], [self.largeur, self.longueur, 0], [0, self.longueur, 0]
                            [0, 0, self.hauteur], [self.largeur, 0, self.hauteur], [self.largeur, self.longueur, self.hauteur],
                            [0, self.longueur, self.hauteur]])
        # Ajout des faces au graphique
        poly3d = Poly3DCollection(faces, alpha=.25, linewidths=1, edgecolors='r')
        ax.add_collection3d(poly3d)
        # Ajustement des limites des axes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_xlim([0, largeur])
        ax.set_ylim([0, longueur])
        ax.set_zlim([0, hauteur])
        # Affichage du modèle 3D
        plt.show()

    def plot_Parallelepipede_avec_forces(forces):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # Définir les faces du cube
        faces = [
            [sommets[0], sommets[1], sommets[2], sommets[3]],
            [sommets[4], sommets[5], sommets[6], sommets[7]],
            [sommets[0], sommets[1], sommets[5], sommets[4]],
            [sommets[2], sommets[3], sommets[7], sommets[6]],
            [sommets[1], sommets[2], sommets[6], sommets[5]],
            [sommets[4], sommets[7], sommets[3], sommets[0]]
        ]
        # Ajout des faces au graphique
        poly3d = Poly3DCollection(faces, alpha=0.25, linewidths=1, edgecolors='r')
        ax.add_collection3d(poly3d)
        # Ajout des forces au graphique
        for force in forces:
            direction, vector, magnitude = force
            start_point = [largeur / 2, longeur / 2, hauteur / 2]
            vector = np.array(vector) * magnitude / max(
                [magnitude for _, _, magnitude in forces])  # Ajustement de la longueur des vecteurs
            ax.quiver(
                start_point[0], start_point[1], start_point[2],
                vector[0], vector[1], vector[2],
                color='b', length= longueur, normalize=True
            )
        # Ajustement des limites des axes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_xlim([0, largeur])
        ax.set_ylim([0, longeur])
        ax.set_zlim([0, hauteur])
        # Affichage du modèle 3D
        plt.show()
