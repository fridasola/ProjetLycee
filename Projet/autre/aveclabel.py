# Créé par emilynolesolorzano, le 01/01/2024 en Python 3.7

from tkinter import*
from PIL import ImageTk, Image


fen=Tk()
fen.geometry("1200x700")
fen.title("E&LFastCooker")
can=Canvas(fen,width=1400, height=700)
can.place(x=0,y=0)

imgOeuf=ImageTk.PhotoImage(Image.open("OeufBacon.jpg"))
imgPain=ImageTk.PhotoImage(Image.open("Pain.jpg"))
label=Label(fen,image=imgOeuf)

def bonjourfonction():
    global label
    label.pack()

imgbar=ImageTk.PhotoImage(file="bar.jpg")
can.create_image( 150, 0, image = imgbar,
                     anchor = "nw")


imgtable=ImageTk.PhotoImage(Image.open("table-removebg-preview.png"))
can.create_image(150,400,image=imgtable,anchor="nw")
mon_bouton = Button(fen, image = imgPain, bg = 'grey', command = bonjourfonction)
can.create_window(150,400,anchor=NW,window=mon_bouton)

fen.mainloop()