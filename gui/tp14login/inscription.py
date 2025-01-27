import tkinter as tk
import json
from student import Student

root = tk.Tk()
root.title("Inscription")
root.geometry("800x690")
root.resizable(False, False)
root.configure(bg="lightblue")

# Fonction pour construire un champ d'entrée
def buildField(root, fieldname="nom", bg="lightgreen"):
    frame1 = tk.Frame(root, bg=bg, pady=10, padx=10)

    label = tk.Label(frame1, text=fieldname, anchor="w", fg="blue", font=("Calibri", 20), bg=bg)
    label.pack(side="top", fill="x")

    entry = tk.Entry(frame1, fg="blue", font=("Calibri", 20))
    entry.pack(side="top", fill="x")
    return frame1, entry

# Titre
labletitle = tk.Label(root, text="Inscription", fg="blue", font=('Tahoma', 32))
labletitle.grid(column=0, row=0, sticky="nsew")

# Conteneur des champs
frame0 = tk.Frame(root, bg="green")
frame0.grid(row=1, column=0, sticky="snew")

# Champs d'entrée
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

# Fonction pour sauvegarder les données
def saveStudent():
    student_data = {
        "nom": entry_nom.get(),
        "prenom": entry_prenom.get(),
        "date_de_naissance": entry_date.get(),
        "adresse": entry_adresse.get(),
        "email": entry_email.get(),
        "pwd": entry_pwd.get()
    }
    
    # Écriture des données dans un fichier JSON
    with open("students.json", "a") as file:
        file.write(json.dumps(student_data, ensure_ascii=False) + "\n")
    
    # Confirmation de sauvegarde
    print("Étudiant enregistré :", student_data)

# Bouton d'enregistrement
btnsave = tk.Button(root, text="Enregistrer", command=saveStudent, font=("Verdana", 20))
btnsave.grid(row=2, column=0)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

root.mainloop()
