import tkinter as tk
from student import Student


root=tk.Tk()
root.title("Inscription")
root.geometry("800x690")
root.resizable(False, False)
root.configure(bg="lightblue")

def buildField(root,fieldname="nom",bg="lightgreen"):
    frame1=tk.Frame(root, bg=bg,pady=10,padx=10)
    
    label=tk.Label(frame1, text=fieldname, anchor="w" ,fg="blue", font=("Calibri",20), bg=bg)
    label.pack(side="top", fill="x")

    entry=tk.Entry(frame1, fg="blue", font=("Calibri",20))
    entry.pack(side="top",fill="x")
    return frame1, entry

labletitle=tk.Label(root,text="Inscription", fg="blue", font=('Tahoma', 32))

labletitle.grid(column=0,row=0,sticky="nsew")

frame0=tk.Frame(root, bg="green")
frame0.grid(row=1,column=0, sticky="snew")

fnom, nom_entry = buildField(frame0,fieldname="Nom:")
fnom.pack(side="top",fill="x")

fprenom, prenom_entry = buildField(frame0,fieldname="Prénom:")
fprenom.pack(side="top",fill="x")

fdate, date_entry = buildField(frame0,fieldname="Date de naissance:")
fdate.pack(side="top",fill="x")

fadresse, adresse_entry = buildField(frame0,fieldname="Adresse:")
fadresse.pack(side="top",fill="x")

femail, email_entry = buildField(frame0,fieldname="Email:")
femail.pack(side="top",fill="x")

fpwd, pwd_entry = buildField(frame0,fieldname="Mot de passe:")
fpwd.pack(side="top",fill="x")


def saveStudent():
    student = Student(
        nom=nom_entry.get(),
        prenom=prenom_entry.get(),
        adresse=adresse_entry.get(),
        date_de_naissance=date_entry.get(),
        email=email_entry.get(),
        pwd=pwd_entry.get()
    )
    student.save()

btnsave=tk.Button(root,text="Enregistrer", command=saveStudent, font=("Verdana",20))
btnsave.grid(row=2,column=0)

root.grid_columnconfigure(0,weight=1) 
root.grid_rowconfigure(1,weight=1) 

root.mainloop()