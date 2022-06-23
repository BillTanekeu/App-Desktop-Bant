from tkinter import Button, Entry, Tk, Canvas, Menu, Toplevel, ttk, Scrollbar, Listbox,constants, Frame, Label,messagebox
from Plateau import Page
from Save import EcritureBD
from DAO import Lecture_BD
from create_table_fpdf2 import PDF
import copy
from tkinter.filedialog import asksaveasfile

class CMenu:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        for w in self.fenetre.winfo_children():
            w.destroy()
       
        # Mettre en plein ecran
        #self.fenetre.resizable(0,0)
        self.w , self.h = self.fenetre.winfo_screenwidth(), self.fenetre.winfo_screenheight()
        self.fenetre.geometry("%dx%d" %(self.w, self.h))
        self.fenetre.config(bg="#ADA69F")
        self.fenetre.title("Bant")
        
        self.menu = Menu(self.fenetre,fg="white", bg="#58585A")
        self.fenetre.configure(menu = self.menu)

        self.fichier = Menu(self.menu, tearoff=0)
        self.fichier.add_command(label = "Nouveau", command=self.restar)
        self.fichier.add_separator()
        self.fichier.add_command(label = "Charger", command= self.loading)
        self.fichier.add_separator()
        self.fichier.add_command(label = "Enregistrer", command= self.save_project)
        self.fichier.add_separator()
        self.fichier.add_command(label = "Imprimer en pdf", command= self.imprimer)
        self.menu.add_cascade(label = "Fichier", menu= self.fichier)

        self.ajouter = Menu(self.menu, tearoff=0)
        
        self.ajouter.add_command(label = "Add amphi", command= self.Add_amphi)
        self.ajouter.add_separator()
        self.ajouter.add_command(label = "Add département", command= self.Add_departement)
        self.ajouter.add_separator()
        self.ajouter.add_command(label = "Add filière", command= self.Add_filiere)
        self.ajouter.add_separator()
        self.ajouter.add_command(label = "Add niveau", command= self.Add_niveau)
        self.ajouter.add_separator()
        self.ajouter.add_command(label = "Add Enseignant", command= self.Add_enseignant )
        self.ajouter.add_separator()
        self.ajouter.add_command(label = "Add specialité",command= self.Add_specialite)
        self.ajouter.add_separator()
        self.ajouter.add_command(label = "Add groupe", command= self.Add_groupe)
        self.ajouter.add_separator()
        self.ajouter.add_command(label = "Add matière", command= self.Add_matiere)
        
        self.menu.add_cascade(label = "Ajouter", menu= self.ajouter)
        
        self.info = []
        self.fenetre.rowconfigure(2, weight=4)
        
        self.numPage = 0
        self.indice = 0
        self.B_page = Button(self.fenetre, text="New page",bg = "#A8F1DE",fg = "#F17E3F", command= self.new_page)
        self.B_page.grid(row = 0, column = 0)
        
        self.can_p = Canvas(self.fenetre, width=85, height= self.h, bg="#ADA69F")
        self.can_p.grid(row=2, column=0)
        
        self.ls_page = Listbox(self.can_p, width=75, height= 60, bg="#08B0C5", font=("time new romam", 12))
        self.ls_page.bind("<<ListboxSelect>>", self.charge)
        self.bar1 = Scrollbar(self.fenetre, orient= "vertical", command= self.can_p.yview, bg= "#000")
        self.can_p.configure(yscrollcommand= self.bar1.set)
        
        

        self.bar1.grid(row =2, column=1, sticky= "ns")
        self.ls_page.grid(row = 2, column=0, sticky= "nw")

        self.ls_page.insert(constants.END,0)
        self.can_p.create_window((0,0), window=self.ls_page, anchor="nw")
        self.ls_page.bind("<Configure>", lambda e: self.can_p.configure(scrollregion = self.can_p.bbox("all")))
       
        """
        self.B_charge = Button(self.fenetre, text="capture")
        self.B_charge.grid(row = 1, column = 0)
        """

        self.dic_h = {11: ("Lundi", "07h05-9h15"), 12: ("Mardi","07h05-9h15"), 13: ("Mercredi","07h05-9h15")
            , 14: ("Jeudi","07h05-9h15"), 15: ("Vendredi","07h05-9h15"), 16: ("Samedi","07h05-9h15"), 17: ("Dimanche","07h05-9h15")
            , 21: ("Lundi", "10h05-12h55"), 22: ("Mardi","10h05-12h55"), 23: ("Mercredi","10h05-12h55")
            , 24: ("Jeudi","10h05-12h55"), 25: ("Vendredi","10h05-12h55"), 26: ("Samedi","10h05-12h55"), 27: ("Dimanche","10h05-12h55")
            , 31: ("Lundi", "13h05-15h55"), 32: ("Mardi","13h05-15h55"), 33: ("Mercredi","13h05-15h55")
            , 34: ("Jeudi","13h05-15h55"), 35: ("Vendredi","13h05-15h55"), 36: ("Samedi","13h05-15h55"), 37: ("Dimanche","13h05-15h55")
            , 41: ("Lundi", "16h05-18h55"), 42: ("Mardi","16h05-18h55"), 43: ("Mercredi","16h05-18h55")
            , 44: ("Jeudi","16h05-18h55"), 45: ("Vendredi","16h05-18h55"), 46: ("Samedi","16h05-18h55"), 47: ("Dimanche","16h05-18h55")
            , 51: ("Lundi", "19h05-21h55"), 52: ("Mardi","19h05-21h55"), 53: ("Mercredi","19h05-21h55")
            , 54: ("Jeudi","19h05-21h55"), 55: ("Vendredi","19h05-21h55"), 56: ("Samedi","19h05-21h55"), 57: ("Dimanche","19h05-21h55")
            }
        
        self.data = [ ["Horaires", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"],
         ["07h05-9h15", "", "", "", "", "", "", ""],
         ["10h05-12h55", "", "", "", "", "", "", ""],
         ["13h05-15h55", "", "", "", "", "", "", ""],
         ["16h05-18h55", "", "", "", "", "", "", ""],
         ["19h05-21h55", "", "", "", "", "", "", ""] ]
        self.pg = Page(self.fenetre,2,2,self.w /1.07, self.h / 1.3, self.info)
        
        self.pg.fenetre.mainloop()

        



        self.fenetre.mainloop()
        
    def new_page(self):
        b = ""
        self.info.append((self.pg.var_filiere.get(), self.pg.var_niveau.get(), self.pg.dico))
        if (self.pg.var_filiere.get() != "" and self.pg.var_niveau.get() != ""):
            b = self.pg.var_filiere.get()[0:5]+" "+ self.pg.var_niveau.get()[0] + self.pg.var_niveau.get()[-1]
            self.update_ls(self.indice, b)
        self.pg = Page(self.fenetre,2,2,self.w /1.07, self.h / 1.3,self.info)
        self.numPage += 1
        self.ls_page.insert(constants.END, self.numPage)
        self.ls_page.activate(self.numPage)
        self.indice = self.numPage
        #self.ls_page.see(self.numPage)
        #self.fenetre.update()

        #print(self.info)

    def charge(self,event):
        i= 0
        b=0
        if (self.indice >= len(self.info)):
            self.info.append((self.pg.var_filiere.get(), self.pg.var_niveau.get(), self.pg.dico))
        else:
            self.info[self.indice] = (self.pg.var_filiere.get(), self.pg.var_niveau.get(), self.pg.dico)
        #print(self.info)
        if(self.ls_page.curselection() != ()):
            if (self.pg.var_filiere.get() != "" and self.pg.var_niveau.get() != ""):
                b = self.pg.var_filiere.get()[0:5]+" "+ self.pg.var_niveau.get()[0] + self.pg.var_niveau.get()[-1]
                self.update_ls(self.indice, b)
            if(self.ls_page.curselection() != ()):
                i = self.ls_page.curselection()[0]
                item = self.info[i]
                self.pg = Page(self.fenetre,2,2,self.w /1.07, self.h / 1.3, self.info)
                self.pg.charger(item[0], item[1], item[2],0)
                self.indice = i
                self.ls_page.activate(self.indice)
        else:
            self.ls_page.activate(self.indice)

    
    def update_ls(self, indice, value):
        self.ls_page.delete(indice)
        self.ls_page.insert(indice, value)
        self.ls_page.activate(indice)


    def Add_amphi(self):
        self.F_amphi = Toplevel(self.fenetre)
        self.F_amphi.title("Ajouter un Amphi")
        self.F_amphi.geometry("400x400")
        
        
        self.frame_form = Frame(self.F_amphi, width=380, height= 380, bg = "grey")
        self.frame_form.place(x = 10, y = 10)
        self.label_Amphi = Label(self.frame_form, text="Nom Amphi :", font=("arial", 16, "bold"), bg = "white")
        self.label_Amphi.place(x = 20, y = 80)
        self.Entry_Amphi = Entry(self.frame_form, font = ("arial", 14),justify="center", width=14)
        #self.select_matiere.bind("<<ComboboxSelected>>", self.update_AmphiEnseignant)
        self.Entry_Amphi.place(x = 200, y = 80)

        self.label_capacite = Label(self.frame_form, text="Capacité :", font=("arial", 16, "bold"), bg = "white")
        self.label_capacite.place(x = 20, y = 140)
        self.entry_capacite= Entry(self.frame_form, font = ("arial", 14),justify="center", width=14)
        self.entry_capacite.place(x = 200, y = 140)

        self.button_form = Button(self.frame_form, text="Valider",font=("calibri",18),bg = "#A8F1DE",fg = "#F17E3F",command = self.V_Amphi)
        self.button_form.place(x = 120, y = 300)
       
        self.F_amphi.transient(self.fenetre)
        #self.form.wm_attributes("-topmost",1)
        self.F_amphi.mainloop()

    def V_Amphi(self):
        if(self.Entry_Amphi.get()!= "" and type(int(self.entry_capacite.get())) == int ):
            EcritureBD.save_Amphi(self.Entry_Amphi.get(), self.entry_capacite.get())
            self.F_amphi.destroy()

        else:
            messagebox.showerror("Erreur!!!", "champ(s) erroné(s)", parent = self.F_amphi)
    

    def Add_departement(self):
        self.F_departement = Toplevel(self.fenetre)
        self.F_departement.title("Ajouter un Amphi")
        self.F_departement.geometry("400x400")
        
        
        self.frame_form = Frame(self.F_departement, width=380, height= 380, bg = "grey")
        self.frame_form.place(x = 10, y = 10)
        self.label_Departement = Label(self.frame_form, text="Nom Département :", font=("arial", 16, "bold"), bg = "white")
        self.label_Departement.place(x = 20, y = 80)
        self.Entry_Departement = Entry(self.frame_form, font = ("arial", 14),justify="center", width=16)
        #self.select_matiere.bind("<<ComboboxSelected>>", self.update_DepartementEnseignant)
        self.Entry_Departement.place(x = 30, y = 120)

       
        self.button_form = Button(self.frame_form, text="Valider",font=("calibri",18),bg = "#A8F1DE",fg = "#F17E3F",command = self.V_Departement)
        self.button_form.place(x = 120, y = 300)
       
        self.F_departement.transient(self.fenetre)
        #self.form.wm_attributes("-topmost",1)
        self.F_departement.mainloop()

    
    def V_Departement(self):
        if(self.Entry_Departement.get()!=""):
            EcritureBD.save_departement(self.Entry_Departement.get())
            self.F_departement.destroy()

        else:
            messagebox.showerror("Erreur!!!", "champ vide", parent = self.F_departement)
    
    def Add_filiere(self):
        self.F_filiere = Toplevel(self.fenetre)
        self.F_filiere.title("Ajouter un Amphi")
        self.F_filiere.geometry("400x400")
        
        ls = []
        self.ls_dep = Lecture_BD.get_departement()
        for dico in self.ls_dep:
            for k in dico.keys():
                ls.append(k)
        
        self.frame_form = Frame(self.F_filiere, width=380, height= 380, bg = "grey")
        self.frame_form.place(x = 10, y = 10)
        self.label_Filiere = Label(self.frame_form, text="Nom Filière :", font=("arial", 16, "bold"), bg = "white")
        self.label_Filiere.place(x = 20, y = 80)
        self.Entry_Filiere = Entry(self.frame_form, font = ("arial", 14),justify="center", width=14)
        #self.select_matiere.bind("<<ComboboxSelected>>", self.update_FiliereEnseignant)
        self.Entry_Filiere.place(x = 200, y = 80)

        self.label_departement = Label(self.frame_form, text=" Département :", font=("arial", 16, "bold"), bg = "white")
        self.label_departement.place(x = 20, y = 140)
        self.select_departement = ttk.Combobox(self.frame_form, font = ("arial", 14),justify="center")
        self.select_departement["values"] = ls
        self.select_departement.place(x = 20, y = 180)

        self.button_form = Button(self.frame_form, text="Valider",font=("calibri",18),bg = "#A8F1DE",fg = "#F17E3F",command = self.V_Filiere)
        self.button_form.place(x = 120, y = 300)
       
        self.F_filiere.transient(self.fenetre)
        #self.form.wm_attributes("-topmost",1)
        self.F_filiere.mainloop()


    def V_Filiere(self):
        if(self.Entry_Filiere.get() != "" and self.select_departement.get()!= ""):
            EcritureBD.save_filiere(self.Entry_Filiere.get(), self.get_id(self.select_departement.get(), self.ls_dep))
            self.F_filiere.destroy()

        else:
            messagebox.showerror("Erreur!!!", "un des champs vide", parent = self.F_filiere)
            
    def Add_niveau(self):
        self.F_niveau = Toplevel(self.fenetre)
        self.F_niveau.title("Ajouter un Amphi")
        self.F_niveau.geometry("400x400")
        
        
        self.frame_form = Frame(self.F_niveau, width=380, height= 380, bg = "grey")
        self.frame_form.place(x = 10, y = 10)
        self.label_Niveau = Label(self.frame_form, text="Nom Niveau :", font=("arial", 16, "bold"), bg = "white")
        self.label_Niveau.place(x = 10, y = 80)
        self.Entry_Niveau = Entry(self.frame_form, font = ("arial", 14),justify="center", width=16)
        #self.select_matiere.bind("<<ComboboxSelected>>", self.update_NiveauEnseignant)
        self.Entry_Niveau.place(x = 180, y = 80)

       
        self.button_form = Button(self.frame_form, text="Valider",font=("calibri",18),bg = "#A8F1DE",fg = "#F17E3F",command = self.V_Niveau)
        self.button_form.place(x = 120, y = 300)
       
        self.F_niveau.transient(self.fenetre)
        #self.form.wm_attributes("-topmost",1)
        self.F_niveau.mainloop()

    
    def V_Niveau(self):
        if(self.Entry_Niveau != ""):
            EcritureBD.save_niveau(self.Entry_Niveau.get())
            self.F_niveau.destroy()

        else:
            messagebox.showerror("Erreur!!!", "Champ vide", parent = self.F_niveau)

    def Add_specialite(self):
        self.F_specialite = Toplevel(self.fenetre)
        self.F_specialite.title("Ajouter une specialité")
        self.F_specialite.geometry("400x400")
        
        ls = []
        self.ls_filiere = Lecture_BD.get_filiere2()
        for dico in self.ls_filiere:
            for k in dico.keys():
                ls.append(k)
        
        self.frame_form = Frame(self.F_specialite, width=380, height= 380, bg = "grey")
        self.frame_form.place(x = 10, y = 10)
        self.label_Specialite = Label(self.frame_form, text="Nom specialite :", font=("arial", 16, "bold"), bg = "white")
        self.label_Specialite.place(x = 40, y = 80)
        self.Entry_Specialite = Entry(self.frame_form, font = ("arial", 14),justify="center", width=14)
        #self.select_matiere.bind("<<ComboboxSelected>>", self.update_SpecialiteeEnseignant)
        self.Entry_Specialite.place(x = 40, y = 120)

        self.label_filiere = Label(self.frame_form, text=" Filière :", font=("arial", 16, "bold"), bg = "white")
        self.label_filiere.place(x = 40, y = 160)
        self.select_filiere = ttk.Combobox(self.frame_form, font = ("arial", 14),justify="center")
        self.select_filiere["values"] = ls
        self.select_filiere.place(x = 40, y = 200)

        self.button_form = Button(self.frame_form, text="Valider",font=("calibri",18),bg = "#A8F1DE",fg = "#F17E3F",command = self.V_Specialite)
        self.button_form.place(x = 120, y = 300)
       
        self.F_specialite.transient(self.fenetre)
        #self.form.wm_attributes("-topmost",1)
        self.F_specialite.mainloop()



    def V_Specialite(self):
        if(self.Entry_Specialite.get() !="" and self.select_filiere.get() != ""):
            EcritureBD.save_specialite(self.get_id( self.select_filiere.get(), self.ls_filiere), self.Entry_Specialite.get())
            self.F_specialite.destroy()
        else:
            messagebox.showerror("Erreur!!!", "Un des champs vide", parent = self.F_specialite)

    def Add_enseignant(self):
        self.F_enseignant = Toplevel(self.fenetre)
        self.F_enseignant.title("Ajouter un enseignant")
        self.F_enseignant.geometry("400x400")
        
        self.ls_dep = Lecture_BD.get_departement()
        ls = []
        for dico in self.ls_dep:
            for k in dico.keys():
                ls.append(k)
        self.frame_form = Frame(self.F_enseignant, width=380, height= 380, bg = "grey")
        self.frame_form.place(x = 10, y = 10)
        self.label_Enseignant = Label(self.frame_form, text="Nom enseignant :", font=("arial", 16, "bold"), bg = "white")
        self.label_Enseignant.place(x = 40, y = 80)
        self.Entry_Enseignant = Entry(self.frame_form, font = ("arial", 14),justify="center", width=14)
        #self.select_matiere.bind("<<ComboboxSelected>>", self.update_EnseignanteEnseignant)
        self.Entry_Enseignant.place(x = 40, y = 120)

        self.label_departement = Label(self.frame_form, text=" Département :", font=("arial", 16, "bold"), bg = "white")
        self.label_departement.place(x = 40, y = 160)
        self.select_departement = ttk.Combobox(self.frame_form, font = ("arial", 14),justify="center")
        self.select_departement["values"] = ls
        self.select_departement.place(x = 40, y = 200)

        self.button_form = Button(self.frame_form, text="Valider",font=("calibri",18),bg = "#A8F1DE",fg = "#F17E3F",command = self.V_Enseignant)
        self.button_form.place(x = 120, y = 300)
       
        self.F_enseignant.transient(self.fenetre)
        #self.form.wm_attributes("-topmost",1)
        self.F_enseignant.mainloop()
    

    def V_Enseignant(self):
        if(self.Entry_Enseignant.get() !="" and self.select_departement.get() != ""):
            EcritureBD.save_enseignant(self.Entry_Specialite.get(), self.get_id( self.select_departement.get(), self.ls_dep))
            self.F_enseignant.destroy()
        else:
            messagebox.showerror("Erreur!!!", "Un des champs vide", parent = self.F_enseignant)
    

    def Add_groupe(self):
        self.F_groupe = Toplevel(self.fenetre)
        self.F_groupe.title("Ajouter un groupe")
        self.F_groupe.geometry("400x400")
        self.ls_specialite = Lecture_BD.get_specialite()
        ls1 = []
        for dico in self.ls_specialite:
            for k in dico.keys():
                ls1.append(k)
        self.ls_niveau = Lecture_BD.get_niveau2()
        ls2 = []
        for dico in self.ls_niveau:
            for k in dico.keys():
                ls2.append(k)
        self.frame_form = Frame(self.F_groupe, width=380, height= 380, bg = "grey")
        self.frame_form.place(x = 10, y = 10)
        self.label_Groupe = Label(self.frame_form, text="Nom groupe :", font=("arial", 16, "bold"), bg = "white")
        self.label_Groupe.place(x = 40, y = 50)
        self.Entry_Groupe = Entry(self.frame_form, font = ("arial", 14),justify="center", width=14)
        self.Entry_Groupe.place(x = 40, y = 90)

        self.label_Nb_etudiant = Label(self.frame_form, text="Nonbre d'étudiant :", font=("arial", 16, "bold"), bg = "white")
        self.label_Nb_etudiant.place(x = 40, y = 130)
        self.Entry_Nb_etudiant = Entry(self.frame_form, font = ("arial", 14),justify="center", width=14)
        #self.select_matiere.bind("<<ComboboxSelected>>", self.update_Nb_etudianteEnseignant)
        self.Entry_Nb_etudiant.place(x = 40, y = 160)

        self.label_Specialite = Label(self.frame_form, text=" Specialité :", font=("arial", 16, "bold"), bg = "white")
        self.label_Specialite.place(x = 40, y = 190)
        self.select_Specialite = ttk.Combobox(self.frame_form, font = ("arial", 14),justify="center")
        self.select_Specialite["values"] = ls1
        self.select_Specialite.place(x = 40, y = 220)

        self.label_Niveau = Label(self.frame_form, text=" Niveau :", font=("arial", 16, "bold"), bg = "white")
        self.label_Niveau.place(x = 40, y = 260)
        self.select_Niveau = ttk.Combobox(self.frame_form, font = ("arial", 14),justify="center")
        self.select_Niveau["values"] = ls2
        self.select_Niveau.place(x = 40, y = 300)


        self.button_form = Button(self.frame_form, text="Valider",font=("calibri",18),bg = "#A8F1DE",fg = "#F17E3F",command = self.V_Groupe)
        self.button_form.place(x = 120, y = 340)
       
        self.F_groupe.transient(self.fenetre)
        #self.form.wm_attributes("-topmost",1)
        self.F_groupe.mainloop()


    def V_Groupe(self):
        if(self.Entry_Groupe.get() != "" and type(int(self.Entry_Nb_etudiant.get())) == int and self.select_Specialite.get() !="" and self.select_Niveau.get()!=""):
            EcritureBD.save_groupe(self.get_id( self.select_Specialite.get(), self.ls_specialite),self.get_id( self.select_Niveau.get(), self.ls_niveau), self.Entry_Groupe.get(), self.Entry_Nb_etudiant.get())
            self.F_groupe.destroy()
        else:
            messagebox.showerror("Erreur!!!", "Un des champs est erroné")

    def Add_matiere(self):
        self.F_matiere = Toplevel(self.fenetre)
        self.F_matiere.title("Ajouter une matière")
        self.F_matiere.geometry("400x400")
        self.ls_niveau = Lecture_BD.get_niveau2()

        self.ls_dep = Lecture_BD.get_departement()
        ls1 = []
        for dico in self.ls_dep:
            for k in dico.keys():
                ls1.append(k)
        
        self.ls_groupe = Lecture_BD.get_groupe()
        ls2 = []
        for dico in self.ls_groupe:
            for k in dico.keys():
                ls2.append(k)
        
        self.frame_form = Frame(self.F_matiere, width=380, height= 380, bg = "grey")
        self.frame_form.place(x = 10, y = 10)
        self.label_Matiere = Label(self.frame_form, text="Nom matiere :", font=("arial", 16, "bold"), bg = "white")
        self.label_Matiere.place(x = 40, y = 50)
        self.Entry_Matiere = Entry(self.frame_form, font = ("arial", 14),justify="center", width=14)
        self.Entry_Matiere.place(x = 40, y = 90)

         
        self.label_Groupe = Label(self.frame_form, text=" Groupe :", font=("arial", 16, "bold"), bg = "white")
        self.label_Groupe.place(x = 40, y = 170)
        self.select_Groupe = ttk.Combobox(self.frame_form, font = ("arial", 14),justify="center")
        self.select_Groupe["values"] = ls2
        self.select_Groupe.place(x = 40, y = 200)

        self.label_Departement = Label(self.frame_form, text=" Departement :", font=("arial", 16, "bold"), bg = "white")
        self.label_Departement.place(x = 40, y = 240)
        self.select_departement = ttk.Combobox(self.frame_form, font = ("arial", 14),justify="center")
        self.select_departement["values"] = ls1
        self.select_departement.place(x = 40, y = 280)


        self.button_form = Button(self.frame_form, text="Valider",font=("calibri",18),bg = "#A8F1DE",fg = "#F17E3F",command = self.V_Matiere)
        self.button_form.place(x = 120, y = 320)
       
        self.F_matiere.transient(self.fenetre)
        #self.form.wm_attributes("-topmost",1)
        self.F_matiere.mainloop()


    def V_Matiere(self):
        if(self.Entry_Matiere.get() != "" and self.select_departement.get() !="" and self.select_Groupe.get()!=""):
            EcritureBD.save_matiere(self.get_id( self.select_Groupe.get(), self.ls_groupe),self.get_id( self.select_departement.get(), self.ls_niveau), self.Entry_Matiere.get())
            self.F_matiere.destroy()

        else:
            messagebox.showerror("Erreur!!!", "Un des champs est erroné")

    def get_id(self,value,ls):
        for dico in ls:
            for k in dico.keys():
                if(k == value):
                    return dico[k] 
        return False


    def save_project(self):
        self.F_save = Toplevel(self.fenetre)
        self.F_save.title("Sauvegarder")
        self.F_save.geometry("200x200")

        self.frame_form = Frame(self.F_save, width=180, height= 180, bg = "grey")
        self.frame_form.place(x = 10, y = 10)
        self.label_save = Label(self.frame_form, text="Nom projet :", font=("arial", 14, "bold"), bg = "white")
        self.label_save.place(x = 5, y = 10)
        self.Entry_save = Entry(self.frame_form, font = ("arial", 14),justify="center", width=14)
        self.Entry_save.place(x = 5, y = 40)
        
        self.button_form = Button(self.frame_form, text="Valider",font=("calibri",18),bg = "#A8F1DE",fg = "#F17E3F",command = self.V_save)
        self.button_form.place(x = 5, y = 120)

        self.F_save.transient(self.fenetre)
    
    def V_save(self):
        if (self.indice >= len(self.info)):
            self.info.append((self.pg.var_filiere.get(), self.pg.var_niveau.get(), self.pg.dico))
        else:
            self.info[self.indice] = (self.pg.var_filiere.get(), self.pg.var_niveau.get(), self.pg.dico)
        if(self.Entry_save.get() != ""):
            self.projet = EcritureBD.save_project(self.Entry_save.get())
            self.F_save.destroy()

            for item in self.info:
                f,n = item[0], item[1]
                id_emploi = EcritureBD.save_emploi(self.projet,f, n)
                for k in item[2].keys():
                    m,a,e = item[2][k][0], item[2][k][1], item[2][k][2]
                    j,h = self.dic_h[k][0], self.dic_h[k][1]
                    EcritureBD.save_cellule(id_emploi,m,a,e,h,j,k)

                    
        else:
            messagebox.showerror("Erreur!!!", "Le champs est vide", parent = self.F_save)


    def imprimer(self):
        self.f = asksaveasfile(mode ="w", defaultextension=".pdf")
        if (self.indice >= len(self.info)):
            self.info.append((self.pg.var_filiere.get(), self.pg.var_niveau.get(), self.pg.dico))
        else:
            self.info[self.indice] = (self.pg.var_filiere.get(), self.pg.var_niveau.get(), self.pg.dico)
        
        pdf = PDF()
        pdf.set_author("Bant")
        pdf.alias_nb_pages()

        pdf.set_auto_page_break(auto = True, margin = 5)
        pdf.set_font("Times", size=10)
        for item in self.info:
            data = copy.deepcopy(self.data)
            pdf.add_page(orientation="L", format="A3")
            titre = item[0] + "    "+ item[1]
            for cle in item[2].keys():
                i,j = int(str(cle)[0]), int(str(cle)[1])
                data[i][j] = "{}\n{}\n{}".format(item[2][cle][0], item[2][cle][1], item[2][cle][2])

            pdf.create_table(table_data = data,title= titre, cell_width=pdf.epw/8)

        pdf.output(self.f.name)



    def loading(self):
        self.load = Toplevel(self.fenetre)
        self.load.title("Charger un projet")
        self.load.geometry("400x400")
        self.list_proj = Lecture_BD.get_projet() 
        self.can_load = Canvas(self.load, width=340, height=300, bg = "grey")
        self.can_load.grid(row= 0, column=0, padx=10, pady= 10)
        self.ls_proj = Listbox(self.can_load, width=340, height= len(self.list_proj)+17, bg="white", font=("time new romam", 14))
        self.ls_proj.place(x = 0, y = 0)

        self.bar_load = Scrollbar(self.load, orient= "vertical", command= self.can_load.yview, bg= "#000")
        self.can_load.configure(yscrollcommand= self.bar_load.set)
        self.button_form = Button(self.load, text="Valider",font=("calibri",18),bg = "#A8F1DE",fg = "#F17E3F",command = self.V_loading)
        self.bar_load.grid(row = 0, column=1, sticky="ns")
        
        for k in self.list_proj.keys():
            self.ls_proj.insert(constants.END, k)
        
        self.button_form.grid(row = 1, column = 0)
        self.can_load.create_window((0,0), window=self.ls_proj, anchor="nw")
        self.ls_proj.bind("<Configure>", lambda e: self.can_load.configure(scrollregion = self.can_load.bbox("all")))
        self.load.transient(self.fenetre)
        #self.form.wm_attributes("-topmost",1)

        self.load.mainloop()

    

    def V_loading(self):
        ls =[]
        result = []
        value = self.ls_proj.curselection()
        if(self.ls_proj.get(value[0])!=""):
            ls = Lecture_BD.get_emploi(self.list_proj[ self.ls_proj.get(value[0])])
            for i in ls:
                result.append(Lecture_BD.get_cellule(i))
            self.info = result
            self.indice = 0
            i = 1
            for item in self.info:
                #item = self.info[i]
                self.pg.charger(item[0], item[1], item[2],0)
                if(self.pg.var_filiere.get()!="" and self.pg.var_niveau.get()!=""):
                    b = self.pg.var_filiere.get()[0:5]+" "+ self.pg.var_niveau.get()[0] + self.pg.var_niveau.get()[-1]
                else:
                    b= self.numPage
                self.update_ls(self.indice, b)
                if(i< len(self.info)):
                    self.pg = Page(self.fenetre,2,2,self.w /1.07, self.h / 1.3,self.info)
                    self.numPage += 1
                    self.ls_page.insert(constants.END, self.numPage)
                    self.ls_page.activate(self.numPage)
                    self.indice = self.numPage
                    i+=1
                #i = self.ls_page.curselection()[0]
                #self.indice = i
                self.ls_page.activate(self.indice)
            self.load.destroy()
            #print(self.info[1])

    def restar(self):
        CMenu(self.fenetre)
#CMenu()
