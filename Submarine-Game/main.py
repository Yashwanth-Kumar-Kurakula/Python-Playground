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

SUBMARINE_SPEED = 10

def move_submarine(event):
    if event.keysym == 'Up':
        canvas.move(submarine_id, 0, -SUBMARINE_SPEED)
        canvas.move(submarine2_id, 0, -SUBMARINE_SPEED)
    if event.keysym == 'Down':
        canvas.move(submarine_id, 0, SUBMARINE_SPEED)
        canvas.move(submarine2_id, 0, SUBMARINE_SPEED)
    if event.keysym == 'Left':
        canvas.move(submarine_id, -SUBMARINE_SPEED, 0)
        canvas.move(submarine2_id, -SUBMARINE_SPEED, 0)
    if event.keysym == 'Right':
        canvas.move(submarine_id, SUBMARINE_SPEED, 0)
        canvas.move(submarine2_id, SUBMARINE_SPEED, 0)

canvas.bind_all('<Key>', move_submarine)
    