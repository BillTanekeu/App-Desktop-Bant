from tkinter import Canvas, Label, Listbox, Tk, Button, constants, PhotoImage
from PIL import ImageTk,Image
from DAO import Lecture_BD
from Menu import CMenu
class Accueil:
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.iconphoto(True, PhotoImage("Images/logo.png"))
        for w in self.fenetre.winfo_children():
            w.destroy()

        # Mettre en plein ecran
        #self.fenetre.resizable(0,0)
        self.w , self.h = self.fenetre.winfo_screenwidth(), self.fenetre.winfo_screenheight()
        self.fenetre.geometry("%dx%d" %(self.w, self.h))
        self.fenetre.config(bg="#ADA69F")
        self.fenetre.title("Bant")
        self.canvas = Canvas(self.fenetre, width= self.w *2/3, height= self.h)
        self.canvas.grid(row = 0, column=0)
        self.img = Image.open("Images/font5.jpg")
        self.img = self.img.resize((int(self.w *2/3) ,int(self.h/1.1)))
        self.img1 = ImageTk.PhotoImage(image= self.img)
        self.l1 = Label(self.canvas, image= self.img1).place(x=0,y=0)

        """self.board = self.canvas.create_image(0,0, anchor = "nw", image= self.img1)
        #self.l1 = Label(self.fenetre, image= self.img1, width= self.w *2/3, height= self.h).place(x=0,y=0)

        self.img2 = ImageTk.PhotoImage(file = "Images/img deb.jpg")
        #self.l2 = Label(self.fenetre, image= self.img2, width= self.w *2/3, height= self.h).place(x=0,y=0)
"""
        self.img2 = Image.open("Images/bant.png")
        self.img3 = ImageTk.PhotoImage(image= self.img2)

        self.can_1 = Canvas(self.fenetre, width= (self.w - self.w *2/3), height= self.h, bg = "grey")
        self.can_1.grid(row = 0, column= 1)
        txt = "Réaliser les emplois du temps\n rapidement\n avec Bant"
        self.L_bienvenue = Label(self.can_1, image=self.img3, font=("calibri", 16), fg = 'Blue')
        self.L_bienvenue.place(x= 60, y = 20)

        self.img4 = Image.open("Images/commencer.png")
        self.img4 = self.img4.resize((130 ,40))
        self.img4 = ImageTk.PhotoImage(image= self.img4)
        self.B_new = Button(self.can_1,image= self.img4, font=("calibri", 20), bg ="#3B7DA3", fg ="yellow", command=self.Go)
        self.B_new.place(x = 60, y = 140)

        self.L_recent = Label(self.can_1, text= "Récent(s):", font=("calibri", 16))
        self.L_recent.place(x = 60, y = 260)
        self.la = Label(self.can_1, text="Projets récemments ouverts cliquer dessus pour charger", fg="green").place(x=60, y=290)
        self.Ls = Listbox(self.can_1, width= 30, bg="#DBD1CB",fg = "blue", font=("arial",16), justify="center")
        #self.Ls.bind("<<ListboxSelect>>", self.Go)

        self.Ls.place(x = 60, y = 320 )
        self.list_proj = Lecture_BD.get_projet()
        for k in self.list_proj.keys():
            self.Ls.insert(constants.END,k )

        self.fenetre.mainloop()
    

    def Go(self):
        CMenu(self.fenetre)
        #value = self.Ls.curselection()
        #print(self.Ls.get(value[0]))


Accueil()