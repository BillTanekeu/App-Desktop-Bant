from tkinter import  Button, Frame, StringVar, Tk, Canvas, Scrollbar, ttk, Label,messagebox,Toplevel
from PIL import ImageTk, Image
from DAO import Lecture_BD
class Page:
    def __init__(self, fenetre, line, colonne, w, h,info):
        self.fenetre = fenetre
        self.info = info
        # vider la fenetre
        #for w in self.fenetre.winfo_children():
         #   w.destroy()

        # Mettre en plein ecran
        #self.fenetre.resizable(0,0)
        self.w , self.h = w,h
        #self.fenetre.geometry("%dx%d" %(self.w, self.h))
        #self.fenetre.configure(bg="#ADA69F")
        #self.fenetre.title("Bant")
        
        w_canvas , h_canvas = self.w /1., self.h / 1.2
        self.can_f = Canvas(self.fenetre, width=self.w -25, height=self.h+35)
        #self.can_f = Canvas(self.fenetre)
        
        #self.can_f.grid(row = 0, column= 0,  sticky="nw")
        #self.can_f.grid_propagate(True)
        # ***************canvas et configuration du canvas
        
        self.canvas = Canvas(self.can_f, width= w_canvas, height= h_canvas, bg = "#F0EFEF")
        #self.canvas.place(x= (self.w - w_canvas)/2  ,y= (self.h - h_canvas)/3)
        #self.canvas.grid(row=0, column=0, sticky="news")

        self.bar1 = Scrollbar(self.fenetre, orient= "vertical", command= self.can_f.yview, bg= "#000")
        self.can_f.configure(yscrollcommand= self.bar1.set)
        self.bar2 = Scrollbar(self.fenetre, orient= "horizontal", command= self.can_f.xview, bg= "#000")
        self.can_f.configure(xscrollcommand= self.bar2.set)

        self.bar2.grid(row = line+1, column=colonne, sticky= "we")
        self.bar1.grid(row =line, column= colonne+1, sticky= "ns")
        self.can_f.grid(row = line, column=  colonne,  sticky="nw")

        self.can_f.create_window((0,0), window=self.canvas, anchor="nw", tags="win")
        self.canvas.bind("<Configure>", lambda e: self.can_f.configure(scrollregion = self.can_f.bbox("all")))
        #self.bar1.place(x= w_canvas - 10,y = 0)
        
        #self.canvas.grid_propagate(True)
        self.dico = {}
        self.filieres = Lecture_BD.get_filiere()
        self.niveaux = Lecture_BD.get_niveau()
        self.res_matieres = [""]
        self.res_amphis = [""]
        self.res_enseignants = [""]
        
        #***********Titre de la page
        self.L_filiere = Label(self.canvas, text="Filiere:",font=("arial",16),fg="black", bg="#E4C876")
        self.var_filiere = StringVar()
        self.filiere = ttk.Combobox(self.canvas, font = ("arial", 14),justify="center",width=14,state="readonly", textvariable=self.var_filiere)
        self.filiere["values"] = self.filieres
        self.filiere.bind("<<ComboboxSelected>>", self.update_matiere)

        self.L_filiere.place(x = (w_canvas)/5 , y = 10  )
        self.filiere.place(x =  (w_canvas)/3.4 , y =12)


        self.L_niveau = Label(self.canvas, text="Niveau:",font=("arial",14),fg="black", bg="#E4C876")
        self.var_niveau = StringVar()
        self.niveau = ttk.Combobox(self.canvas, font = ("arial", 14),justify="center",width=10,state="readonly", textvariable=self.var_niveau)
        self.niveau["values"] = self.niveaux
        self.niveau.bind("<<ComboboxSelected>>", self.update_matiere)

        self.L_niveau.place(x = (w_canvas)/1.8 , y = 10  )
        self.niveau.place(x =  (w_canvas)/1.6 , y =12)

        self.L_heure = Label(self.canvas, text="Heures",font=("arial",16),fg="black", bg="#F17E3F")
        self.L_heure.place(x= 10, y=80)
        
        

        #********Configuration Jours
        pas = 150
        self.L_jour1 = Label(self.canvas, text="Lundi",font=("arial",16),fg="black", bg="#A8F1DE")
        self.L_jour1.place(x= (w_canvas)/6, y=80)

        self.L_jour2 = Label(self.canvas, text="Mardi",font=("arial",16),fg="black", bg="#A8F1DE")
        self.L_jour2.place(x= (w_canvas)/6 + pas, y=80)

        self.L_jour3 = Label(self.canvas, text="Mercredi",font=("arial",16),fg="black", bg="#A8F1DE")
        self.L_jour3.place(x= (w_canvas)/6 +2*pas, y=80)

        self.L_jour4 = Label(self.canvas, text="Jeudi",font=("arial",16),fg="black", bg="#A8F1DE")
        self.L_jour4.place(x= (w_canvas)/6 +3*pas +20, y=80)

        self.L_jour5 = Label(self.canvas, text="Vendredi",font=("arial",16),fg="black", bg="#A8F1DE")
        self.L_jour5.place(x= (w_canvas)/6 + 4*pas +6, y=80)

        self.L_jour6 = Label(self.canvas, text="Samedi",font=("arial",16),fg="black", bg="#A8F1DE")
        self.L_jour6.place(x= (w_canvas)/6 + 5*pas+25, y=80)

        self.L_jour7 = Label(self.canvas, text="Dimanche",font=("arial",16),fg="black", bg="#A8F1DE")
        self.L_jour7.place(x= (w_canvas)/6 + 6*pas+25, y=80)

        

        #**********************Configuration heure
        pasHauteur =  150
        self.horaire = ["07h05-9h15", "10h05-12h55", "13h05-15h55", "16h05-18h55", "19h05-21h55"]
        
        self.heure1 = Label(self.canvas, text= self.horaire[0], font=("arial",16),fg="black", bg="#F17E3F")
        self.heure1.place(x = 10, y = (h_canvas)/3.5 )

        self.heure2 = Label(self.canvas, text= self.horaire[1], font=("arial",16),fg="black", bg="#F17E3F")
        self.heure2.place(x = 10, y = (h_canvas)/3.5 + pasHauteur )

        self.heure3 = Label(self.canvas, text= self.horaire[2], font=("arial",16),fg="black", bg="#F17E3F")
        self.heure3.place(x = 10, y = (h_canvas)/3.5 + 2*pasHauteur )

        self.heure4 = Label(self.canvas, text= self.horaire[3], font=("arial",16),fg="black", bg="#F17E3F")
        self.heure4.place(x = 10, y = (h_canvas)/3.5 + 3*pasHauteur )

        self.heure5 = Label(self.canvas, text= self.horaire[4], font=("arial",16),fg="black", bg="#F17E3F")
        self.heure5.place(x = 10, y = (h_canvas)/3.5 + 4*pasHauteur )
        
        self.img = Image.open("Images/img3.ico")
        self.imgModif = ImageTk.PhotoImage(image = self.img, size=20)
        WpasCell = 160
        #******************Ligne 1
        
        self.cell11 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b11 = Button(self.cell11, image= self.imgModif, command= lambda : self.Formulaire(11))
        self.var_Matiere11 = StringVar()
        self.var_Amphi11 = StringVar()
        self.var_Enseignant11 = StringVar()
        self.Matiere11 = Label(self.cell11, textvariable= self.var_Matiere11, font=("arial",12,"bold"))
        self.Matiere11.place(x = 10, y = 30)
        self.Amphi11 = Label(self.cell11,textvariable= self.var_Amphi11, font=("arial",12, "bold"))
        self.Amphi11.place(x = 10, y = 62)
        self.Enseigant11 = Label(self.cell11, textvariable= self.var_Enseignant11, font = ("arial",12, "bold"))
        self.Enseigant11.place(x = 10, y = 90)
        self.b11.place(x = 80, y =0)
        self.cell11.place(x = 170, y = (h_canvas)/3.5 -40 )
 
        self.cell12 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b12 = Button(self.cell12, image= self.imgModif, command= lambda : self.Formulaire(12))
        self.var_Matiere12 = StringVar()
        self.var_Amphi12 = StringVar()
        self.var_Enseignant12 = StringVar()
        self.Matiere12 = Label(self.cell12, textvariable= self.var_Matiere12, font=("arial",12,"bold"))
        self.Matiere12.place(x = 10, y = 30)
        self.Amphi12 = Label(self.cell12,textvariable= self.var_Amphi12, font=("arial",12, "bold"))
        self.Amphi12.place(x = 10, y = 62)
        self.Enseigant12 = Label(self.cell12, textvariable= self.var_Enseignant12, font = ("arial",12, "bold"))
        self.Enseigant12.place(x = 10, y = 90)
        self.b12.place(x = 80, y =0)
        self.cell12.place(x = 170 + WpasCell, y = (h_canvas)/3.5 -40 )

 
        self.cell13 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b13 = Button(self.cell13, image= self.imgModif, command= lambda : self.Formulaire(13))
        self.var_Matiere13 = StringVar()
        self.var_Amphi13 = StringVar()
        self.var_Enseignant13 = StringVar()
        self.Matiere13 = Label(self.cell13, textvariable= self.var_Matiere13, font=("arial",12,"bold"))
        self.Matiere13.place(x = 10, y = 30)
        self.Amphi13 = Label(self.cell13,textvariable= self.var_Amphi13, font=("arial",12, "bold"))
        self.Amphi13.place(x = 10, y = 62)
        self.Enseigant13 = Label(self.cell13, textvariable= self.var_Enseignant13, font = ("arial",12, "bold"))
        self.Enseigant13.place(x = 10, y = 90)
        self.b13.place(x = 80, y =0)
        self.cell13.place(x = 170 +2*WpasCell, y = (h_canvas)/3.5 -40 )

 
        self.cell14 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b14 = Button(self.cell14, image= self.imgModif, command= lambda : self.Formulaire(14))
        self.var_Matiere14 = StringVar()
        self.var_Amphi14 = StringVar()
        self.var_Enseignant14 = StringVar()
        self.Matiere14 = Label(self.cell14, textvariable= self.var_Matiere14, font=("arial",12,"bold"))
        self.Matiere14.place(x = 10, y = 30)
        self.Amphi14 = Label(self.cell14,textvariable= self.var_Amphi14, font=("arial",12, "bold"))
        self.Amphi14.place(x = 10, y = 62)
        self.Enseigant14 = Label(self.cell14, textvariable= self.var_Enseignant14, font = ("arial",12, "bold"))
        self.Enseigant14.place(x = 10, y = 90)
        self.b14.place(x = 80, y =0) 
        self.cell14.place(x = 170 +3*WpasCell, y = (h_canvas)/3.5 -40 )

 
        self.cell15 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b15 = Button(self.cell15, image= self.imgModif, command= lambda : self.Formulaire(15))
        self.var_Matiere15 = StringVar()
        self.var_Amphi15 = StringVar()
        self.var_Enseignant15 = StringVar()
        self.Matiere15 = Label(self.cell15, textvariable= self.var_Matiere15, font=("arial",12,"bold"))
        self.Matiere15.place(x = 10, y = 30)
        self.Amphi15 = Label(self.cell15,textvariable= self.var_Amphi15, font=("arial",12, "bold"))
        self.Amphi15.place(x = 10, y = 62)
        self.Enseigant15 = Label(self.cell15, textvariable= self.var_Enseignant15, font = ("arial",12, "bold"))
        self.Enseigant15.place(x = 10, y = 90)
        self.b15.place(x = 80, y =0)
        self.cell15.place(x = 170 + 4*WpasCell, y = (h_canvas)/3.5 -40 )
 

        self.cell16 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b16 = Button(self.cell16, image= self.imgModif, command= lambda : self.Formulaire(16))
        self.var_Matiere16 = StringVar()
        self.var_Amphi16 = StringVar()
        self.var_Enseignant16 = StringVar()
        self.Matiere16 = Label(self.cell16, textvariable= self.var_Matiere16, font=("arial",12,"bold"))
        self.Matiere16.place(x = 10, y = 30)
        self.Amphi16 = Label(self.cell16,textvariable= self.var_Amphi16, font=("arial",12, "bold"))
        self.Amphi16.place(x = 10, y = 62)
        self.Enseigant16 = Label(self.cell16, textvariable= self.var_Enseignant16, font = ("arial",12, "bold"))
        self.Enseigant16.place(x = 10, y = 90)
        self.b16.place(x = 80, y =0)
        self.cell16.place(x = 170+ 5*WpasCell, y = (h_canvas)/3.5 -40 )
 

        self.cell17 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b17 = Button(self.cell17, image= self.imgModif, command= lambda : self.Formulaire(17))
        self.var_Matiere17 = StringVar()
        self.var_Amphi17 = StringVar()
        self.var_Enseignant17 = StringVar()
        self.Matiere17 = Label(self.cell17, textvariable= self.var_Matiere17, font=("arial",12,"bold"))
        self.Matiere17.place(x = 10, y = 30)
        self.Amphi17 = Label(self.cell17,textvariable= self.var_Amphi17, font=("arial",12, "bold"))
        self.Amphi17.place(x = 10, y = 62)
        self.Enseigant17 = Label(self.cell17, textvariable= self.var_Enseignant17, font = ("arial",12, "bold"))
        self.Enseigant17.place(x = 10, y = 90)
        self.b17.place(x = 80, y =0)
        self.cell17.place(x = 170 + 6*WpasCell, y = (h_canvas)/3.5 -40 )
 
        #****************Ligne 2

        
        self.cell21 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b21 = Button(self.cell21, image= self.imgModif, command= lambda : self.Formulaire(21))
        self.var_Matiere21 = StringVar()
        self.var_Amphi21 = StringVar()
        self.var_Enseignant21 = StringVar()
        self.Matiere21 = Label(self.cell21, textvariable= self.var_Matiere21, font=("arial",12,"bold"))
        self.Matiere21.place(x = 10, y = 30)
        self.Amphi21 = Label(self.cell21,textvariable= self.var_Amphi21, font=("arial",12, "bold"))
        self.Amphi21.place(x = 10, y = 62)
        self.Enseigant21 = Label(self.cell21, textvariable= self.var_Enseignant21, font = ("arial",12, "bold"))
        self.Enseigant21.place(x = 10, y = 90)
        self.b21.place(x = 80, y =0)
        self.cell21.place(x = 170, y = (h_canvas)/3.5 + pasHauteur -40 )

 
        self.cell22 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b22 = Button(self.cell22, image= self.imgModif, command= lambda : self.Formulaire(22))
        self.var_Matiere22 = StringVar()
        self.var_Amphi22 = StringVar()
        self.var_Enseignant22 = StringVar()
        self.Matiere22 = Label(self.cell22, textvariable= self.var_Matiere22, font=("arial",12,"bold"))
        self.Matiere22.place(x = 10, y = 30)
        self.Amphi22 = Label(self.cell22,textvariable= self.var_Amphi22, font=("arial",12, "bold"))
        self.Amphi22.place(x = 10, y = 62)
        self.Enseigant22 = Label(self.cell22, textvariable= self.var_Enseignant22, font = ("arial",12, "bold"))
        self.Enseigant22.place(x = 10, y = 90)
        self.b22.place(x = 80, y =0)
        self.cell22.place(x = 170 + WpasCell, y = (h_canvas)/3.5 + pasHauteur -40 )
 

        self.cell23 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b23 = Button(self.cell23, image= self.imgModif, command= lambda : self.Formulaire(23))
        self.var_Matiere23 = StringVar()
        self.var_Amphi23 = StringVar()
        self.var_Enseignant23 = StringVar()
        self.Matiere23 = Label(self.cell23, textvariable= self.var_Matiere23, font=("arial",12,"bold"))
        self.Matiere23.place(x = 10, y = 30)
        self.Amphi23 = Label(self.cell23,textvariable= self.var_Amphi23, font=("arial",12, "bold"))
        self.Amphi23.place(x = 10, y = 62)
        self.Enseigant23 = Label(self.cell23, textvariable= self.var_Enseignant23, font = ("arial",12, "bold"))
        self.Enseigant23.place(x = 10, y = 90)
        self.b23.place(x = 80, y =0)
        self.cell23.place(x = 170 +2*WpasCell, y = (h_canvas)/3.5 + pasHauteur -40 )
 

        self.cell24 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b24 = Button(self.cell24, image= self.imgModif, command= lambda : self.Formulaire(24))
        self.var_Matiere24 = StringVar()
        self.var_Amphi24 = StringVar()
        self.var_Enseignant24 = StringVar()
        self.Matiere24 = Label(self.cell24, textvariable= self.var_Matiere24, font=("arial",12,"bold"))
        self.Matiere24.place(x = 10, y = 30)
        self.Amphi24 = Label(self.cell24,textvariable= self.var_Amphi24, font=("arial",12, "bold"))
        self.Amphi24.place(x = 10, y = 62)
        self.Enseigant24 = Label(self.cell24, textvariable= self.var_Enseignant24, font = ("arial",12, "bold"))
        self.Enseigant24.place(x = 10, y = 90)
        self.b24.place(x = 80, y =0)
        self.cell24.place(x = 170 +3*WpasCell, y = (h_canvas)/3.5 + pasHauteur -40 )
 
        self.cell25 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b25 = Button(self.cell25, image= self.imgModif, command= lambda : self.Formulaire(25))
        self.var_Matiere25 = StringVar()
        self.var_Amphi25 = StringVar()
        self.var_Enseignant25 = StringVar()
        self.Matiere25 = Label(self.cell25, textvariable= self.var_Matiere25, font=("arial",12,"bold"))
        self.Matiere25.place(x = 10, y = 30)
        self.Amphi25 = Label(self.cell25,textvariable= self.var_Amphi25, font=("arial",12, "bold"))
        self.Amphi25.place(x = 10, y = 62)
        self.Enseigant25 = Label(self.cell25, textvariable= self.var_Enseignant25, font = ("arial",12, "bold"))
        self.Enseigant25.place(x = 10, y = 90)
        self.b25.place(x = 80, y =0)
        self.cell25.place(x = 170 + 4*WpasCell, y = (h_canvas)/3.5 + pasHauteur -40 )
 

        self.cell26 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b26 = Button(self.cell26, image= self.imgModif, command= lambda : self.Formulaire(26))
        self.var_Matiere26 = StringVar()
        self.var_Amphi26 = StringVar()
        self.var_Enseignant26 = StringVar()
        self.Matiere26 = Label(self.cell26, textvariable= self.var_Matiere26, font=("arial",12,"bold"))
        self.Matiere26.place(x = 10, y = 30)
        self.Amphi26 = Label(self.cell26,textvariable= self.var_Amphi26, font=("arial",12, "bold"))
        self.Amphi26.place(x = 10, y = 62)
        self.Enseigant26 = Label(self.cell26, textvariable= self.var_Enseignant26, font = ("arial",12, "bold"))
        self.Enseigant26.place(x = 10, y = 90)
        self.b26.place(x = 80, y =0)
        self.cell26.place(x = 170+ 5*WpasCell, y = (h_canvas)/3.5 + pasHauteur -40 )
 
        self.cell27 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b27 = Button(self.cell27, image= self.imgModif, command= lambda : self.Formulaire(27))
        self.var_Matiere27 = StringVar()
        self.var_Amphi27 = StringVar()
        self.var_Enseignant27 = StringVar()
        self.Matiere27 = Label(self.cell27, textvariable= self.var_Matiere27, font=("arial",12,"bold"))
        self.Matiere27.place(x = 10, y = 30)
        self.Amphi27 = Label(self.cell27,textvariable= self.var_Amphi27, font=("arial",12, "bold"))
        self.Amphi27.place(x = 10, y = 62)
        self.Enseigant27 = Label(self.cell27, textvariable= self.var_Enseignant27, font = ("arial",12, "bold"))
        self.Enseigant27.place(x = 10, y = 90)
        self.b27.place(x = 80, y =0)
        self.cell27.place(x = 170 + 6*WpasCell, y = (h_canvas)/3.5 + pasHauteur -40 )
        

        #****************Ligne 3

        
        self.cell31 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b31 = Button(self.cell31, image= self.imgModif, command= lambda : self.Formulaire(31))
        self.var_Matiere31 = StringVar()
        self.var_Amphi31 = StringVar()
        self.var_Enseignant31 = StringVar()
        self.Matiere31 = Label(self.cell31, textvariable= self.var_Matiere31, font=("arial",12,"bold"))
        self.Matiere31.place(x = 10, y = 30)
        self.Amphi31 = Label(self.cell31,textvariable= self.var_Amphi31, font=("arial",12, "bold"))
        self.Amphi31.place(x = 10, y = 62)
        self.Enseigant31 = Label(self.cell31, textvariable= self.var_Enseignant31, font = ("arial",12, "bold"))
        self.Enseigant31.place(x = 10, y = 90)
        self.b31.place(x = 80, y =0)
        self.cell31.place(x = 170, y = (h_canvas)/3.5 + 2*pasHauteur -40 )
 

        self.cell32 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b32 = Button(self.cell32, image= self.imgModif, command= lambda : self.Formulaire(32))
        self.var_Matiere32 = StringVar()
        self.var_Amphi32 = StringVar()
        self.var_Enseignant32 = StringVar()
        self.Matiere32 = Label(self.cell32, textvariable= self.var_Matiere32, font=("arial",12,"bold"))
        self.Matiere32.place(x = 10, y = 30)
        self.Amphi32 = Label(self.cell32,textvariable= self.var_Amphi32, font=("arial",12, "bold"))
        self.Amphi32.place(x = 10, y = 62)
        self.Enseigant32 = Label(self.cell32, textvariable= self.var_Enseignant32, font = ("arial",12, "bold"))
        self.Enseigant32.place(x = 10, y = 90)
        self.b32.place(x = 80, y =0)
        self.cell32.place(x = 170 + WpasCell, y = (h_canvas)/3.5 + 2*pasHauteur -40 )
 
        self.cell33 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b33 = Button(self.cell33, image= self.imgModif, command= lambda : self.Formulaire(33))
        self.var_Matiere33 = StringVar()
        self.var_Amphi33 = StringVar()
        self.var_Enseignant33 = StringVar()
        self.Matiere33 = Label(self.cell33, textvariable= self.var_Matiere33, font=("arial",12,"bold"))
        self.Matiere33.place(x = 10, y = 30)
        self.Amphi33 = Label(self.cell33,textvariable= self.var_Amphi33, font=("arial",12, "bold"))
        self.Amphi33.place(x = 10, y = 62)
        self.Enseigant33 = Label(self.cell33, textvariable= self.var_Enseignant33, font = ("arial",12, "bold"))
        self.Enseigant33.place(x = 10, y = 90)
        self.b33.place(x = 80, y =0)
        self.cell33.place(x = 170 +2*WpasCell, y = (h_canvas)/3.5 + 2*pasHauteur -40 )
 

        self.cell34 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b34 = Button(self.cell34, image= self.imgModif, command= lambda : self.Formulaire(34))
        self.var_Matiere34 = StringVar()
        self.var_Amphi34 = StringVar()
        self.var_Enseignant34 = StringVar()
        self.Matiere34 = Label(self.cell34, textvariable= self.var_Matiere34, font=("arial",12,"bold"))
        self.Matiere34.place(x = 10, y = 30)
        self.Amphi34 = Label(self.cell34,textvariable= self.var_Amphi34, font=("arial",12, "bold"))
        self.Amphi34.place(x = 10, y = 62)
        self.Enseigant34 = Label(self.cell34, textvariable= self.var_Enseignant34, font = ("arial",12, "bold"))
        self.Enseigant34.place(x = 10, y = 90)
        self.b34.place(x = 80, y =0)
        self.cell34.place(x = 170 +3*WpasCell, y = (h_canvas)/3.5 + 2*pasHauteur -40 )
 

        self.cell35 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b35 = Button(self.cell35, image= self.imgModif, command= lambda : self.Formulaire(35))
        self.var_Matiere35 = StringVar()
        self.var_Amphi35 = StringVar()
        self.var_Enseignant35 = StringVar()
        self.Matiere35 = Label(self.cell35, textvariable= self.var_Matiere35, font=("arial",12,"bold"))
        self.Matiere35.place(x = 10, y = 30)
        self.Amphi35 = Label(self.cell35,textvariable= self.var_Amphi35, font=("arial",12, "bold"))
        self.Amphi35.place(x = 10, y = 62)
        self.Enseigant35 = Label(self.cell35, textvariable= self.var_Enseignant35, font = ("arial",12, "bold"))
        self.Enseigant35.place(x = 10, y = 90)
        self.b35.place(x = 80, y =0)
        self.cell35.place(x = 170 + 4*WpasCell, y = (h_canvas)/3.5 + 2*pasHauteur -40 )
 

        self.cell36 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b36 = Button(self.cell36, image= self.imgModif, command= lambda : self.Formulaire(36))
        self.var_Matiere36 = StringVar()
        self.var_Amphi36 = StringVar()
        self.var_Enseignant36 = StringVar()
        self.Matiere36 = Label(self.cell36, textvariable= self.var_Matiere36, font=("arial",12,"bold"))
        self.Matiere36.place(x = 10, y = 30)
        self.Amphi36 = Label(self.cell36,textvariable= self.var_Amphi36, font=("arial",12, "bold"))
        self.Amphi36.place(x = 10, y = 62)
        self.Enseigant36 = Label(self.cell36, textvariable= self.var_Enseignant36, font = ("arial",12, "bold"))
        self.Enseigant36.place(x = 10, y = 90)
        self.b36.place(x = 80, y =0)
        self.cell36.place(x = 170+ 5*WpasCell, y = (h_canvas)/3.5 + 2*pasHauteur -40 )
 

        self.cell37 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b37 = Button(self.cell37, image= self.imgModif, command= lambda : self.Formulaire(37))
        self.var_Matiere37 = StringVar()
        self.var_Amphi37 = StringVar()
        self.var_Enseignant37 = StringVar()
        self.Matiere37 = Label(self.cell37, textvariable= self.var_Matiere37, font=("arial",12,"bold"))
        self.Matiere37.place(x = 10, y = 30)
        self.Amphi37 = Label(self.cell37,textvariable= self.var_Amphi37, font=("arial",12, "bold"))
        self.Amphi37.place(x = 10, y = 62)
        self.Enseigant37 = Label(self.cell37, textvariable= self.var_Enseignant37, font = ("arial",12, "bold"))
        self.Enseigant37.place(x = 10, y = 90)
        self.b37.place(x = 80, y =0)
        self.cell37.place(x = 170 + 6*WpasCell, y = (h_canvas)/3.5 + 2*pasHauteur -40 )
        
        #****************Ligne 4

        
        self.cell41 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b41 = Button(self.cell41, image= self.imgModif, command= lambda : self.Formulaire(41))
        self.var_Matiere41 = StringVar()
        self.var_Amphi41 = StringVar()
        self.var_Enseignant41 = StringVar()
        self.Matiere41 = Label(self.cell41, textvariable= self.var_Matiere41, font=("arial",12,"bold"))
        self.Matiere41.place(x = 10, y = 30)
        self.Amphi41 = Label(self.cell41,textvariable= self.var_Amphi41, font=("arial",12, "bold"))
        self.Amphi41.place(x = 10, y = 62)
        self.Enseigant41 = Label(self.cell41, textvariable= self.var_Enseignant41, font = ("arial",12, "bold"))
        self.Enseigant41.place(x = 10, y = 90)
        self.b41.place(x = 80, y =0)
        self.cell41.place(x = 170, y = (h_canvas)/3.5 + 3*pasHauteur -40 )
 

        self.cell42 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b42 = Button(self.cell42, image= self.imgModif, command= lambda : self.Formulaire(42))
        self.var_Matiere42 = StringVar()
        self.var_Amphi42 = StringVar()
        self.var_Enseignant42 = StringVar()
        self.Matiere42 = Label(self.cell42, textvariable= self.var_Matiere42, font=("arial",12,"bold"))
        self.Matiere42.place(x = 10, y = 30)
        self.Amphi42 = Label(self.cell42,textvariable= self.var_Amphi42, font=("arial",12, "bold"))
        self.Amphi42.place(x = 10, y = 62)
        self.Enseigant42 = Label(self.cell42, textvariable= self.var_Enseignant42, font = ("arial",12, "bold"))
        self.Enseigant42.place(x = 10, y = 90)
        self.b42.place(x = 80, y =0)
        self.cell42.place(x = 170 + WpasCell, y = (h_canvas)/3.5 + 3*pasHauteur -40 )
 

        self.cell43 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b43 = Button(self.cell43, image= self.imgModif, command= lambda : self.Formulaire(43))
        self.var_Matiere43 = StringVar()
        self.var_Amphi43 = StringVar()
        self.var_Enseignant43 = StringVar()
        self.Matiere43 = Label(self.cell43, textvariable= self.var_Matiere43, font=("arial",12,"bold"))
        self.Matiere43.place(x = 10, y = 30)
        self.Amphi43 = Label(self.cell43,textvariable= self.var_Amphi43, font=("arial",12, "bold"))
        self.Amphi43.place(x = 10, y = 62)
        self.Enseigant43 = Label(self.cell43, textvariable= self.var_Enseignant43, font = ("arial",12, "bold"))
        self.Enseigant43.place(x = 10, y = 90)
        self.b43.place(x = 80, y =0)
        self.cell43.place(x = 170 +2*WpasCell, y = (h_canvas)/3.5 + 3*pasHauteur -40 )
 

        self.cell44 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b44 = Button(self.cell44, image= self.imgModif, command= lambda : self.Formulaire(44))
        self.var_Matiere44 = StringVar()
        self.var_Amphi44 = StringVar()
        self.var_Enseignant44 = StringVar()
        self.Matiere44 = Label(self.cell44, textvariable= self.var_Matiere44, font=("arial",12,"bold"))
        self.Matiere44.place(x = 10, y = 30)
        self.Amphi44 = Label(self.cell44,textvariable= self.var_Amphi44, font=("arial",12, "bold"))
        self.Amphi44.place(x = 10, y = 62)
        self.Enseigant44 = Label(self.cell44, textvariable= self.var_Enseignant44, font = ("arial",12, "bold"))
        self.Enseigant44.place(x = 10, y = 90)
        self.b44.place(x = 80, y =0)
        self.cell44.place(x = 170 +3*WpasCell, y = (h_canvas)/3.5 + 3*pasHauteur -40 )
 

        self.cell45 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b45 = Button(self.cell45, image= self.imgModif, command= lambda : self.Formulaire(45))
        self.var_Matiere45 = StringVar()
        self.var_Amphi45 = StringVar()
        self.var_Enseignant45 = StringVar()
        self.Matiere45 = Label(self.cell45, textvariable= self.var_Matiere45, font=("arial",12,"bold"))
        self.Matiere45.place(x = 10, y = 30)
        self.Amphi45 = Label(self.cell45,textvariable= self.var_Amphi45, font=("arial",12, "bold"))
        self.Amphi45.place(x = 10, y = 62)
        self.Enseigant45 = Label(self.cell45, textvariable= self.var_Enseignant45, font = ("arial",12, "bold"))
        self.Enseigant45.place(x = 10, y = 90)
        self.b45.place(x = 80, y =0)
        self.cell45.place(x = 170 + 4*WpasCell, y = (h_canvas)/3.5 + 3*pasHauteur -40 )
 

        self.cell46 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b46 = Button(self.cell46, image= self.imgModif, command= lambda : self.Formulaire(46))
        self.var_Matiere46 = StringVar()
        self.var_Amphi46 = StringVar()
        self.var_Enseignant46 = StringVar()
        self.Matiere46 = Label(self.cell46, textvariable= self.var_Matiere46, font=("arial",12,"bold"))
        self.Matiere46.place(x = 10, y = 30)
        self.Amphi46 = Label(self.cell46,textvariable= self.var_Amphi46, font=("arial",12, "bold"))
        self.Amphi46.place(x = 10, y = 62)
        self.Enseigant46 = Label(self.cell46, textvariable= self.var_Enseignant46, font = ("arial",12, "bold"))
        self.Enseigant46.place(x = 10, y = 90)
        self.b46.place(x = 80, y =0)
        self.cell46.place(x = 170+ 5*WpasCell, y = (h_canvas)/3.5 + 3*pasHauteur -40 )
 

        self.cell47 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b47 = Button(self.cell47, image= self.imgModif, command= lambda : self.Formulaire(47))
        self.var_Matiere47 = StringVar()
        self.var_Amphi47 = StringVar()
        self.var_Enseignant47 = StringVar()
        self.Matiere47 = Label(self.cell47, textvariable= self.var_Matiere47, font=("arial",12,"bold"))
        self.Matiere47.place(x = 10, y = 30)
        self.Amphi47 = Label(self.cell47,textvariable= self.var_Amphi47, font=("arial",12, "bold"))
        self.Amphi47.place(x = 10, y = 62)
        self.Enseigant47 = Label(self.cell47, textvariable= self.var_Enseignant47, font = ("arial",12, "bold"))
        self.Enseigant47.place(x = 10, y = 90)
        self.b47.place(x = 80, y =0)
        self.cell47.place(x = 170 + 6*WpasCell, y = (h_canvas)/3.5 + 3*pasHauteur -40 )
           
        #****************Ligne 5

        
        self.cell51 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b51 = Button(self.cell51, image= self.imgModif, command= lambda : self.Formulaire(51))
        self.var_Matiere51 = StringVar()
        self.var_Amphi51 = StringVar()
        self.var_Enseignant51 = StringVar()
        self.Matiere51 = Label(self.cell51, textvariable= self.var_Matiere51, font=("arial",12,"bold"))
        self.Matiere51.place(x = 10, y = 30)
        self.Amphi51 = Label(self.cell51,textvariable= self.var_Amphi51, font=("arial",12, "bold"))
        self.Amphi51.place(x = 10, y = 62)
        self.Enseigant51 = Label(self.cell51, textvariable= self.var_Enseignant51, font = ("arial",12, "bold"))
        self.Enseigant51.place(x = 10, y = 90)
        self.b51.place(x = 80, y =0)
        self.cell51.place(x = 170, y = (h_canvas)/3.5 + 4*pasHauteur -40 )
 

        self.cell52 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b52 = Button(self.cell52, image= self.imgModif, command= lambda : self.Formulaire(52))
        self.var_Matiere52 = StringVar()
        self.var_Amphi52 = StringVar()
        self.var_Enseignant52 = StringVar()
        self.Matiere52 = Label(self.cell52, textvariable= self.var_Matiere52, font=("arial",12,"bold"))
        self.Matiere52.place(x = 10, y = 30)
        self.Amphi52 = Label(self.cell52,textvariable= self.var_Amphi52, font=("arial",12, "bold"))
        self.Amphi52.place(x = 10, y = 62)
        self.Enseigant52 = Label(self.cell52, textvariable= self.var_Enseignant52, font = ("arial",12, "bold"))
        self.Enseigant52.place(x = 10, y = 90)
        self.b52.place(x = 80, y =0)
        self.cell52.place(x = 170 + WpasCell, y = (h_canvas)/3.5 + 4*pasHauteur -40 )
 

        self.cell53 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b53 = Button(self.cell53, image= self.imgModif, command= lambda : self.Formulaire(53))
        self.var_Matiere53 = StringVar()
        self.var_Amphi53 = StringVar()
        self.var_Enseignant53 = StringVar()
        self.Matiere53 = Label(self.cell53, textvariable= self.var_Matiere53, font=("arial",12,"bold"))
        self.Matiere53.place(x = 10, y = 30)
        self.Amphi53 = Label(self.cell53,textvariable= self.var_Amphi53, font=("arial",12, "bold"))
        self.Amphi53.place(x = 10, y = 62)
        self.Enseigant53 = Label(self.cell53, textvariable= self.var_Enseignant53, font = ("arial",12, "bold"))
        self.Enseigant53.place(x = 10, y = 90)
        self.b53.place(x = 80, y =0)
        self.cell53.place(x = 170 +2*WpasCell, y = (h_canvas)/3.5 + 4*pasHauteur -40 )
 

        self.cell54 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b54 = Button(self.cell54, image= self.imgModif, command= lambda : self.Formulaire(54))
        self.var_Matiere54 = StringVar()
        self.var_Amphi54 = StringVar()
        self.var_Enseignant54 = StringVar()
        self.Matiere54 = Label(self.cell54, textvariable= self.var_Matiere54, font=("arial",12,"bold"))
        self.Matiere54.place(x = 10, y = 30)
        self.Amphi54 = Label(self.cell54,textvariable= self.var_Amphi54, font=("arial",12, "bold"))
        self.Amphi54.place(x = 10, y = 62)
        self.Enseigant54 = Label(self.cell54, textvariable= self.var_Enseignant54, font = ("arial",12, "bold"))
        self.Enseigant54.place(x = 10, y = 90)
        self.b54.place(x = 80, y =0)
        self.cell54.place(x = 170 +3*WpasCell, y = (h_canvas)/3.5 + 4*pasHauteur -40 )
 

        self.cell55 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b55 = Button(self.cell55, image= self.imgModif, command= lambda : self.Formulaire(55))
        self.var_Matiere55 = StringVar()
        self.var_Amphi55 = StringVar()
        self.var_Enseignant55 = StringVar()
        self.Matiere55 = Label(self.cell55, textvariable= self.var_Matiere55, font=("arial",12,"bold"))
        self.Matiere55.place(x = 10, y = 30)
        self.Amphi55 = Label(self.cell55,textvariable= self.var_Amphi55, font=("arial",12, "bold"))
        self.Amphi55.place(x = 10, y = 62)
        self.Enseigant55 = Label(self.cell55, textvariable= self.var_Enseignant55, font = ("arial",12, "bold"))
        self.Enseigant55.place(x = 10, y = 90)
        self.b55.place(x = 80, y =0)
        self.cell55.place(x = 170 + 4*WpasCell, y = (h_canvas)/3.5 + 4*pasHauteur -40 )
 

        self.cell56 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b56 = Button(self.cell56, image= self.imgModif, command= lambda : self.Formulaire(56))
        self.var_Matiere56 = StringVar()
        self.var_Amphi56 = StringVar()
        self.var_Enseignant56 = StringVar()
        self.Matiere56 = Label(self.cell56, textvariable= self.var_Matiere56, font=("arial",12,"bold"))
        self.Matiere56.place(x = 10, y = 30)
        self.Amphi56 = Label(self.cell56,textvariable= self.var_Amphi56, font=("arial",12, "bold"))
        self.Amphi56.place(x = 10, y = 62)
        self.Enseigant56 = Label(self.cell56, textvariable= self.var_Enseignant56, font = ("arial",12, "bold"))
        self.Enseigant56.place(x = 10, y = 90)
        self.b56.place(x = 80, y =0)
        self.cell56.place(x = 170+ 5*WpasCell, y = (h_canvas)/3.5 + 4*pasHauteur -40 )
 

        self.cell57 = Canvas(self.canvas, width=120, height= 120, bg="#DBD1CB")
        self.b57 = Button(self.cell57, image= self.imgModif, command= lambda : self.Formulaire(57))
        self.var_Matiere57 = StringVar()
        self.var_Amphi57 = StringVar()
        self.var_Enseignant57 = StringVar()
        self.Matiere57 = Label(self.cell57, textvariable= self.var_Matiere57, font=("arial",12,"bold"))
        self.Matiere57.place(x = 10, y = 30)
        self.Amphi57 = Label(self.cell57,textvariable= self.var_Amphi57, font=("arial",12, "bold"))
        self.Amphi57.place(x = 10, y = 62)
        self.Enseigant57 = Label(self.cell57, textvariable= self.var_Enseignant57, font = ("arial",12, "bold"))
        self.Enseigant57.place(x = 10, y = 90)
        self.b57.place(x = 80, y =0)
        self.cell57.place(x = 170 + 6*WpasCell, y = (h_canvas)/3.5 + 4*pasHauteur -40 )
      
 
        self.canvas.configure(width= w_canvas , height= (h_canvas)/3.5 + 6*pasHauteur )

        self.clear_dico = {11:("","",""), 12:("","",""), 13:("","",""), 14:("","",""), 15:("","",""), 16:("","",""), 
                                17:("","",""), 21:("","",""), 22:("","",""), 23:("","",""), 24:("","",""), 25:("","",""), 
                                26:("","",""), 27:("","",""), 31:("","",""), 32:("","",""), 33:("","",""), 34:("","",""), 
                                35:("","",""), 36:("","",""), 37:("","",""), 41:("","",""), 42:("","",""), 43:("","",""), 
                                44:("","",""), 45:("","",""), 46:("","",""), 47:("","",""), 51:("","",""), 52:("","",""), 
                                53:("","",""), 54:("","",""), 55:("","",""), 56:("","",""), 57:("","","")}    

        self.clear_filiere = ""
        self.clear_niveau = ""
        self.var_EntryMa = StringVar()
        self.var_EntryA = StringVar()
        self.var_EntryE = StringVar()

        #self.fenetre.mainloop()

    
    def Formulaire(self,p):
        #print("ok ",p)
        #self.form = Tk()
        self.form  = Toplevel(self.fenetre)
        self.form.title("Cellule: {}".format(p))
        self.form.geometry("400x400")
        
        
        self.frame_form = Frame(self.form, width=380, height= 380, bg = "grey")
        self.frame_form.place(x = 10, y = 10)
        self.label_matiere = Label(self.frame_form, text=" Matiere :", font=("arial", 16, "bold"), bg = "white")
        self.label_matiere.place(x = 20, y = 80)
        self.select_matiere = ttk.Combobox(self.frame_form, font = ("arial", 14),justify="center",width=10,state="readonly", textvariable=self.var_EntryMa)
        self.select_matiere["values"] = self.res_matieres
        #self.select_matiere.bind("<<ComboboxSelected>>", self.update_AmphiEnseignant)
        self.select_matiere.place(x = 200, y = 80)

        self.label_amphi = Label(self.frame_form, text=" Amphi :", font=("arial", 16, "bold"), bg = "white")
        self.label_amphi.place(x = 20, y = 140)
        self.select_amphi= ttk.Combobox(self.frame_form, font = ("arial", 14),justify="center",width=10,state="readonly",textvariable= self.var_EntryA, postcommand=self.update_AmphiEnseignant)
        self.select_amphi["values"] = self.res_amphis
        self.select_amphi.place(x = 200, y = 140)

        self.label_enseignant = Label(self.frame_form, text=" Enseignant :", font=("arial", 16, "bold"), bg = "white")
        self.label_enseignant.place(x = 20, y = 200)
        self.select_enseignant = ttk.Combobox(self.frame_form, font = ("arial", 14),justify="center",width=10,state="readonly",textvariable= self.var_EntryE, postcommand=self.update_AmphiEnseignant)
        self.select_enseignant["values"] = self.res_enseignants
        self.select_enseignant.place(x = 200, y = 200)
        

        self.button_form = Button(self.frame_form, text="Valider",font=("calibri",18),bg = "#A8F1DE",fg = "#F17E3F", command= lambda: self.Verification_Form(p))
        self.button_form.place(x = 120, y = 300)
        """self.form.wm_client(self.fenetre)
        self.form.grab_set()
        self.form.focus_set()"""
        self.form.transient(self.fenetre)
        #self.form.wm_attributes("-topmost",1)
        self.form.mainloop()
    

    def Verification_Form(self,p):
        b = 1
        for i in self.info:
            for k in i[2].keys():
                if(k==p and b==1):
                    if(i[2][k][1] == self.select_amphi.get()):
                        messagebox.showerror("Erreur!!!","Amphi occupée par {} {}  cellule {}".format(i[0],i[1],k),parent = self.form)
                        b=0
                        break
                    if(i[2][k][2] == self.select_enseignant.get()):
                        messagebox.showerror("Erreur!!!","Enseignant déjà pris par {} {}  cellule {}".format(i[0],i[1],k), parent = self.form)
                        b=0
                        break
        if(b == 1):
            if(self.select_amphi.get() != "" or self.select_enseignant.get() != "" or self.select_matiere.get() != ""):
                self.dico[p] = (self.select_matiere.get(), self.select_amphi.get(), self.select_enseignant.get())
            if (p == 11):
                self.var_EntryMa.trace("w",  self.var_Matiere11.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi11.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant11.set(self.select_enseignant.get()))
            elif(p == 12):
                self.var_EntryMa.trace("w", self.var_Matiere12.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi12.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant12.set(self.select_enseignant.get()))
            
            elif(p == 13):
                self.var_EntryMa.trace("w", self.var_Matiere13.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi13.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant13.set(self.select_enseignant.get()))
            
            elif(p == 14):
                self.var_EntryMa.trace("w", self.var_Matiere14.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi14.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant14.set(self.select_enseignant.get()))
            
            elif(p == 15):
                self.var_EntryMa.trace("w", self.var_Matiere15.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi15.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant15.set(self.select_enseignant.get()))
            
            elif(p == 16):
                self.var_EntryMa.trace("w", self.var_Matiere16.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi16.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant16.set(self.select_enseignant.get()))
            
            elif(p == 17):
                self.var_EntryMa.trace("w", self.var_Matiere17.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi17.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant17.set(self.select_enseignant.get()))
            
            elif(p == 21):
                self.var_EntryMa.trace("w", self.var_Matiere21.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi21.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant21.set(self.select_enseignant.get()))
            
            elif(p == 22):
                self.var_EntryMa.trace("w", self.var_Matiere22.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi22.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant22.set(self.select_enseignant.get()))
            
            elif(p == 23):
                self.var_EntryMa.trace("w", self.var_Matiere23.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi23.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant23.set(self.select_enseignant.get()))
            
            elif(p == 24):
                self.var_EntryMa.trace("w", self.var_Matiere24.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi24.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant24.set(self.select_enseignant.get()))
            
            elif(p == 25):
                self.var_EntryMa.trace("w", self.var_Matiere25.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi25.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant25.set(self.select_enseignant.get()))
            
            elif(p == 26):
                self.var_EntryMa.trace("w", self.var_Matiere26.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi26.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant26.set(self.select_enseignant.get()))
            
            elif(p == 27):
                self.var_EntryMa.trace("w", self.var_Matiere27.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi27.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant27.set(self.select_enseignant.get()))
            
            elif(p == 31):
                self.var_EntryMa.trace("w", self.var_Matiere31.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi31.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant31.set(self.select_enseignant.get()))
            
            elif(p == 32):
                self.var_EntryMa.trace("w", self.var_Matiere32.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi32.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant32.set(self.select_enseignant.get()))
            
            elif(p == 33):
                self.var_EntryMa.trace("w", self.var_Matiere33.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi33.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant33.set(self.select_enseignant.get()))
            
            elif(p == 34):
                self.var_EntryMa.trace("w", self.var_Matiere34.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi34.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant34.set(self.select_enseignant.get()))
            
            elif(p == 35):
                self.var_EntryMa.trace("w", self.var_Matiere35.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi35.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant35.set(self.select_enseignant.get()))
            
            elif(p == 36):
                self.var_EntryMa.trace("w", self.var_Matiere36.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi36.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant36.set(self.select_enseignant.get()))
            
            elif(p == 37):
                self.var_EntryMa.trace("w", self.var_Matiere37.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi37.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant37.set(self.select_enseignant.get()))
            
            elif(p == 41):
                self.var_EntryMa.trace("w", self.var_Matiere41.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi41.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant41.set(self.select_enseignant.get()))
            
            elif(p == 42):
                self.var_EntryMa.trace("w", self.var_Matiere42.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi42.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant42.set(self.select_enseignant.get()))
            
            elif(p == 43):
                self.var_EntryMa.trace("w", self.var_Matiere43.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi43.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant43.set(self.select_enseignant.get()))
            
            elif(p == 44):
                self.var_EntryMa.trace("w", self.var_Matiere44.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi44.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant44.set(self.select_enseignant.get()))
            
            elif(p == 45):
                self.var_EntryMa.trace("w", self.var_Matiere45.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi45.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant45.set(self.select_enseignant.get()))
            
            elif(p == 46):
                self.var_EntryMa.trace("w", self.var_Matiere46.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi46.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant46.set(self.select_enseignant.get()))
            
            elif(p == 47):
                self.var_EntryMa.trace("w", self.var_Matiere47.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi47.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant47.set(self.select_enseignant.get()))
            
            elif(p == 51):
                self.var_EntryMa.trace("w", self.var_Matiere51.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi51.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant51.set(self.select_enseignant.get()))
            
            elif(p == 52):
                self.var_EntryMa.trace("w", self.var_Matiere52.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi52.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant52.set(self.select_enseignant.get()))
            
            elif(p == 53):
                self.var_EntryMa.trace("w", self.var_Matiere53.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi53.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant53.set(self.select_enseignant.get()))
            
            elif(p == 54):
                self.var_EntryMa.trace("w", self.var_Matiere54.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi54.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant54.set(self.select_enseignant.get()))
            
            elif(p == 55):
                self.var_EntryMa.trace("w", self.var_Matiere55.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi55.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant55.set(self.select_enseignant.get()))
            
            elif(p == 56):
                self.var_EntryMa.trace("w", self.var_Matiere56.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi56.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant56.set(self.select_enseignant.get()))
            
            elif(p == 57):
                self.var_EntryMa.trace("w", self.var_Matiere57.set(self.select_matiere.get()))
                self.var_EntryA.trace("w", self.var_Amphi57.set(self.select_amphi.get()))
                self.var_EntryE.trace("w", self.var_Enseignant57.set(self.select_enseignant.get()))
            
            #print(self.dico)
            self.var_EntryMa = StringVar()
            self.var_EntryA = StringVar()
            self.var_EntryE = StringVar()
            """self.select_amphi.destroy()
            self.select_enseignant.destroy()
            self.select_matiere.destroy()"""
            
            self.form.destroy()
            
            #self.fenetre.update()
    
    
    def charger(self, filiere, niveau, dico, b = 0):
        self.filiere.set(filiere)
        self.niveau.set(niveau)
        for p in dico.keys():
            
            if (p == 11):
                self.var_EntryMa.trace("w",  self.var_Matiere11.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi11.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant11.set(dico[p][2]))
                if(b or self.var_Amphi11.get() != "" or self.var_Enseignant11.get() != "" or self.var_Matiere11.get() != ""):
                    self.dico[p] = (self.var_Matiere11.get(), self.var_Amphi11.get(), self.var_Enseignant11.get())

            elif(p == 12):
                self.var_EntryMa.trace("w", self.var_Matiere12.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi12.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant12.set(dico[p][2]))
                if(b or self.var_Amphi12.get() != "" or self.var_Enseignant12.get() != "" or self.var_Matiere12.get() != ""):
                    self.dico[p] = (self.var_Matiere12.get(), self.var_Amphi12.get(), self.var_Enseignant12.get())

            elif(p == 13):
                self.var_EntryMa.trace("w", self.var_Matiere13.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi13.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant13.set(dico[p][2]))
                if(b or self.var_Amphi13.get() != "" or self.var_Enseignant13.get() != "" or self.var_Matiere13.get() != ""):
                    self.dico[p] = (self.var_Matiere13.get(), self.var_Amphi13.get(), self.var_Enseignant13.get())

            elif(p == 14):
                self.var_EntryMa.trace("w", self.var_Matiere14.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi14.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant14.set(dico[p][2]))
                if(b or self.var_Amphi14.get() != "" or self.var_Enseignant14.get() != "" or self.var_Matiere14.get() != ""):
                    self.dico[p] = (self.var_Matiere14.get(), self.var_Amphi14.get(), self.var_Enseignant14.get())

            elif(p == 15):
                self.var_EntryMa.trace("w", self.var_Matiere15.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi15.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant15.set(dico[p][2]))
                if(b or self.var_Amphi15.get() != "" or self.var_Enseignant15.get() != "" or self.var_Matiere15.get() != ""):
                    self.dico[p] = (self.var_Matiere15.get(), self.var_Amphi15.get(), self.var_Enseignant15.get())

            elif(p == 16):
                self.var_EntryMa.trace("w", self.var_Matiere16.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi16.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant16.set(dico[p][2]))
                if(b or self.var_Amphi16.get() != "" or self.var_Enseignant16.get() != "" or self.var_Matiere16.get() != ""):
                    self.dico[p] = (self.var_Matiere16.get(), self.var_Amphi16.get(), self.var_Enseignant16.get())

            elif(p == 17):
                self.var_EntryMa.trace("w", self.var_Matiere17.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi17.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant17.set(dico[p][2]))
                if(b or self.var_Amphi17.get() != "" or self.var_Enseignant17.get() != "" or self.var_Matiere17.get() != ""):
                    self.dico[p] = (self.var_Matiere17.get(), self.var_Amphi17.get(), self.var_Enseignant17.get())

            elif(p == 21):
                self.var_EntryMa.trace("w", self.var_Matiere21.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi21.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant21.set(dico[p][2]))
                if(b or self.var_Amphi21.get() != "" or self.var_Enseignant21.get() != "" or self.var_Matiere21.get() != ""):
                    self.dico[p] = (self.var_Matiere21.get(), self.var_Amphi21.get(), self.var_Enseignant21.get())

            elif(p == 22):
                self.var_EntryMa.trace("w", self.var_Matiere22.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi22.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant22.set(dico[p][2]))
                if(b or self.var_Amphi22.get() != "" or self.var_Enseignant22.get() != "" or self.var_Matiere22.get() != ""):
                    self.dico[p] = (self.var_Matiere22.get(), self.var_Amphi22.get(), self.var_Enseignant22.get())

            elif(p == 23):
                self.var_EntryMa.trace("w", self.var_Matiere23.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi23.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant23.set(dico[p][2]))
                if(b or self.var_Amphi23.get() != "" or self.var_Enseignant23.get() != "" or self.var_Matiere23.get() != ""):
                    self.dico[p] = (self.var_Matiere23.get(), self.var_Amphi23.get(), self.var_Enseignant23.get())

            elif(p == 24):
                self.var_EntryMa.trace("w", self.var_Matiere24.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi24.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant24.set(dico[p][2]))
                if(b or self.var_Amphi24.get() != "" or self.var_Enseignant24.get() != "" or self.var_Matiere24.get() != ""):
                    self.dico[p] = (self.var_Matiere24.get(), self.var_Amphi24.get(), self.var_Enseignant24.get())

            elif(p == 25):
                self.var_EntryMa.trace("w", self.var_Matiere25.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi25.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant25.set(dico[p][2]))
                if(b or self.var_Amphi25.get() != "" or self.var_Enseignant25.get() != "" or self.var_Matiere25.get() != ""):
                    self.dico[p] = (self.var_Matiere25.get(), self.var_Amphi25.get(), self.var_Enseignant25.get())

            elif(p == 26):
                self.var_EntryMa.trace("w", self.var_Matiere26.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi26.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant26.set(dico[p][2]))
                if(b or self.var_Amphi26.get() != "" or self.var_Enseignant26.get() != "" or self.var_Matiere26.get() != ""):
                    self.dico[p] = (self.var_Matiere26.get(), self.var_Amphi26.get(), self.var_Enseignant26.get())

            elif(p == 27):
                self.var_EntryMa.trace("w", self.var_Matiere27.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi27.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant27.set(dico[p][2]))
                if(b or self.var_Amphi27.get() != "" or self.var_Enseignant27.get() != "" or self.var_Matiere27.get() != ""):
                    self.dico[p] = (self.var_Matiere27.get(), self.var_Amphi27.get(), self.var_Enseignant27.get())

            elif(p == 31):
                self.var_EntryMa.trace("w", self.var_Matiere31.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi31.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant31.set(dico[p][2]))
                if(b or self.var_Amphi31.get() != "" or self.var_Enseignant31.get() != "" or self.var_Matiere31.get() != ""):
                    self.dico[p] = (self.var_Matiere31.get(), self.var_Amphi31.get(), self.var_Enseignant31.get())

            elif(p == 32):
                self.var_EntryMa.trace("w", self.var_Matiere32.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi32.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant32.set(dico[p][2]))
                if(b or self.var_Amphi32.get() != "" or self.var_Enseignant32.get() != "" or self.var_Matiere32.get() != ""):
                    self.dico[p] = (self.var_Matiere32.get(), self.var_Amphi32.get(), self.var_Enseignant32.get())

            elif(p == 33):
                self.var_EntryMa.trace("w", self.var_Matiere33.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi33.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant33.set(dico[p][2]))
                if(b or self.var_Amphi33.get() != "" or self.var_Enseignant33.get() != "" or self.var_Matiere33.get() != ""):
                    self.dico[p] = (self.var_Matiere33.get(), self.var_Amphi33.get(), self.var_Enseignant33.get())

            elif(p == 34):
                self.var_EntryMa.trace("w", self.var_Matiere34.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi34.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant34.set(dico[p][2]))
                if(b or self.var_Amphi34.get() != "" or self.var_Enseignant34.get() != "" or self.var_Matiere34.get() != ""):
                    self.dico[p] = (self.var_Matiere34.get(), self.var_Amphi34.get(), self.var_Enseignant34.get())

            elif(p == 35):
                self.var_EntryMa.trace("w", self.var_Matiere35.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi35.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant35.set(dico[p][2]))
                if(b or self.var_Amphi35.get() != "" or self.var_Enseignant35.get() != "" or self.var_Matiere35.get() != ""):
                    self.dico[p] = (self.var_Matiere35.get(), self.var_Amphi35.get(), self.var_Enseignant35.get())

            elif(p == 36):
                self.var_EntryMa.trace("w", self.var_Matiere36.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi36.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant36.set(dico[p][2]))
                if(b or self.var_Amphi36.get() != "" or self.var_Enseignant36.get() != "" or self.var_Matiere36.get() != ""):
                    self.dico[p] = (self.var_Matiere36.get(), self.var_Amphi36.get(), self.var_Enseignant36.get())

            elif(p == 37):
                self.var_EntryMa.trace("w", self.var_Matiere37.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi37.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant37.set(dico[p][2]))
                if(b or self.var_Amphi37.get() != "" or self.var_Enseignant37.get() != "" or self.var_Matiere37.get() != ""):
                    self.dico[p] = (self.var_Matiere37.get(), self.var_Amphi37.get(), self.var_Enseignant37.get())

            elif(p == 41):
                self.var_EntryMa.trace("w", self.var_Matiere41.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi41.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant41.set(dico[p][2]))
                if(b or self.var_Amphi41.get() != "" or self.var_Enseignant41.get() != "" or self.var_Matiere41.get() != ""):
                    self.dico[p] = (self.var_Matiere41.get(), self.var_Amphi41.get(), self.var_Enseignant41.get())

            elif(p == 42):
                self.var_EntryMa.trace("w", self.var_Matiere42.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi42.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant42.set(dico[p][2]))
                if(b or self.var_Amphi42.get() != "" or self.var_Enseignant42.get() != "" or self.var_Matiere42.get() != ""):
                    self.dico[p] = (self.var_Matiere42.get(), self.var_Amphi42.get(), self.var_Enseignant42.get())

            elif(p == 43):
                self.var_EntryMa.trace("w", self.var_Matiere43.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi43.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant43.set(dico[p][2]))
                if(b or self.var_Amphi43.get() != "" or self.var_Enseignant43.get() != "" or self.var_Matiere43.get() != ""):
                    self.dico[p] = (self.var_Matiere43.get(), self.var_Amphi43.get(), self.var_Enseignant43.get())

            elif(p == 44):
                self.var_EntryMa.trace("w", self.var_Matiere44.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi44.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant44.set(dico[p][2]))
                if(b or self.var_Amphi44.get() != "" or self.var_Enseignant44.get() != "" or self.var_Matiere44.get() != ""):
                    self.dico[p] = (self.var_Matiere44.get(), self.var_Amphi44.get(), self.var_Enseignant44.get())

            elif(p == 45):
                self.var_EntryMa.trace("w", self.var_Matiere45.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi45.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant45.set(dico[p][2]))
                if(b or self.var_Amphi45.get() != "" or self.var_Enseignant45.get() != "" or self.var_Matiere45.get() != ""):
                    self.dico[p] = (self.var_Matiere45.get(), self.var_Amphi45.get(), self.var_Enseignant45.get())

            elif(p == 46):
                self.var_EntryMa.trace("w", self.var_Matiere46.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi46.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant46.set(dico[p][2]))
                if(b or self.var_Amphi46.get() != "" or self.var_Enseignant46.get() != "" or self.var_Matiere46.get() != ""):
                    self.dico[p] = (self.var_Matiere46.get(), self.var_Amphi46.get(), self.var_Enseignant46.get())

            elif(p == 47):
                self.var_EntryMa.trace("w", self.var_Matiere47.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi47.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant47.set(dico[p][2]))
                if(b or self.var_Amphi47.get() != "" or self.var_Enseignant47.get() != "" or self.var_Matiere47.get() != ""):
                    self.dico[p] = (self.var_Matiere47.get(), self.var_Amphi47.get(), self.var_Enseignant47.get())

            elif(p == 51):
                self.var_EntryMa.trace("w", self.var_Matiere51.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi51.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant51.set(dico[p][2]))
                if(b or self.var_Amphi51.get() != "" or self.var_Enseignant51.get() != "" or self.var_Matiere51.get() != ""):
                    self.dico[p] = (self.var_Matiere51.get(), self.var_Amphi51.get(), self.var_Enseignant51.get())

            elif(p == 52):
                self.var_EntryMa.trace("w", self.var_Matiere52.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi52.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant52.set(dico[p][2]))
                if(b or self.var_Amphi52.get() != "" or self.var_Enseignant52.get() != "" or self.var_Matiere52.get() != ""):
                    self.dico[p] = (self.var_Matiere52.get(), self.var_Amphi52.get(), self.var_Enseignant52.get())

            elif(p == 53):
                self.var_EntryMa.trace("w", self.var_Matiere53.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi53.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant53.set(dico[p][2]))
                if(b or self.var_Amphi53.get() != "" or self.var_Enseignant53.get() != "" or self.var_Matiere53.get() != ""):
                    self.dico[p] = (self.var_Matiere53.get(), self.var_Amphi53.get(), self.var_Enseignant53.get())

            elif(p == 54):
                self.var_EntryMa.trace("w", self.var_Matiere54.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi54.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant54.set(dico[p][2]))
                if(b or self.var_Amphi54.get() != "" or self.var_Enseignant54.get() != "" or self.var_Matiere54.get() != ""):
                    self.dico[p] = (self.var_Matiere54.get(), self.var_Amphi54.get(), self.var_Enseignant54.get())

            elif(p == 55):
                self.var_EntryMa.trace("w", self.var_Matiere55.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi55.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant55.set(dico[p][2]))
                if(b or self.var_Amphi55.get() != "" or self.var_Enseignant55.get() != "" or self.var_Matiere55.get() != ""):
                    self.dico[p] = (self.var_Matiere55.get(), self.var_Amphi55.get(), self.var_Enseignant55.get())

            elif(p == 56):
                self.var_EntryMa.trace("w", self.var_Matiere56.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi56.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant56.set(dico[p][2]))
                if(b or self.var_Amphi56.get() != "" or self.var_Enseignant56.get() != "" or self.var_Matiere56.get() != ""):
                    self.dico[p] = (self.var_Matiere56.get(), self.var_Amphi56.get(), self.var_Enseignant56.get())

            elif(p == 57):
                self.var_EntryMa.trace("w", self.var_Matiere57.set(dico[p][0]))
                self.var_EntryA.trace("w", self.var_Amphi57.set(dico[p][1]))
                self.var_EntryE.trace("w", self.var_Enseignant57.set(dico[p][2]))
                if(b or self.var_Amphi57.get() != "" or self.var_Enseignant57.get() != "" or self.var_Matiere57.get() != ""):
                    self.dico[p] = (self.var_Matiere57.get(), self.var_Amphi57.get(), self.var_Enseignant57.get())
        self.var_EntryMa = StringVar()
        self.var_EntryA = StringVar()
        self.var_EntryE = StringVar()
        self.res_matieres = Lecture_BD.get_matiereFN(filiere, niveau)


    def update_matiere(self, event):
        for item in self.info:
            if(item[0] == self.filiere.get() and item[1] == self.niveau.get()):
                messagebox.showinfo("Attention!!!","Une page a déjà été créee avec cette filière et ce niveau (page {})".format(self.info.index(item)+1))
                break
        self.res_matieres = Lecture_BD.get_matiereFN(self.filiere.get(), self.niveau.get())
    
    def update_AmphiEnseignant(self):
        self.res_amphis  = Lecture_BD.get_amphi(self.select_matiere.get())
        self.res_enseignants = Lecture_BD.get_enseignant(self.select_matiere.get())
        self.select_amphi["values"] = self.res_amphis
        self.select_enseignant["values"] = self.res_enseignants
        
    def clear(self):
        self.charger(self.clear_filiere, self.clear_niveau, self.clear_dico, 0)
        
"""r = Tk()

p = Page(r,0,0,00,400)
p.fenetre.mainloop()"""