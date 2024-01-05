from tkinter import *

HEIGHT = 500
WIDTH = 800

window = Tk()
window.title('Submarine Game')

canvas = Canvas(window, height=HEIGHT, width=WIDTH, bg='darkblue')
canvas.pack()

submarine_id = canvas.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
submarine2_id = canvas.create_oval(0, 0, 30, 30, outline='red')

SUBMARINE_RADIUS = 15

X_CENTER = WIDTH / 2
Y_CENTER = HEIGHT / 2

canvas.move(submarine_id, X_CENTER, Y_CENTER)
canvas.move(submarine2_id, X_CENTER, Y_CENTER)
