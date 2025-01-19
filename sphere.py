import math


# classe parallelepipede
class Sphere :
    def __init__(self) -> None:
        super.init__()   # initialisation de la classe mère
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



    # calcul du volume d'une sphère
    def calcul_volume_sphere(self) -> float:
        return (4/3)*math.pi*self.rayon**3

    # calcul de la surface d'une sphère
    def calculer_surface_sphere(self) -> float:
        return 4*math.pi*self.rayon**2