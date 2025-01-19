import Materiau

#classe Cube
class Cube :
    def __init__(self) -> None:
        super.init__()   # initialisation de la classe mère
        self.surface = 0 
        self.volume = 0
        self.arrete = 0

    # getter
    def getSurface(self) -> float:
            return self.surface
    def getVolume(self) -> float:
            return self.volume
    def getArrete(self) -> float:
            return self.arrete

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

    def setarrete(self, arrete : float ) -> None:
        if isinstance(arrete, float) :
            self.arrete = arrete
        else :
            self.arrete = 0

    # calculer les coeddicents de Lamé
    def calculer_coefficient_lambda(self) -> float:
        return self.E * self.nu / ((1 + self.nu) * (1 - 2 * self.nu))

    def calculer_coefficient_mu(self) -> float:
        return self.E / ( 2 * (1 + self.nu))

    #méthode pour calculer la surface et le volume
    def calculer_surface(self) -> float:
        return self.arrete * self.arrete
    
    def calculer_volume(self) -> float:
        return self.arrete * self.arrete * self.arrete

