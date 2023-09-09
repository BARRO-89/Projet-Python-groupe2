#Importation des librairies
import tkinter as tk
from tkinter import ttk
#import currency

root = tk.Tk()
root.title("Convertisseur de devise - UV-BF_2023")
root.geometry('600x250')

#fonction pour recuperer l'element selectionne
def action(event):
    
    # Obtenir l'élément sélectionné
    select = listeCombo.get()
    #print("Vous avez sélectionné : '", select,"'")
    return select

labelChoix1 = tk.Label(root, text = "Devise source:")
labelChoix1.pack()
#créer la liste Python contenant les éléments de la liste Combobox
code_devises=["USD", "EUR","XOF","CAD"]
#Création de la Combobox via la méthode ttk.Combobox()
listeCombo1 = ttk.Combobox(root, values=code_devises)
#Choisir l'élément qui s'affiche par défaut
listeCombo1.current(0)
listeCombo1.pack()
listeCombo1.bind("<<ComboboxSelected>>", action)

zone_saisie = tk.Entry(root,bg="yellow")
saisie = tk.Label(root, text = "Montant a convertir:")
saisie.pack()
zone_saisie.pack() 

labelChoix2 = tk.Label(root, text = "Devise destination:")
labelChoix2.pack()

#créer la liste Python contenant les éléments de la liste Combobox
code_devises=["USD", "EUR","XOF","CAD"]
#Création de la Combobox via la méthode ttk.Combobox()
listeCombo = ttk.Combobox(root, values=code_devises)
#Choisir l'élément qui s'affiche par défaut
listeCombo.current(0)
listeCombo.pack()
listeCombo.bind("<<ComboboxSelected>>", action)

#Creation du bouton convertir
convertir = tk.Button(root, text="Convert", bg= "green")
convertir.pack()

#Creation du bouton Fermer
fermer = tk.Button(root, text="Fermer", command= root.quit, activebackground= "blue")
fermer.pack()
root.mainloop()
