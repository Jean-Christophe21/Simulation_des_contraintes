﻿from cylindre import Cylindre


"""
forces = [
    ('x', [1, 0, 0], 100),  # Force de magnitude 10 dans la direction X
    ('y', [0, 1, 0], 250),   # Force de magnitude 5 dans la direction Y
    ('z', [0, 0, 1], -800)    # Force de magnitude 8 dans la direction Z
]

"""


forces = [
    ("axial", 200),  # Force axiale (en Newtons)
    ("radial", 5000)   # Force radiale (en Newtons)
]

forces_suivant_axe = [
    ('x', [1, 0, 0], 0),  # Force de magnitude 10 dans la direction X
    ('y', [0, 1, 0], 500),   # Force de magnitude 5 dans la direction Y
    ('z', [0, 0, 1], 200)    # Force de magnitude 8 dans la direction Z
]

solide = Cylindre()
solide.rayon = 5
solide.hauteur = 30
solide.setE(110e9)
solide.setnu(0.34)
solide.plot_cylindre()
solide.plot_cylindre_avec_forces(forces_suivant_axe)
solide.plot_contraintes(forces)





"""

# test du cylindre

solide = cy.Cylindre()
solide.rayon = 5
solide.hauteur = 30
print(solide.calcul_volume_cylindre())
print(solide.calculer_surface_axiale_cylindre())
solide.plot_cylindre()




# test de la sphere

solide = sp.Sphere()
solide.rayon = 5
print(solide.calcul_volume_sphere())
print(solide.calculer_surface_sphere())
solide.plot_sphere()





from sympy.physics.units import volume

import Parallelepipede as pp
import Cylindre as Cy
import sphere as sp
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox




def choix(event):
    values = ["Cylindre", "Sphere", "Parallelepipede"]

    if combo_shape.get() in values:
        if combo_shape.get()=="Sphere":
            def nouvelle_fenetre():
                global entry_rayon_sphere
                # Creer une nouvelle fenêtre
                fenetre = tk.Toplevel(root)
                fenetre.geometry("400x650+450+10")
                vcmd = (fenetre.register(valider_entree), '%P')
                fenetre.title("Sphere")
                rayon = tk.Label(fenetre, text="Entrez le rayon:")
                rayon.pack(pady=5)
                entry_rayon_sphere = tk.Entry(fenetre, validate="key", validatecommand=vcmd)
                entry_rayon_sphere.pack(ipadx=20, ipady=5)
                contraintes(fenetre)
            nouvelle_fenetre()

        elif combo_shape.get()=="Parallelepipede":
            def nouvelle_fenetre():
                global entry_longueur_para
                global entry_largeur_para
                global entry_hauteur_para
                # Creer une nouvelle fenêtre
                fenetre = tk.Toplevel(root)
                fenetre.geometry("400x650+450+10")
                fenetre.title("Parallelepipede")
                vcmd = (fenetre.register(valider_entree), '%P')
                longueur = tk.Label(fenetre, text="Entrez la longueur:")
                longueur.pack(pady=3)
                entry_longueur_para = tk.Entry(fenetre, validate="key", validatecommand=vcmd)
                entry_longueur_para.pack(ipadx=25, ipady=3)
                largeur = tk.Label(fenetre, text="Entrez la largeur:")
                largeur.pack(pady=3)
                entry_largeur_para = tk.Entry(fenetre, validate="key", validatecommand=vcmd)
                entry_largeur_para.pack(ipadx=25, ipady=3)
                hauteur = tk.Label(fenetre, text="Entrez la hauteur:")
                hauteur.pack(pady=3)
                entry_hauteur_para = tk.Entry(fenetre, validate="key", validatecommand=vcmd)
                entry_hauteur_para.pack(ipadx=25, ipady=3)

                contraintes(fenetre)
            nouvelle_fenetre()

        elif combo_shape.get()=="Cylindre":
            def nouvelle_fenetre():
                global entry_rayon_cylindre
                global entry_hauteur_cylindre
                # Creer une nouvelle fenêtre
                fenetre = tk.Toplevel(root)
                fenetre.geometry("400x650+450+10")
                vcmd = (fenetre.register(valider_entree), '%P')
                fenetre.title("Cylindre")
                rayon= tk.Label(fenetre, text="Entrez le rayon:")
                rayon.pack(pady=3)
                entry_rayon_cylindre = tk.Entry(fenetre, validate="key", validatecommand=vcmd)
                entry_rayon_cylindre.pack(ipadx=25, ipady=3)
                hauteur = tk.Label(fenetre, text="Entrez la hauteur:")
                hauteur.pack(pady=3)
                entry_hauteur_cylindre = tk.Entry(fenetre, validate="key", validatecommand=vcmd)
                entry_hauteur_cylindre.pack(ipadx=25, ipady=3)
                contraintes(fenetre)
            nouvelle_fenetre()

    else:
        messagebox.showerror("Erreur", "Veuillez choisir un des materiau propose.")

def analyze_data():
    try:
        # Recuperer la forme du materiau
        material_shape = combo_shape.get()
        # Recuperer les valeurs des contraintes
        if(material_shape=="Parallelepipede"):
            # test du paralelepipede
            solide = pp.Parallelepipede()
            solide.longueur  = float(entry_longueur_para.get())
            solide.largeur  = float(entry_largeur_para.get())
            solide.hauteur = float(entry_hauteur_para.get())
            volume=solide.calcul_volume_parallelepipede()
            surface=solide.calcul_surface_parallelepipede()
            solide.plot_Parallelepipede()
        elif(material_shape=="Cylindre"):
            solide = Cy.Cylindre()
            solide.rayon = float(entry_rayon_cylindre.get())
            solide.hauteur = float(entry_hauteur_cylindre.get())
            volume=solide.calcul_volume_cylindre()
            surface=solide.calculer_surface_axiale_cylindre()
            solide.plot_cylindre()
        else:
            solide = sp.Sphere()
            solide.rayon = float(entry_rayon_sphere.get())
            volume=solide.calcul_volume_spere()
            surface=solide.calculer_surface_axiale_shpere()
            solide.plot_sphere()

        stress_x = float(entry_stress_x.get())
        stress_y = float(entry_stress_y.get())
        stress_z = float(entry_stress_z.get())
        stress_xy = float(entry_stress_xy.get())
        stress_xz = float(entry_stress_xz.get())
        stress_yz = float(entry_stress_yz.get())
             # Exemple de traitement des donnees
        result = f"Forme: {material_shape}\n" \
            f"Contraintes: σ_x={stress_x}, σ_y={stress_y}, σ_z={stress_z}, " \
            f"τ_xy={stress_xy}, τ_xz={stress_xz}, τ_yz={stress_yz} ,\nvolume={volume},surface={surface}"

        label_result.config(text=result)
    except ValueError:
          label_result.config(text="Veuillez entrer des valeurs valides.")


# Creer la fenêtre principale
root = tk.Tk()
root.title("Analyse des Contraintes dans un Materiau")
root.geometry("400x150+450+250")

# Choix de la forme du materiau
label_shape = tk.Label(root, text="Choisissez la forme du materiau :")
label_shape.pack(pady=20)

combo_shape = ttk.Combobox(root, values=["Cylindre", "Parallelepipede", "Sphere"])
combo_shape.pack(ipadx=25,ipady=5)
combo_shape.bind("<Return>",choix)

def valider_entree(entree) :
    root.lower()
    if entree.isdigit():
        return True
    elif entree == "":
        return True
    else:
        messagebox.showerror("Erreur", "Veuillez entrer uniquement des nombres entiers.")
        root.lower()
        return False

def contraintes(fenetre):
        global entry_stress_x
        global entry_stress_y
        global entry_stress_z
        global entry_stress_xy
        global entry_stress_xz
        global entry_stress_yz
        global label_result
        # Champs pour entrer les intensites des contraintes
        vcmd = (fenetre.register(valider_entree), '%P')
        label_stress_x = tk.Label(fenetre, text="Entrez la contrainte σ_x (Pa) :")
        label_stress_x.pack(pady=3)
        entry_stress_x = tk.Entry(fenetre,validate="key", validatecommand=vcmd)
        entry_stress_x.pack(ipadx=25,ipady=3)

        label_stress_y = tk.Label(fenetre, text="Entrez la contrainte σ_y (Pa) :")
        label_stress_y.pack(pady=3)
        entry_stress_y = tk.Entry(fenetre,validate="key", validatecommand=vcmd)
        entry_stress_y.pack(ipadx=25,ipady=3)

        label_stress_z = tk.Label(fenetre, text="Entrez la contrainte σ_z (Pa) :")
        label_stress_z.pack(pady=5)
        entry_stress_z = tk.Entry(fenetre,validate="key", validatecommand=vcmd)
        entry_stress_z.pack(ipadx=25,ipady=3)

        label_stress_xy = tk.Label(fenetre, text="Entrez la contrainte τ_xy (Pa) :")
        label_stress_xy.pack(pady=3)
        entry_stress_xy = tk.Entry(fenetre,validate="key", validatecommand=vcmd)
        entry_stress_xy.pack(ipadx=25,ipady=3)

        label_stress_xz = tk.Label(fenetre, text="Entrez la contrainte τ_xz (Pa) :")
        label_stress_xz.pack(pady=3)
        entry_stress_xz = tk.Entry(fenetre,validate="key", validatecommand=vcmd)
        entry_stress_xz.pack(ipadx=25,ipady=3)

        label_stress_yz = tk.Label(fenetre, text="Entrez la contrainte τ_yz (Pa) :")
        label_stress_yz.pack(pady=3)
        entry_stress_yz = tk.Entry(fenetre,validate="key", validatecommand=vcmd)
        entry_stress_yz.pack(ipadx=25,ipady=3)
        # Bouton pour lancer l'analyse
        button_analyze = tk.Button(fenetre, text="Analyser", command=analyze_data)
        button_analyze.pack(pady=20)

        # Label pour afficher les resultats
        label_result = tk.Label(fenetre, text="")
        label_result.pack(pady=10)


# Lancer la boucle principale

root.mainloop()

"""













"""
# Contenu de ce fichier le main

from parallelepipede import Parallelepipede



forces = [
    ('x', [1, 0, 0], 100),  # Force de magnitude 10 dans la direction X
    ('y', [0, 1, 0], 250),   # Force de magnitude 5 dans la direction Y
    ('z', [0, 0, 1], -800)    # Force de magnitude 8 dans la direction Z
]




# test du paralelepipede
solide = Parallelepipede()
solide.hauteur = 10
solide.largeur = 5
solide.longueur = 15
solide.setE(110e9)
solide.setnu(0.34)


print(solide.calcul_volume_parallelepipede())
print(solide.calcul_surface_parallelepipede())
solide.plot_Parallelepipede()
solide.plot_Parallelepipede_avec_forces(forces)
solide.plot_Parallelepipede_contraintes("parallelepipede", forces)






"""


"""

from cylindre import Cylindre


forces = [
    ("axial", 200),  # Force axiale (en Newtons)
    ("radial", 5000)   # Force radiale (en Newtons)
]

forces_suivant_axe = [     # représentation de la variable forces suivant les axes
    ('x', [1, 0, 0], 0),  # Force de magnitude 10 dans la direction X
    ('y', [0, 1, 0], 500),   # Force de magnitude 5 dans la direction Y
    ('z', [0, 0, 1], 200)    # Force de magnitude 8 dans la direction Z
]

solide = Cylindre()
solide.rayon = 5
solide.hauteur = 30
solide.setE(110e9)
solide.setnu(0.34)
solide.plot_cylindre()
solide.plot_cylindre_avec_forces(forces_suivant_axe)
solide.plot_contraintes(forces)




"""