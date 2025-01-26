from materiau import Materiau #importation de la classe mere
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
#from poly3d import Poly3DCollection

# classe parallelepipede
class Parallelepipede(Materiau) :
    def __init__(self) -> None:
        super().__init__()   # initialisation de la classe mere          
        self.volume = 0
        self.longueur = 1
        self.largeur = 1
        self.hauteur = 1
        self.sommets = None # les sommets du parallelepipede
        self.faces = [] # les faces du parallelepipede
        self.surface = 0 # surface du parallelepipede


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


    # calcul du volume d'une sphere
    def calcul_volume_parallelepipede(self)-> float :
        return (self.longueur * self.largeur * self.hauteur)

        # calcul de la surface d'un parallelepipede
    def calcul_surface_parallelepipede(self)-> float :
        return 2 * (self.longueur * self.largeur + self.longueur * self.hauteur + self.largeur * self.hauteur)



    # partie d'Angelo
    #fonctions d'affichage dans la classe Parallelepipede

    # initialisation des sommets et des faces du parallelepipede
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

         

        # affichage du parallelepipede
    def plot_Parallelepipede(self):

        self.init_sommets_Parallelepipede()     # permet de s'assurer avant l'affichaqe que les sommets sont bien initialises
        self.init_faces_Parallelepipede()       # permet de s'assurer avant l'affichaqe que les faces sont bien initialises

        # Creation de la figure et des axes 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # Definition des sommets du cube

        # Ajout des faces au graphique
        poly3d = Poly3DCollection(self.faces, alpha=.25, linewidths=1, edgecolors='r')
        ax.add_collection3d(poly3d)
        # Ajustement des limites des axes
        limit_ax = max(self.longueur, self.largeur, self.hauteur)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_xlim([0, limit_ax])
        ax.set_ylim([0, limit_ax])
        ax.set_zlim([0, limit_ax])
        # Affichage du modele 3D
        plt.show()

    def plot_Parallelepipede_avec_forces(self, forces):

        self.init_sommets_Parallelepipede()     # permet de s'assurer avant l'affichaqe que les sommets sont bien initialises
        self.init_faces_Parallelepipede()       # permet de s'assurer avant l'affichaqe que les faces sont bien initialises

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Ajout des faces au graphique
        poly3d = Poly3DCollection(self.faces, alpha=0.25, linewidths=1, edgecolors='r')
        ax.add_collection3d(poly3d)
        # Ajout des forces au graphique
        for force in forces:
            direction, vector, magnitude = force
            start_point = [self.largeur / 2, self.longueur / 2, self.hauteur / 2]
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
        ax.set_ylim([0, self.longueur])
        ax.set_zlim([0, self.hauteur])
        ax.set_zlabel('Z')
        # Affichage du modele 3D
        plt.show()



    # Fonctions qui permettent d'afficher le cube avec les contraintes


    #Fonction pour appliquer les deformation sur le cube
    def appliquer_deformation_maillage(self, maillage, deformation):
        maillage_deforme = maillage.copy()
        for i in range(len(maillage)):
            maillage_deforme[i, :] = maillage[i, :] + np.dot(deformation, maillage[i, :])
        return maillage_deforme

    # Creation du maillage pour le cube
    def creer_maillage_Parallelepipede(self, largeur, longueur, hauteur, nb_points):
        x = np.linspace(0, largeur, nb_points)
        y = np.linspace(0, longueur, nb_points)
        z = np.linspace(0, hauteur, nb_points)
        return np.array(np.meshgrid(x, y, z)).T.reshape(-1, 3)

    def plot_Parallelepipede_contraintes(self,solide, forces):
        self.surface = self.calcul_surface_parallelepipede() # calcul de la surface du parallelepipede
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # Nombre de points pour le maillage
        nb_points = 30
        # Creation du maillage
        maillage = self.creer_maillage_Parallelepipede(self.largeur, self.longueur, self.hauteur, nb_points)
        # Calculer les tenseurs
        contraintes_totales, deformation_totale = super().calculer_tenseur_contraintes_et_deformation(solide, self.E, self.nu, forces, self.surface)
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
        limit_ax = max(self.longueur, self.largeur, self.hauteur)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_xlim([0, limit_ax])
        ax.set_ylim([0, limit_ax])
        ax.set_zlim([0, limit_ax])
        # Affichage du modele 3D
        plt.show()