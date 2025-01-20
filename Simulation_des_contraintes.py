import Parallelepipede as pp


# test du paralelepipede
solide = pp.Parallelepipede()
solide.hauteur = 10
solide.largeur = 5
solide.longueur = 150
print(solide.calcul_volume_parallelepipede())
print(solide.calcul_surface_parallelepipede())
solide.plot_Parallelepipede()

