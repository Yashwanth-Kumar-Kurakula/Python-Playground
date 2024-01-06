from tkinter import *
from random import randint

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

bubble_id = list()
radius_id = list()
bubble_speed = list()

MIN_BUBBLE_RADIUS = 10
MAX_BUBBLE_RADIUS = 30
MAX_BUBBLE_SPEED = 10
GAP = 100

def create_bubble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUBBLE_RADIUS, MAX_BUBBLE_RADIUS)
    id1 = canvas.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bubble_id.append(id1)
    radius_id(r)
    bubble_speed.append(randint(1, MAX_BUBBLE_SPEED))

def move_bubbles():
    for i in range(len(bubble_id)):
        canvas.move(bubble_id[i], -bubble_speed[i], 0)
