import tkinter as tk

root = tk.Tk()
root.title("Preteky lopticiek")

canvas = tk.Canvas(width=400, height=600, bg="lightblue")
canvas.pack()

lopticky = []

def vytvor_lopticky():
    x = -10
    for i in range(10):
        x += 30
        lopticka = canvas.create_oval(x, 10, x+20, 30, fill="red")
        lopticky.append(lopticka)

def Start():
    for lopticka in lopticky:
        canvas.move(lopticka, 0, 10)
    
    canvas.after(50, Start)

vytvor_lopticky()
Start()
