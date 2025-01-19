import math


# classe parallelepipede
class Cylindre :
    def __init__(self) -> None:
        super.init__()   # initialisation de la classe m�re
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


    # calcul du volume d'une sph�re
    def calcul_volume_cylindre(self) -> float:
        return math.pi * (self.rayon **2) * self.hauteur

    # calcul de la surface axiale d'une sph�re
    def calculer_surface_axiale_cylindre(self) -> float:
        return 2*math.pi*self.hauteur

    # calcul de la surface radiale d'une sph�re
    def calculer_surface_axiale_cylindre(self) -> float:
         return 2*math.pi * self.rayon**2


        