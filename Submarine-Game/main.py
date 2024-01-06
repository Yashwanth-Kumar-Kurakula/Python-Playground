from tkinter import *
from random import randint
from time import sleep, time
from math import sqrt

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
bubble_radius = list()
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
    bubble_radius.append(r)
    bubble_speed.append(randint(1, MAX_BUBBLE_SPEED))

def move_bubbles():
    for i in range(len(bubble_id)):
        canvas.move(bubble_id[i], -bubble_speed[i], 0)

def find_coords(num_id):
    pos = canvas.coords(num_id)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y

def delete_bubble(i):
    del bubble_radius[i]
    del bubble_speed[i]
    canvas.delete(bubble_id[i])
    del bubble_id[i]

def clear_bubbles():
    for i in range(len(bubble_id) - 1, -1, -1):
        x, y = find_coords(bubble_id[i])
        if x < -GAP:
            delete_bubble(i)

def distance(id1, id2):
    x1, y1 = find_coords(id1)
    x2, y2 = find_coords(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def collision():
    points = 0
    for bubble in range(len(bubble_id) - 1, -1, -1):
        if distance(submarine2_id, bubble_id[bubble]) < (SUBMARINE_RADIUS + bubble_radius[bubble]):
            points += (bubble_radius[bubble] + bubble_speed[bubble])
            delete_bubble(bubble)
    return points

canvas.create_text(100, 30, text='REMAINING TIME', fill='white')
canvas.create_text(200, 30, text='SCORE', fill='white')

time_text = canvas.create_text(100, 50, fill='white')
score_text = canvas.create_text(200, 50, fill='white')

def print_score(score):
    canvas.itemconfig(score_text, text=str(score))

def print_time(remaining_time):
    canvas.itemconfig(time_text, text=str(remaining_time))

RANDOM_BUBBLE = 10
TIME_LIMIT = 30
BONUS_SCORE = 1000

score = 0
bonus = 0
end = time() + TIME_LIMIT

# main loop
while time() < end:
    if randint(1, RANDOM_BUBBLE) == 1:
        create_bubble()
    move_bubbles()
    clear_bubbles()
    score += collision()
    print(score)
    if(int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        end += TIME_LIMIT
    print_score(score)
    print_time(int(end - time()))
    window.update()
    sleep(0.01)
