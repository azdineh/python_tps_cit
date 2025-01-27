import tkinter as tk
from student import Student
import json

root = tk.Tk()
root.title("Inscription")
root.geometry("800x690")
root.resizable(False, False)
root.configure(bg="lightblue")

# Fonction pour construire les champs
def buildField(root, fieldname="nom", bg="lightgreen"):
    frame1 = tk.Frame(root, bg=bg, pady=10, padx=10)
    
    label = tk.Label(frame1, text=fieldname, anchor="w", fg="blue", font=("Calibri", 20), bg=bg)
    label.pack(side="top", fill="x")

    entry = tk.Entry(frame1, fg="blue", font=("Calibri", 20))
    entry.pack(side="top", fill="x")
    return frame1, entry

# Titre principal
labletitle = tk.Label(root, text="Inscription", fg="blue", font=('Tahoma', 32))
labletitle.grid(column=0, row=0, sticky="nsew")

frame0 = tk.Frame(root, bg="green")
frame0.grid(row=1, column=0, sticky="snew")

# Création des champs et stockage des entrées
fnom, entry_nom = buildField(frame0, fieldname="Nom:")
fnom.pack(side="top", fill="x")

fprenom, entry_prenom = buildField(frame0, fieldname="Prénom:")
fprenom.pack(side="top", fill="x")

fdate, entry_date = buildField(frame0, fieldname="Date de naissance:")
fdate.pack(side="top", fill="x")

fadresse, entry_adresse = buildField(frame0, fieldname="Adresse:")
fadresse.pack(side="top", fill="x")

femail, entry_email = buildField(frame0, fieldname="Email:")
femail.pack(side="top", fill="x")

fpwd, entry_pwd = buildField(frame0, fieldname="Mot de passe:")
fpwd.pack(side="top", fill="x")

# Fonction pour sauvegarder un étudiant
def saveStudent():
    # Récupérer les données des champs
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    date_de_naissance = entry_date.get()
    adresse = entry_adresse.get()
    email = entry_email.get()
    pwd = entry_pwd.get()

    # Créer un objet Student
    s1 = Student(nom=nom, prenom=prenom, adresse=adresse, date_de_naissance=date_de_naissance, email=email, pwd=pwd)
    
    # Sauvegarder dans un fichier JSON
    student_data = {
        "nom": s1.nom,
        "prenom": s1.prenom,
        "date_de_naissance": s1.date_de_naissance,
        "adresse": s1.adresse,
        "email": s1.email,
        "pwd": s1.pwd
    }

    # Écrire les données dans un fichier JSON
    with open("students.json", "a") as file:
        file.write(json.dumps(student_data) + "\n")
    
    # Afficher un message de confirmation
    confirmation_label = tk.Label(root, text="Étudiant enregistré avec succès!", fg="green", font=("Verdana", 16), bg="lightblue")
    confirmation_label.grid(row=3, column=0)

# Bouton pour enregistrer
btnsave = tk.Button(root, text="Enregistrer", command=saveStudent, font=("Verdana", 20))
btnsave.grid(row=2, column=0)

root.grid_columnconfigure(0, weight=1) 
root.grid_rowconfigure(1, weight=1) 

root.mainloop()
