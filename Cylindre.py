import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# classe parallelepipede
class Cylindre :
    def __init__(self) -> None:
        super.init__()   # initialisation de la classe mère
        self.surface_radiale = 0 
        self.surface_axiale = 0
        self.surface_radiale = 0 
        self.volume = 0
        self.rayon = 0
        self.hauteur = 0


    # getter
    def getSurface(self) -> float:
            return self.surface

    def getVolume(self) -> float:
            return self.volume

    def getrayon(self) -> float:
            return self.rayon


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

    def setrayon(self, rayon : float ) -> None:
        if isinstance(rayon, float) :
            self.rayon = rayon
        else :
            self.rayon = 0

    def setHauteur(self, hauteur : float ) -> None:
        if isinstance(hauteur, float) :
            self.hauteur = hauteur
        else :
            self.hauteur = 0


    # calcul du volume d'une sphère
    def calcul_volume_cylindre(self) -> float:
        return math.pi * (self.rayon **2) * self.hauteur

    # calcul de la surface axiale d'une sphère
    def calculer_surface_axiale_cylindre(self) -> float:
        return 2*math.pi*self.hauteur

    # calcul de la surface radiale d'une sphère
    def calculer_surface_axiale_cylindre(self) -> float:
         return 2*math.pi * self.rayon**2




def plot_cylindre(self):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #Definition de l'axe de la hauteur et de la variable angle
    z = np.linspace(0, self.hauteur, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    #UTILISATION DES COORDONEES CYLINDRE
    # Méthode meshgrid pour créer des grilles de coordonnées
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = self.rayon * np.cos(theta_grid)
    y_grid = self.rayon * np.sin(theta_grid)
    #Le sphere sera centrée sur l'axe z mais dont la base sera posé sur le plan xy
    ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.25, color='cyan')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-self.rayon, self.rayon])
    ax.set_ylim([-self.rayon, self.rayon])
    ax.set_zlim([0, self.hauteur])
    plt.show()

def plot_cylindre_avec_forces(self, forces):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Definition de l'axe de la hauteur et de la variable angle
    z = np.linspace(0, self.hauteur, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    # UTILISATION DES COORDONEES CYLINDRE
    # Méthode meshgrid pour créer des grilles de coordonnées
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = self.rayon * np.cos(theta_grid)
    y_grid = self.rayon * np.sin(theta_grid)
    ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.25, color='cyan')

    # Ajout des faces au graphique
    poly3d = Poly3DCollection(forces, alpha=0.25, linewidths=1, edgecolors='r')
    ax.add_collection3d(poly3d)
    # Ajout des forces au graphique
    for force in forces:
        direction, vector, magnitude = force
        start_point = [0, 0, self.hauteur / 2]
        vector = np.array(vector) * magnitude / max([magnitude for _, _, magnitude in forces])
        ax.quiver(start_point[0], start_point[1], start_point[2], vector[0], vector[1], vector[2], color='b',
                length= self.hauteur*1.5 , normalize=True)
    # Ajustement des limites des axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-self.rayon, self.rayon])
    ax.set_ylim([-self.rayon, self.rayon])
    ax.set_zlim([0,self.hauteur])
    # Affichage du modèle 3D
    plt.show()

    # Fonctions qui permettent d'afficher le cylindre avec les contraintes

    # Fonction pour appliquer les déformation sur le cube
def appliquer_deformation_maillage(maillage, deformation):
    maillage_deforme = maillage.copy()
    for i in range(len(maillage)):
        maillage_deforme[i, :] = maillage[i, :] + np.dot(deformation, maillage[i, :])
    return maillage_deforme

    # Création du maillage pour le cylindre
def creer_maillage_cylindre(x_grid,y_grid, z_grid, theta_grid, nb_points):
    x = np.linspace(0,x_grid , nb_points)
    y = np.linspace(0,y_grid, nb_points)
    z = np.linspace(0,z_grid, nb_points)
    return np.array(np.meshgrid(x, y, z)).T.reshape(-1, 3)


def plot_contraintes(self):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    z = np.linspace(0, self.hauteur, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = self.rayon * np.cos(theta_grid)
    y_grid = self.rayon * np.sin(theta_grid)

    #flatten : méthode des tableaux numpy qui renvoie une copie du tableau réduite à une dimension
    maillage = np.array(np.meshgrid(x_grid.flatten(), y_grid.flatten(), z.flatten())).T.reshape(-1, 3)

    contraintes_totales, deformation_totale = self.calculer_tenseur_contraintes_et_deformation(np.pi * self.rayon ** 2)
    maillage_deforme = appliquer_deformation_maillage(maillage, deformation_totale)

    contraintes_norme = np.linalg.norm(contraintes_totales @ np.transpose(maillage), axis=0)
    sc = ax.scatter(maillage_deforme[:, 0], maillage_deforme[:, 1], maillage_deforme[:, 2], c=contraintes_norme,
                    cmap=plt.cm.viridis)

    cbar = plt.colorbar(sc, ax=ax)
    #Le cylindre est centree sur l'axe z ce qui justifie les limites
    cbar.set_label('Intensité des contraintes')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-self.rayon, self.rayon])
    ax.set_ylim([-self.rayon, self.rayon])
    ax.set_zlim([0, self.hauteur])
    plt.show()