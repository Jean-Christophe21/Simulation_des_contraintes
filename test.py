import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys



def choix(event):
    values = ["Cylindre", "Sphere", "Parallelepipede"]

    if combo_shape.get() in values:
        if combo_shape.get()=="Sphere":
            def nouvelle_fenetre():
                # Créer une nouvelle fenêtre
                fenetre = tk.Toplevel(root)
                fenetre.geometry("400x650+450+10")
                vcmd = (fenetre.register(valider_entrée), '%P')
                fenetre.title("Sphere")
                rayon = tk.Label(fenetre, text="Entrez le rayon:")
                rayon.pack(pady=5)
                entry_rayon = tk.Entry(fenetre, validate="key", validatecommand=vcmd)
                entry_rayon.pack(ipadx=25, ipady=5)
                contraintes(fenetre)
            nouvelle_fenetre()

        elif combo_shape.get()=="Parallelepipede":
            def nouvelle_fenetre():
                # Créer une nouvelle fenêtre
                fenetre = tk.Toplevel(root)
                fenetre.geometry("400x650+450+10")
                fenetre.title("Parallelepipede")
                vcmd = (fenetre.register(valider_entrée), '%P')
                longueur = tk.Label(fenetre, text="Entrez la longueur:")
                longueur.pack(pady=5)
                entry_longueur = tk.Entry(fenetre, validate="key", validatecommand=vcmd)
                entry_longueur.pack(ipadx=25, ipady=5)
                largeur = tk.Label(fenetre, text="Entrez la largeur:")
                largeur.pack(pady=5)
                entry_largeur = tk.Entry(fenetre, validate="key", validatecommand=vcmd)
                entry_largeur.pack(ipadx=25, ipady=5)
                hauteur = tk.Label(fenetre, text="Entrez la hauteur:")
                hauteur.pack(pady=5)
                entry_hauteur = tk.Entry(fenetre, validate="key", validatecommand=vcmd)
                entry_hauteur.pack(ipadx=25, ipady=5)
                contraintes(fenetre)
            nouvelle_fenetre()

        elif combo_shape.get()=="Cylindre":
            def nouvelle_fenetre():
                # Créer une nouvelle fenêtre
                fenetre = tk.Toplevel(root)
                fenetre.geometry("400x650+450+10")
                vcmd = (fenetre.register(valider_entrée), '%P')
                fenetre.title("Cylindre")
                rayon= tk.Label(fenetre, text="Entrez le rayon:")
                rayon.pack(pady=5)
                entry_rayon = tk.Entry(fenetre, validate="key", validatecommand=vcmd)
                entry_rayon.pack(ipadx=25, ipady=5)
                hauteur = tk.Label(fenetre, text="Entrez la hauteur:")
                hauteur.pack(pady=5)
                entry_hauteur = tk.Entry(fenetre, validate="key", validatecommand=vcmd)
                entry_hauteur.pack(ipadx=25, ipady=5)
                contraintes(fenetre)
            nouvelle_fenetre()

    else:
        messagebox.showerror("Erreur", "Veuillez choisir un des materiau proposé.")

def analyze_data():
    try:
        # Récupérer la forme du matériau
        material_shape = combo_shape.get()
        # Récupérer les valeurs des contraintes
        stress_x = float(entry_stress_x.get())
        stress_y = float(entry_stress_y.get())
        stress_z = float(entry_stress_z.get())
        stress_xy = float(entry_stress_xy.get())
        stress_xz = float(entry_stress_xz.get())
        stress_yz = float(entry_stress_yz.get())
         # Exemple de traitement des données
        result = f"Forme: {material_shape}\n" \
        f"Contraintes: σ_x={stress_x}, σ_y={stress_y}, σ_z={stress_z}, " \
        f"τ_xy={stress_xy}, τ_xz={stress_xz}, τ_yz={stress_yz}"

        label_result.config(text=result)
    except ValueError:
          label_result.config(text="Veuillez entrer des valeurs valides.")


# Créer la fenêtre principale
root = tk.Tk()
root.title("Analyse des Contraintes dans un Matériau")
root.geometry("400x150+450+250")

# Choix de la forme du matériau
label_shape = tk.Label(root, text="Choisissez la forme du matériau :")
label_shape.pack(pady=20)

combo_shape = ttk.Combobox(root, values=["Cylindre", "Parallelepipede", "Sphere"])
combo_shape.pack(ipadx=25,ipady=5)
combo_shape.bind("<Return>",choix)

def valider_entrée(entrée) :
    root.lower()
    if entrée.isdigit():
        return True
    elif entrée == "":
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
        # Champs pour entrer les intensités des contraintes
        vcmd = (fenetre.register(valider_entrée), '%P')
        label_stress_x = tk.Label(fenetre, text="Entrez la contrainte σ_x (Pa) :")
        label_stress_x.pack(pady=5)
        entry_stress_x = tk.Entry(fenetre,validate="key", validatecommand=vcmd)
        entry_stress_x.pack(ipadx=25,ipady=5)

        label_stress_y = tk.Label(fenetre, text="Entrez la contrainte σ_y (Pa) :")
        label_stress_y.pack(pady=5)
        entry_stress_y = tk.Entry(fenetre,validate="key", validatecommand=vcmd)
        entry_stress_y.pack(ipadx=25,ipady=5)

        label_stress_z = tk.Label(fenetre, text="Entrez la contrainte σ_z (Pa) :")
        label_stress_z.pack(pady=5)
        entry_stress_z = tk.Entry(fenetre,validate="key", validatecommand=vcmd)
        entry_stress_z.pack(ipadx=25,ipady=5)

        label_stress_xy = tk.Label(fenetre, text="Entrez la contrainte τ_xy (Pa) :")
        label_stress_xy.pack(pady=5)
        entry_stress_xy = tk.Entry(fenetre,validate="key", validatecommand=vcmd)
        entry_stress_xy.pack(ipadx=25,ipady=5)

        label_stress_xz = tk.Label(fenetre, text="Entrez la contrainte τ_xz (Pa) :")
        label_stress_xz.pack(pady=5)
        entry_stress_xz = tk.Entry(fenetre,validate="key", validatecommand=vcmd)
        entry_stress_xz.pack(ipadx=25,ipady=5)

        label_stress_yz = tk.Label(fenetre, text="Entrez la contrainte τ_yz (Pa) :")
        label_stress_yz.pack(pady=5)
        entry_stress_yz = tk.Entry(fenetre,validate="key", validatecommand=vcmd)
        entry_stress_yz.pack(ipadx=25,ipady=5)
        # Bouton pour lancer l'analyse
        button_analyze = tk.Button(fenetre, text="Analyser", command=analyze_data)
        button_analyze.pack(pady=20)

        # Label pour afficher les résultats
        label_result = tk.Label(fenetre, text="")
        label_result.pack(pady=10)


# Lancer la boucle principale

root.mainloop()

