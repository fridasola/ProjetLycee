from tkinter import *
from PIL import ImageTk, Image
from random import *
import time

class Proteine:
    def __init__(self,fen,can):
        self.x=50
        self.y=50
        self.etat="Crue"
        self.fen=fen
        self.canvas=can

    def Poulet(self):
        self.img_boutonpoulet = ImageTk.PhotoImage(Image.open("pouletbouton.png"))
        self.img_friteuseoff=ImageTk.PhotoImage(Image.open("friteuse.png"))
        self.img_friteuseon = ImageTk.PhotoImage(Image.open("friteusepoulet.png"))
        self.img_pillon=ImageTk.PhotoImage(Image.open("pillon.png"))

        self.mon_bouton = Button(self.fen, image=self.img_boutonpoulet, bg='white', command=self.afficher_pillon)
        self.canvas.create_window(45, 110, anchor=NW, window=self.mon_bouton)



    def afficher_pillon(self):
        self.canvas.create_image(300, 350, image=self.img_friteuseon, anchor="nw")
        duree=3
        while duree >= 0:
            time.sleep(1)
            self.canvas.create_text(70, 60, text="Poulet:"+str(duree)+"s", fill="black", font=('Helvetica 15 bold'),tags="tempsPoulet")
            self.fen.update()
            if duree == 0:
                self.canvas.delete("tempsPoulet")
                self.servir()
            duree-=1
            self.canvas.delete("tempsPoulet")

    def servir(self):
        self.img_friteuseoff=ImageTk.PhotoImage(Image.open("friteuse.png"))
        self.canvas.create_image(300,350,image=self.img_friteuseoff, anchor="nw")
        self.canvas.create_image(550, 350, image=self.img_pillon, anchor="nw",tags="pillon")

    def deletepoulet(self):
        self.canvas.delete("pillon")


class Boisson:
    def __init__(self, fen, can):
        self.fen = fen
        self.canvas = can

    def Soda(self):
        self.img_soda = ImageTk.PhotoImage(Image.open("soda.png "))

        self.mon_bouton = Button(self.fen, image = self.img_soda, bg = "white", command = self.afficher_soda)
        self.canvas.create_window(45, 352,  anchor=NW, window = self.mon_bouton)

    def afficher_soda(self):
        self.canvas.create_image(500, 310, image=self.img_soda, anchor="nw",tags="soda")

    def deletesoda(self):
        self.canvas.delete("soda")


class Accompagnement:
    def __init__(self,fen,can):
        #self.etat = "Crue"
        self.fen = fen
        self.canvas = can

    def Frites(self):
        self.img_frite = ImageTk.PhotoImage(Image.open("friteusefrite.png"))
        self.img_paquetfrites = ImageTk.PhotoImage(Image.open("paquet_frites.png"))
        self.mon_bouton = Button(self.fen, image=self.img_paquetfrites, bg='white', command=self.afficher_friteuseFrite)
        self.canvas.create_window(45, 242, anchor=NW, window=self.mon_bouton)

    def afficher_friteuseFrite(self):
        self.canvas.create_image(200, 350, image=self.img_frite, anchor="nw")
        duree=3
        while duree >= 0:
            time.sleep(1)
            self.canvas.create_text(70, 40, text="Frites:"+str(duree)+"s", fill="black", font=('Helvetica 15 bold'),tags="tempsFrites")
            self.fen.update()
            if duree == 0:
                self.canvas.delete("tempsFrites")
                self.servir()
            duree-=1
            self.canvas.delete("tempsFrites")


    def servir(self):
        self.img_friteuseoff=ImageTk.PhotoImage(Image.open("friteuse.png"))
        self.canvas.create_image(200,350,image=self.img_friteuseoff, anchor="nw")
        self.canvas.create_image(400, 350, image=self.img_paquetfrites, anchor="nw",tags="frites")

    def deletefrite(self):
        self.canvas.delete("frites")


class Demande:
    def __init__(self,fen):
        self.fen = fen #fenetre
        self.fen.geometry("1200x700")
        self.fen.title("E&LFastCooker")
        self.canvas = Canvas(self.fen, width=1400, height=700)
        self.canvas.place(x=0, y=0)
        self.nbclient = 0
        self.heure = "midi"
        self.historique = [] #file des commandes
        self.P = Proteine(fen,self.canvas)
        self.B = Boisson(fen,self.canvas)
        self.A = Accompagnement(fen,self.canvas)
        self.fait=[]
        self.counter = 0
        self.running = False


    def Cuisine(self): #Afficher la cuisine, le restaurant
        self.img_bar = ImageTk.PhotoImage(file="fond.jpg") #fond
        self.canvas.create_image(150, 0, image=self.img_bar, anchor="nw")#affiche fond

        self.img_table = ImageTk.PhotoImage(Image.open("table-removebg-preview.png"))#photo de la table
        self.canvas.create_image(150, 400, image=self.img_table, anchor="nw")#affiche la table

        self.img_friteuseoff=ImageTk.PhotoImage(Image.open("friteuse.png"))
        self.canvas.create_image(300,350,image=self.img_friteuseoff, anchor="nw")
        self.canvas.create_image(200,350,image=self.img_friteuseoff, anchor="nw")

        self.commande()


    def counter_label(self,label):
        from datetime import datetime
        def count():
            if self.running:
                if self.counter==0:
                    self.display="Chargement..."
                else:
                    tt = datetime.fromtimestamp(self.counter)
                    string = tt.strftime("%M:%S")
                    self.display=string

                label['text']=self.display   # Or label.config(text=display)
                label.after(1000, count)
                self.counter += 1
        count()

    def Start(self,label):
        self.running=True #Go cliqué
        self.counter_label(label)
        start['state']='disabled'
        self.Cuisine()

    def commande(self):
        self.prendboisson = [True, True , False] #tableau de True et False
        self.prendproteine = [True, True, False]
        self.prendaccompagnement = [True, True, False]
        self.tupple = (self.prendboisson[randint(0,2)], self.prendproteine[randint(0,2)], self.prendaccompagnement[randint(0,2)])
        self.fait.append([False]*3)
        if not self.tupple[1]:
            self.fait[self.nbclient][0]=True
        if not self.tupple[0]:
            self.fait[self.nbclient][1]=True
        if not self.tupple[2]:
            self.fait[self.nbclient][2]=True
        self.affichage_commande()

    def affichage_commande(self):
        x=500
        print("client:",self.nbclient)
        if self.tupple[1]:
            self.canvas.create_text(x, 100, text="Poulet", fill="red", font=('Helvetica 15 bold'),tags="ProteineTF"+str(self.nbclient))
            x+=100
        if self.tupple[0]:
            self.canvas.create_text(x, 100, text="Boisson", fill="red", font=('Helvetica 15 bold'),tags="BoissonTF"+str(self.nbclient))
            x+=100
        if self.tupple[2]:
            self.canvas.create_text(x, 100, text="Frite", fill="red", font=('Helvetica 15 bold'),tags="AccompagnementTF"+str(self.nbclient))
        self.arrivee_client()

    def arrivee_client(self):
        self.historique.append(self.tupple)

        client=["client1.png","client2.png","client3.png","client4.png","client5.png",
                "client6.png","client7.png","client8.png","client9.png","client10.png",
                "client11.png","client12.png","client13.png","client14.png","client15.png"]
        self.img_client= ImageTk.PhotoImage(Image.open(client[randint(0,15)]))
        self.canvas.create_image(1000,200,image=self.img_client,anchor="nw",tags="client")

        print("tupple:",self.tupple)
        print("Historique",self.historique)
        self.préparation()


    def préparation(self):
        commande1 = self.historique[self.nbclient]
        if self.heure == 'midi':
            if commande1[0] == True:
                self.B.Soda()
            if commande1[1] == True:
                self.P.Poulet()
            if commande1[2] == True:
                self.A.Frites()

        self.fin_commande()


    def fin_commande(self):
        self.canvas.bind('<ButtonPress-1>', self.clic)

    def clic(self,evt):
        x= evt.x
        y=evt.y
        if 350<=y<=450 and 400<=x<=500:
            self.A.deletefrite()
            #self.canvas.delete("AccompagnementTF"+str(self.nbclient))
            self.fait[self.nbclient][2]=True
        if 350<=y<=450 and 550<=x<=650:
            self.P.deletepoulet()
            #self.canvas.delete("ProteineTF"+str(self.nbclient))
            self.fait[self.nbclient][0]=True
        if 310<=y<=410 and 500<=x<=600:
            self.B.deletesoda()
            #self.canvas.delete("BoissonTF"+str(self.nbclient))
            self.fait[self.nbclient][1]=True
        print("fait:",self.fait)

        if self.fait[self.nbclient]==[True]*3: #si tous les articles demander de la commande ont était servit
            self.nbclient+=1
            print("client:",self.nbclient)
            if self.nbclient>15:
                self.FinJeu()
            else:
                self.canvas.delete("client")
                self.commande() #On passe au prochain client

    def FinJeu(self):
        self.canvas=Canvas(self.fen,width=1400, height=700)
        self.canvas.place(x=0,y=0)#Affichage du temps, du fond
        self.img_fin = ImageTk.PhotoImage(file="paie.png")
        self.canvas.create_image(700,250, image=self.img_fin, anchor = "nw")
        self.canvas.create_text(600,200,text='BRAVO ! Vous avez fini votre service en :  ',fill="black",font=('Helvetica 40 bold'))
        self.canvas.create_text(600,300,text=str(self.display),fill="black",font=('Helvetica 40 bold'))






if __name__ == "__main__":
    fen = Tk()
    app = Demande(fen)
    fen.minsize(width=250, height=70)
    label =Label(fen, text="Commencer à cuisiner!", fg="black", font="Verdana 30 bold")
    label.pack()
    f = Frame(fen)
    start = Button(f, text='GO', width=6, command=lambda:app.Start(label))
    f.pack(anchor = 'center',pady=5)
    start.pack(side="left")

    fen.mainloop()




