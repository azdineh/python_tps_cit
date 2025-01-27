import tkinter as tk
import json
from student import Student
from tkinter import messagebox 

root = tk.Tk()
root.title("Inscription")
root.geometry("800x690")
root.resizable(False, False)
root.configure(bg="lightblue")

def buildField(root, fieldname="nom", bg="lightgreen"):
    frame1 = tk.Frame(root, bg=bg, pady=10, padx=10)
    
    label = tk.Label(frame1, text=fieldname, anchor="w", fg="blue", font=("Calibri", 20), bg=bg)
    label.pack(side="top", fill="x")

    entry = tk.Entry(frame1, fg="blue", font=("Calibri", 20))
    entry.pack(side="top", fill="x")
    return frame1, entry

labletitle = tk.Label(root, text="Inscription", fg="blue", font=('Tahoma', 32))
labletitle.grid(column=0, row=0, sticky="nsew")

frame0 = tk.Frame(root, bg="green")
frame0.grid(row=1, column=0, sticky="snew")

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

def saveStudent():
    # Récupérer les données des champs
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    date_naissance = entry_date.get()
    adresse = entry_adresse.get()
    email = entry_email.get()
    pwd = entry_pwd.get()
    
    # Créer une instance de Student (si nécessaire)
    student = Student(
        nom=nom,
        prenom=prenom,
        adresse=adresse,
        date_de_naissance=date_naissance,
        email=email,
        pwd=pwd
    )
    
    # Préparer les données à enregistrer
    student_data = {
        "nom": student.nom,
        "prenom": student.prenom,
        "date_de_naissance": student.date_de_naissance,
        "adresse": student.adresse,
        "email": student.email,
        "pwd": student.pwd
    }

    # Enregistrer dans un fichier JSON
    try:
        with open("students.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(student_data)

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)

    # Confirmer l'enregistrement
    tk.messagebox.showinfo("Succès", "L'étudiant a été enregistré avec succès!")

btnsave = tk.Button(root, text="Enregistrer", command=saveStudent, font=("Verdana", 20))
btnsave.grid(row=2, column=0)

root.grid_columnconfigure(0, weight=1) 
root.grid_rowconfigure(1, weight=1) 

root.mainloop()
