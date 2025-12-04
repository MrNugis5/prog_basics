from tkinter import *

root = Tk()
root.geometry("800x500")
root.title("maja")
canva = Canvas(width=800, height= 500)
canva.pack()

maja = canva.create_rectangle(220, 260, 580, 499, fill="#E3C619")
katus = canva.create_polygon(400, 100, 220, 260, 580, 260, fill="#BD1809" )
i = 0
while i < 2:
    aken1 = canva.create_rectangle(245+i*40, 300, 275+i*40, 330, fill="#5E97D6")
    aken2 = canva.create_rectangle(245+i*40, 340, 275+i*40, 370, fill="#5E97D6")
    aken3 = canva.create_rectangle(470+i*40, 300, 500+i*40, 330, fill="#5E97D6")
    i +=1

aken5 = canva.create_rectangle(470, 340, 500, 370, fill="#5E97D6") #ei tööta, ei saa aru miks, kõik õige.
aken4 = canva.create_rectangle(470, 300, 500, 330, fill="#5E97D6") 
uks = canva.create_rectangle(380, 450, 410, 500, fill="black")
link = canva.create_oval(401, 475, 410, 485, fill="yellow")
korsten = canva.create_rectangle(535, 200, 568, 260, fill="black")
root.mainloop()
