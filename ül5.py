from tkinter import *

def vicsekFractals(canvas, x, y, size, depth):
    if depth == 0:
        canvas.create_rectangle(x, y, x + size, y + size, fill="black", outline="")
    else:
        new_size = size // 3
        positions = [
            (0,0), (2, 0),
            (1, 1),
            (0, 2), (2, 2)
        ]
        for dx, dy in positions:
            vicsekFractals(canvas, x + dx * new_size, y + dy * new_size, new_size, depth - 1)

def mingi_asjad():
    windows = Tk()
    windows.geometry("400x400")
    windows.title("Vicseki fraktaal")

    canva = Canvas(windows, width=400, height=400, bg="white")
    canva.pack()

    current_depth = [2]

    def redraw():
        canva.delete("all")
        vicsekFractals(canva, 0, 0, 400, current_depth[0])

    def key_pressed(event):
        if event.char.isdigit():
            current_depth[0] = int(event.char)
            redraw()

    windows.bind("<Key>", key_pressed)
    redraw()
    windows.mainloop()

mingi_asjad()
