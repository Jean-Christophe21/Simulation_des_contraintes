
import math
import matplotlib.pyplot as plt
import numpy as np


# classe Sphere
class Sphere :
    def __init__(self) -> None:
        #super.__init__()   # initialisation de la classe mere      cette ligne est une erreur car la classe mere est une classe abstraite
        self.surface = 0 
        self.volume = 0
        self.rayon = 0


    # getter
    def getSurface(self) -> float:
            return self.surface

    def getVolume(self) -> float:
            return self.volume

    def getrayon(self) -> float:
            return self.rayon

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



    # calcul du volume d'une sphere
    def calcul_volume_sphere(self) -> float:
        return (4/3)*math.pi*self.rayon**3

    # calcul de la surface d'une sphere
    def calculer_surface_sphere(self) -> float:
        return 4*math.pi*self.rayon**2




    # Fonction pour afficher la sphere
    def plot_sphere(self):
        # Creation de la figure et des axes 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # Creation de la sphere
        #initialosation des coordonees spheriques (u, v, et x, y, z qui eux definiront le rayon)
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = self.rayon * np.outer(np.cos(u), np.sin(v))
        y = self.rayon * np.outer(np.sin(u), np.sin(v))
        z = self.rayon * np.outer(np.ones(np.size(u)), np.cos(v))

        # Affichage de la sphere
        ax.plot_surface(x, y, z, color='b', alpha=0.25)

        # Ajustement des limites des axes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_xlim([-self.rayon, self.rayon])
        ax.set_ylim([-self.rayon, self.rayon])
        ax.set_zlim([-self.rayon, self.rayon])

        # Affichage du modèle 3D
        plt.show()

    # Fonction pour afficher la sphere avec les flèches des forces
    def plot_sphere_avec_forces(self, forces):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Creation de la sphere
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        #Expression des differents coordonnes spheriques un peu comme on l'a fait avec les triangles
        x = self.rayon * np.outer(np.cos(u), np.sin(v))
        y = self.rayon * np.outer(np.sin(u), np.sin(v))
        z = self.rayon * np.outer(np.ones(np.size(u)), np.cos(v))

        # Affichage de la sphere
        ax.plot_surface(x, y, z, color='b', alpha=0.25)

        # Ajout des forces au graphique
        for force in forces:
            direction, vector, magnitude = force
            start_point = [0, 0, 0]  # Centre de la sphere
            vector = np.array(vector) * magnitude / max([magnitude for _, _, magnitude in forces])  # Ajustement de la longueur des vecteurs
            ax.quiver(
                start_point[0], start_point[1], start_point[2],
                vector[0], vector[1], vector[2],
                color='r', length= self.rayon, normalize=True
            )
        # Le sphere sera clairement centree en O
        # Ajustement des limites des axes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_xlim([-self.rayon, self.rayon])
        ax.set_ylim([-self.rayon, self.rayon])
        ax.set_zlim([-self.rayon, self.rayon])

        # Affichage du modèle 3D
        plt.show()

    # Creation du maillage pour la sphere

    def creer_maillage_sphere(self, rayon, nb_points):
        phi = np.linspace(0, np.pi, nb_points)
        theta = np.linspace(0, 2 * np.pi, nb_points)
        phi, theta = np.meshgrid(phi, theta)
        x = self.rayon * np.outer(np.sin(phi), np.cos(theta))
        y = self.rayon * np.outer(np.sin(phi), np.sin(theta))
        z = self.rayon * np.outer(np.cos(phi), np.ones(np.size(theta)))
        return np.array([x.flatten(), y.flatten(), z.flatten()]).T


    def plot_sphere_contraintes(self, forces):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # Nombre de points pour le maillage
        nb_points = 30
        # Creation du maillage
        maillage = creer_maillage_sphere(self.rayon, nb_points)
        # Calculer les tenseurs
        contraintes_totales, deformation_totale = self.calculer_tenseur_contraintes_et_deformation(forces, self.surface)
        # Appliquer les contraintes au maillage
        maillage_deforme = self.appliquer_deformation_maillage(maillage, deformation_totale)
        # Calcule de la norme des contraintes pour chaque point du maillage
        contraintes_norme = np.linalg.norm(contraintes_totales @ np.transpose(maillage), axis=0)
        # Ajout des points du maillage avec des couleurs representant les contraintes
        sc = ax.scatter(maillage_deforme[:, 0], maillage_deforme[:, 1], maillage_deforme[:, 2], c=contraintes_norme, cmap=plt.cm.viridis)
        # Creation de la barre de couleurs
        cbar = plt.colorbar(sc, ax=ax)
        cbar.set_label('Intensite des contraintes')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_xlim([-self.rayon, self.rayon])
        ax.set_ylim([-self.rayon, self.rayon])
        ax.set_zlim([-self.rayon, self.rayon])
        # Affichage du modèle 3D
        plt.show()