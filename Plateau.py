from tkinter import*
from random import*


fen=Tk()
fen.geometry("1000x1000")
can=Canvas(fen,width=1000, height=1000, bg='gold')
can.place(x=0,y=0)

#Faire affichage debut plusieur mouton position aléatoire

class Plateau:
    def __init__(self,x,y):
        self.abscisse=x
        self.ordonnee=y
        self.M=Mouton(210,70,"Mouton",10)
        self.L=Loup(210,55,"Loup",5)
        self.Case=[]
        self.ligne=0
        self.colonne=0
        self.Ani=[None]*100
        self.both=[None]*3

    def case(self):
        i=0
        for trop in range(10):
            for loop in range(10):
                self.Case.append({'Ligne':self.ligne})
                self.Case[i]['Colonne']=self.colonne
                self.Case[i]['XMouton']=self.M.abscisseM+50*loop
                self.Case[i]['YMouton']=self.M.ordonneeM+50*trop
                self.Case[i]['XLoup']=self.L.abscisseL+50*loop
                self.Case[i]['YLoup']=self.L.ordonneeL+50*trop
                self.Case[i]['nbCaseCompteur']=i
                self.ligne+=1
                i=i+1
            self.colonne+=1
            self.ligne=0
        #print(self.Case)


    def afficheHerbe(self):
        c = 0
        abscisse = 200
        ordonnee = 50
        for i in range(10):
            for j in range(10):
                if self.Case[c]['Herbe'] == True:
                    can.create_rectangle(abscisse,ordonnee,abscisse + 50 ,ordonnee +50, fill = 'green')
                c += 1
                abscisse += 50
            abscisse = 200
            ordonnee += 50






    def pousseherbe(self):
        self.herbe=[None]*30

        for i in range(30):
            self.herbe[i]=(randint(0,10),randint(0,10))
        i=0
        for trop in range(10):
            for loop in range(10):
                if (self.Case[i]['Ligne'],self.Case[i]['Colonne']) in self.herbe:
                    self.Case[i]['Herbe']=True
                else:
                    self.Case[i]['Herbe']=False
                i=i+1

    def affichageP(self):
        colonne=0
        ligne=0
        while colonne<=10:
            can.create_line(self.abscisse,self.ordonnee,self.abscisse,self.ordonnee+500)
            colonne+=1
            self.abscisse+=50

        while ligne<=10:
            can.create_line(self.abscisse-50,self.ordonnee,self.abscisse-550,self.ordonnee)
            ligne+=1
            self.ordonnee+=50


class Mouton:
    def __init__(self,x,y,num,QM):
        self.abscisseM=x
        self.ordonneeM=y
        self.nameM="Mouton"
        self.nbMc=[0]*100
        self.dx=-5
        self.dy=-5
        self.Oinitial=self.ordonneeM
        self.Ainitial=self.abscisseM
        self.ale=0
        self.i=1
        self.num=num                                # sert à nommer chaque objet
        self.tuples=(self.abscisseM,self.ordonneeM)
        self.quantite_mangee = QM


    def AffichageMouton(self):

        can.create_arc(self.abscisseM, self.ordonneeM-30, self.abscisseM+30, self.ordonneeM+20, start=180, extent=180, fill="snow",outline="black",tags=str(self.num))
        can.create_rectangle(self.abscisseM,self.ordonneeM,self.abscisseM+25,self.ordonneeM, fill='snow', outline='black',tags=str(self.num))
        for rond in range(4):
            can.create_oval(self.abscisseM-3 + 8*rond,self.ordonneeM-7,self.abscisseM+7 +8 *rond,self.ordonneeM+3,fill='snow',outline='snow',tags=str(self.num))

    def deplacerM(self,ale):
        if ale == 'H':
            if self.ordonneeM > self.Oinitial - 50:#print(self.ordonneeM,self.Oinitial-50) | Si Y est après Y attendu
                self.ordonneeM+=self.dy
            else:
               self.i=0
               self.Oinitial-=50
               #self.ordonneeM= self.Oinitial


        if ale == 'D':
            if  self.abscisseM < self.Ainitial + 50:#print(self.abscisseM,self.Ainitial+50) | Si X est avant X attendu
                self.abscisseM -= self.dx
            else:
               self.i=0
               self.Ainitial+=50
               #self.abscisseM=self.Ainitial


        if ale == 'B':
            if self.ordonneeM < self.Oinitial +50: #print(self.ordonneeM,self.Oinitial+50) | Si Y est avant Y attendu
                self.ordonneeM-=self.dy

            else:
               self.i=0
               self.Oinitial+=50
               #self.ordonneeM= self.Oinitial


        if ale == 'G':
            if self.abscisseM > self.Ainitial - 50:#print(self.abscisseM,self.Ainitial-50) | Si X est apès X attendu
                self.abscisseM += self.dx
            else:
               self.i=0
               self.Ainitial-=50
               #self.abscisseM=self.Ainitial





    def animationM(self):
        self.deplacerM(self.ale)
        if self.num==str(self.num):
            can.delete(str(self.num))

        self.AffichageMouton()
        if self.i !=0:                              #condition d'arrêt de récursivité
            can.after(50, self.animationM)          #Attend 50ms puis recursivité

    def tours(self):                                #Unir animationL() et aleatoire()
        self.ale=self.aleatoire()
        if (210 < self.abscisseM-50 and self.ale=="G") or (self.abscisseM+50<660 and self.ale=="D") or (55<self.ordonneeM - 50 and self.ale=="H") or (self.ordonneeM+50 < 500 and self.ale=="B"):
            self.animationM()
            self.NouvelleCoordonnee()
        else:
            self.tuples=(self.Ainitial,self.Oinitial)

    def NouvelleCoordonnee(self):
        if self.ale=="H":
            self.tuples=(self.abscisseM,self.ordonneeM-45)
        if self.ale=="D":
            self.tuples=(self.abscisseM+45,self.ordonneeM)
        if self.ale=="B":
            self.tuples=(self.abscisseM,self.ordonneeM+45)
        if self.ale=="G":
            self.tuples=(self.abscisseM-45,self.ordonneeM)


    def aleatoire(self):
        direction=["Haut","Droite","Bas","Gauche"]
        nombre= randint(0,3)
        if direction[nombre]=="Haut":
            return 'H'
        if direction[nombre]=="Droite":
            return 'D'
        if direction[nombre]=="Bas":
            return 'B'
        if direction[nombre]=="Gauche":
            return 'G'



    def quantitemangeeparM(self,case):
        if self.tuples == (case['XMouton'], case['YMouton']) and case['Herbe']:
            self.quantite_mangee= self.quantite_mangee+1
        else:
            self.quantite_mangee=self.quantite_mangee-1
        if self.mortM():
            can.delete(str(self.num))
            #print(self.quantite_mangee)
        return self.quantite_mangee


    def mortM(self):
        if self.quantite_mangee == 0:
            can.create_arc(self.abscisseM, self.ordonneeM-30, self.abscisseM+30, self.ordonneeM+20, start=180, extent=180, fill="red",outline="black",tags=str(self.num))
            can.create_rectangle(self.abscisseM,self.ordonneeM,self.abscisseM+25,self.ordonneeM, fill='red', outline='black',tags=str(self.num))
            for rond in range(4):
                can.create_oval(self.abscisseM-3 + 8*rond,self.ordonneeM-7,self.abscisseM+7 +8 *rond,self.ordonneeM+3,fill='red',outline='red',tags=str(self.num))



class Loup:
    def __init__(self,x,y,num,QM):
        self.abscisseL=x
        self.ordonneeL=y
        self.nameL='Loup'
        self.nbLc=[0]*100
        self.dx=-10
        self.dy=-10
        self.Oinitial=self.ordonneeL
        self.Ainitial=self.abscisseL
        self.ale=0
        self.i=1
        self.num=num                                # sert à nommer chaque objet
        self.tuples=(self.abscisseL,self.ordonneeL)
        self.quantite_mangee = QM
        self.Atuer=False
        self.Lequel=(0,0)


    def AffichageL(self):

            can.create_polygon(self.abscisseL, self.ordonneeL-7.5,
                           self.abscisseL+7.5, self.ordonneeL+7.5,
                           self.abscisseL+22.5, self.ordonneeL+7.5,
                           self.abscisseL+30, self.ordonneeL-7.5,
                           self.abscisseL+37.5, self.ordonneeL+22.5,
                           self.abscisseL+15, self.ordonneeL+45,
                           self.abscisseL-7.5, self.ordonneeL+22.5,fill = '#696969',
                               tags=str(self.num))


    def ModifLcase(self,nouveau):
        self.nbLc=nouveau
        return self.nbLc

    def deplacerL(self,ale):
        if ale == 'H':
            if self.ordonneeL >self.Oinitial -50:#print(self.ordonneeL,self.Oinitial-50) | Si Y est après Y attendu
                self.ordonneeL+=self.dy

            else:
               self.i=0
               self.Oinitial-=50

        if ale == 'D':
            if  self.abscisseL < self.Ainitial +50 :#print(self.abscisseL,self.Ainitial+50) | Si X est avant X attendu
                self.abscisseL -= self.dx
            else:
               self.i=0
               self.Ainitial+=50

        if ale == 'B':
            if self.ordonneeL < self.Oinitial +50: #print(self.ordonneeL,self.Oinitial+50) | Si Y est avant Y attendu
                self.ordonneeL-=self.dy

            else:
               self.i=0
               self.Oinitial+=50

        if ale == 'G':
            if self.abscisseL > self.Ainitial - 50:#print(self.abscisseL,self.Ainitial-50) | Si X est apès X attend
                self.abscisseL += self.dx
            else:
               self.i=0
               self.Ainitial-=50

    def animationL(self):
        self.deplacerL(self.ale)
        if self.num==str(self.num):
            can.delete(str(self.num))  #si tag est égal au nom du loup (ex:Loup1) supprimer que l'objet ayant ce tag

        self.AffichageL()
        if self.i !=0:                              #condition d'arrêt de récursivité
            can.after(50, self.animationL)          #Attend 50ms puis recursivité

    def tours(self):                                #Unir animationL() et aleatoire()

        self.ale=self.aleatoire()
        #print(self.ale)
        if (210 < self.abscisseL-50 and self.ale=="G") or (self.abscisseL+50<=660 and self.ale=="D") or (70<self.ordonneeL - 50 and self.ale=="H") or (self.ordonneeL+50 < 520 and self.ale=="B"):
            self.animationL()
            self.NouvelleCoordonnee()
        else:
            self.tuples=(self.Ainitial,self.Oinitial)

    def NouvelleCoordonnee(self):
        if self.ale=="H":
            self.tuples=(self.abscisseL,self.ordonneeL-40)
        if self.ale=="D":
            self.tuples=(self.abscisseL+40,self.ordonneeL)
        if self.ale=="B":
            self.tuples=(self.abscisseL,self.ordonneeL+40)
        if self.ale=="G":
            self.tuples=(self.abscisseL-40,self.ordonneeL)

    def aleatoire(self):
        direction=["Haut","Droite","Bas","Gauche"]
        nombre= randint(0,3)
        if direction[nombre]=="Haut":
            return 'H'
        if direction[nombre]=="Droite":
            return 'D'
        if direction[nombre]=="Bas":
            return 'B'
        if direction[nombre]=="Gauche":
            return 'G'

    def quantitemangeeparL(self,case,TabMoutonT):
        for i in range(len(TabMoutonT)):
            if (case['XLoup'],case['YLoup'])== TabMoutonT[ i]:
                self.quantite_mangee= self.quantite_mangee+1
                self.TuerMouton(TabMoutonT[i],i)
            else:
                self.quantite_mangee=self.quantite_mangee-1
        if self.mortL():
            can.delete(str(self.num))
            #print(self.quantite_mangee)
        return self.quantite_mangee

    def TuerMouton(self,T,i):
        self.Atuer=True
        self.Lequel=(T[0],T[1],i)

    def mortL(self):
        if self.quantite_mangee == 0:

            can.create_polygon(self.abscisseL, self.ordonneeL-7.5,
                           self.abscisseL+7.5, self.ordonneeL+7.5,
                           self.abscisseL+22.5, self.ordonneeL+7.5,
                           self.abscisseL+30, self.ordonneeL-7.5,
                           self.abscisseL+37.5, self.ordonneeL+22.5,
                           self.abscisseL+15, self.ordonneeL+45,
                           self.abscisseL-7.5, self.ordonneeL+22.5,fill = 'red',
                               tags=str(self.num))


class Experience:

    def __init__(self,nbL,nbM):

        self.P=Plateau(200,50)
        self.P.affichageP()
        self.P.case()
        self.P.pousseherbe()
        self.tour=0
        self.Loup=[]
        self.Mouton=[]
        self.P.afficheHerbe()
        self.HerbeMangee=[10]*4 # tableau dynamique du stockage d'herbe mangé par chaque Mouton
        self.MoutonMangee=[5]*4
        self.nbL=nbL # Nombre de Loup sur le plateau
        self.nbM=nbM # Nombre de Mouton sur le plateau
        self.NombreMoutonTotal=4 #Nombre total de Mouton qu'il a eu au cours de la simulation
        self.MortM=[False]*4
        self.MortL=[False]*4
        self.nbTOTALL=4

    def DicodeCASE(self,name):
        t=0
        for c in self.P.Case:
            if name=='Loup':
                if c['XLoup'] == self.prochainX and c['YLoup']== self.prochainY:
                    t=c
            if name=='Mouton':
                if c['XMouton']== self.prochainX and self.prochainY== c['YMouton']:
                    t=c
        return t



    def debut(self):

        #Loups
        for L in range(self.nbL):
            self.prochainX=self.P.Case[randint(0,99)]['XLoup']
            self.prochainY=self.P.Case[randint(0,99)]['YLoup']

            Loups=Loup(self.prochainX,self.prochainY,"Loup"+str(L+1),5)
            Loups.AffichageL()
            self.Loup.append((self.prochainX,self.prochainY))


        #Moutons

        for M in range(self.nbM):
            self.prochainX=self.P.Case[randint(0,99)]['XMouton']
            self.prochainY=self.P.Case[randint(0,99)]['YMouton']
            Moutons=Mouton(self.prochainX,self.prochainY,"Mouton"+str(M+1),10)
            Moutons.AffichageMouton()
            self.Mouton.append((self.prochainX,self.prochainY))

        self.depla()

    def depla(self):

        for i in range (self.nbTOTALL):
            if self.MortL[i]==False:
                app=Loup(self.Loup[i][0],self.Loup[i][1],"Loup"+str(i+1),self.MoutonMangee[i])
                app.tours()

                self.Loup[i]=app.tuples

                self.prochainX=self.Loup[i][0]
                self.prochainY=self.Loup[i][1]
                c=self.DicodeCASE("Loup")

                self.MoutonMangee[i]==app.quantitemangeeparL(c,self.Mouton)
                #print(self.MoutonMangee[i])
                if app.Atuer:
                    A=app.Lequel[2]
                    self.MortM[A]=True
                    self.nbM-=1
                    self.Mouton[A]=None
                    #print("oui")

                if self.MoutonMangee[i] ==0:
                    self.MortM[i]=True
                    self.nbL-=1
                    app.mortL()
                    self.Loup[i]=None

            else:
                can.delete("Loup"+str(i+1))


        for i in  range(self.NombreMoutonTotal):
            if self.MortM[i]==False:
                app=Mouton(self.Mouton[i][0],self.Mouton[i][1],"Mouton"+str(i+1),self.HerbeMangee[i])
                app.tours()

                self.Mouton[i]=app.tuples


                self.prochainX=self.Mouton[i][0]
                self.prochainY=self.Mouton[i][1]
                c=self.DicodeCASE("Mouton")                  #print(c)

                self.HerbeMangee[i]=app.quantitemangeeparM(c)
                self.reproductionM(self.prochainX,self.prochainY)
                if self.HerbeMangee[i] ==0: #LAURE
                    self.MortM[i]=True
                    self.nbM-=1
                    app.mortM()
                    self.Mouton[i]=None
            else:
                 can.delete("Mouton"+str(i+1))

                                                        #print(self.HerbeMangee[0],self.Mouton[i])
        self.tour+=1
        if self.tour<=2 and self.nbM>0 and self.nbL>0:
            can.after(3000,self.depla)
        else:
            for i in range(self.NombreMoutonTotal):

                app=Mouton(self.Mouton[i][0],self.Mouton[i][1],"Mouton",self.HerbeMangee[i])
                self.MortM=[None]*self.NombreMoutonTotal
                can.delete("Mouton")
            Fin=Statistique()
            Fin.Affichage(self.NombreMoutonTotal,self.nbTOTALL,self.nbM,self.nbL)

        #print(self.tour)

    def reproductionM(self,X,Y): #LAURE
        chance=[True,False,False,False]
        compteur=0
        for i in self.Mouton:
            if (X,Y)== i:
                compteur+=1
                if compteur>1:
                    if chance[randint(0,3)]==True:
                        self.nbM+=1
                        self.NombreMoutonTotal+=1
                        self.HerbeMangee.append(10)
                        self.MortM.append(False)
                        self.Mouton.append((X,Y))



commence=Experience(4,4)
commence.debut()

class Statistique: #LAURE
    def Affichage(self,NTM,NTL,nbM,nbL):
        can.after(1000)
        can.create_rectangle(0,0,1000,1000,fill='black')
        can.create_text(500, 100, text="Fin de la Simulation", font=('Arial', 36, 'bold'), fill='white') #Emily
        can.after(1000)
        can.delete("Mouton")
        can.create_text(550, 200, text=NTM, font=('Arial', 28, 'bold'), fill='white')
        can.create_text(220, 200, text="Nombre de Mouton Total:", font=('Arial', 20, 'bold'), fill='white')
        can.create_text(220, 300, text="Nombre de Loup au Total:", font=('Arial', 20, 'bold'), fill='white')
        can.create_text(550, 300, text=NTL, font=('Arial', 28, 'bold'), fill='white')
        can.create_text(550, 400, text=nbM, font=('Arial', 20, 'bold'), fill='white')
        can.create_text(550, 500, text=nbL, font=('Arial', 20, 'bold'), fill='white')
        can.create_text(220, 400, text="Nombre de Mouton vivant:", font=('Arial', 20, 'bold'), fill='white')
        can.create_text(220, 500, text="Nombre de Loup vivant:", font=('Arial', 20, 'bold'), fill='white')


fen.mainloop()