from tkinter import *

root = Tk()
root.geometry("800x500")
root.title("maja")
canva = Canvas(width=800, height= 500)
canva.pack()

colors = ["white", "black", "white", "black", "white", "black", "white", "black"]
colors1 = ["black", "white", "black", "white", "black", "white", "black", "white"]
colors2 = ["white", "black", "white", "black", "white", "black", "white", "black"]
colors3 = ["black", "white", "black", "white", "black", "white", "black", "white"]
colors4 = ["white", "black", "white", "black", "white", "black", "white", "black"]
colors5 = ["black", "white", "black", "white", "black", "white", "black", "white"]
colors6 = ["white", "black", "white", "black", "white", "black", "white", "black"]
colors7 = ["black", "white", "black", "white", "black", "white", "black", "white"]



i = 0
while i < 8:
    male_laud = canva.create_rectangle(140+i*60, 10, 200+i*60, 70, fill=colors[i])
    male_laud = canva.create_rectangle(140+i*60, 70, 200+i*60, 130, fill=colors1[i])
    male_laud = canva.create_rectangle(140+i*60, 130, 200+i*60, 190, fill=colors2[i])
    male_laud = canva.create_rectangle(140+i*60, 190, 200+i*60, 250, fill=colors3[i])
    male_laud = canva.create_rectangle(140+i*60, 250, 200+i*60, 330, fill=colors4[i])
    male_laud = canva.create_rectangle(140+i*60, 310, 200+i*60, 390, fill=colors5[i])
    male_laud = canva.create_rectangle(140+i*60, 370, 200+i*60, 450, fill=colors6[i])
    male_laud = canva.create_rectangle(140+i*60, 430, 200+i*60, 490, fill=colors7[i])
    i += 1

root.mainloop()
