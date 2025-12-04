from tkinter import *


root = Tk()
root.geometry("800x500")
root.title("Liiklusmärk")
canva = Canvas(width=800, height= 500)
canva.pack()

Triangle = canva.create_polygon(400, 50, 50, 495, 750, 495, fill="", outline="red", width=20)

colors = ["red", "yellow", "green"]
i = 0
while i < 3:
    ringid = canva.create_oval(350, 240+i*110, 450, 140+i*110, fill=colors[i])
    i +=1


root.mainloop()
