from tkinter import *
from random import randint
from time import sleep, time
from math import sqrt

class SubmarineGame:
    def __init__(self, master):
        self.master = master
        master.title('Submarine Game')

        self.HEIGHT = 500
        self.WIDTH = 800

        self.canvas = Canvas(master, height=self.HEIGHT, width=self.WIDTH, bg='darkblue')
        self.canvas.pack()

        self.SUBMARINE_RADIUS = 15
        self.SUBMARINE_SPEED = 10
        self.X_CENTER = self.WIDTH / 2
        self.Y_CENTER = self.HEIGHT / 2

        self.submarine_id = self.canvas.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
        self.submarine2_id = self.canvas.create_oval(0, 0, 30, 30, outline='red')

        self.canvas.move(self.submarine_id, self.X_CENTER, self.Y_CENTER)
        self.canvas.move(self.submarine2_id, self.X_CENTER, self.Y_CENTER)

        self.canvas.bind_all('<Key>', self.move_submarine)

        self.bubble_id = []
        self.bubble_radius = []
        self.bubble_speed = []

        self.MIN_BUBBLE_RADIUS = 10
        self.MAX_BUBBLE_RADIUS = 30
        self.MAX_BUBBLE_SPEED = 10
        self.GAP = 100

        self.TIME_LIMIT = 30
        self.RANDOM_BUBBLE = 10
        self.BONUS_SCORE = 1000

        self.score = 0
        self.bonus = 0
        self.end = time() + self.TIME_LIMIT

        self.canvas.create_text(100, 30, text='REMAINING TIME', fill='white')
        self.canvas.create_text(200, 30, text='SCORE', fill='white')

        self.time_text = self.canvas.create_text(100, 50, fill='white')
        self.score_text = self.canvas.create_text(200, 50, fill='white')

        self.game_loop()

    def move_submarine(self, event):
        if event.keysym == 'Up':
            self.canvas.move(self.submarine_id, 0, -self.SUBMARINE_SPEED)
            self.canvas.move(self.submarine2_id, 0, -self.SUBMARINE_SPEED)
        elif event.keysym == 'Down':
            self.canvas.move(self.submarine_id, 0, self.SUBMARINE_SPEED)
            self.canvas.move(self.submarine2_id, 0, self.SUBMARINE_SPEED)
        elif event.keysym == 'Left':
            self.canvas.move(self.submarine_id, -self.SUBMARINE_SPEED, 0)
            self.canvas.move(self.submarine2_id, -self.SUBMARINE_SPEED, 0)
        elif event.keysym == 'Right':
            self.canvas.move(self.submarine_id, self.SUBMARINE_SPEED, 0)
            self.canvas.move(self.submarine2_id, self.SUBMARINE_SPEED, 0)

    def create_bubble(self):
        x = self.WIDTH + self.GAP
        y = randint(0, self.HEIGHT)
        r = randint(self.MIN_BUBBLE_RADIUS, self.MAX_BUBBLE_RADIUS)
        id1 = self.canvas.create_oval(x - r, y - r, x + r, y + r, outline='white')
        self.bubble_id.append(id1)
        self.bubble_radius.append(r)
        self.bubble_speed.append(randint(1, self.MAX_BUBBLE_SPEED))

    def move_bubbles(self):
        for i in range(len(self.bubble_id)):
            self.canvas.move(self.bubble_id[i], -self.bubble_speed[i], 0)

    def find_coords(self, num_id):
        pos = self.canvas.coords(num_id)
        x = (pos[0] + pos[2]) / 2
        y = (pos[1] + pos[3]) / 2
        return x, y

    def delete_bubble(self, i):
        del self.bubble_radius[i]
        del self.bubble_speed[i]
        self.canvas.delete(self.bubble_id[i])
        del self.bubble_id[i]

    def clear_bubbles(self):
        for i in range(len(self.bubble_id) - 1, -1, -1):
            x, y = self.find_coords(self.bubble_id[i])
            if x < -self.GAP:
                self.delete_bubble(i)

    def distance(self, id1, id2):
        x1, y1 = self.find_coords(id1)
        x2, y2 = self.find_coords(id2)
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def collision(self):
        points = 0
        for bubble in range(len(self.bubble_id) - 1, -1, -1):
            if self.distance(self.submarine2_id, self.bubble_id[bubble]) < (
                    self.SUBMARINE_RADIUS + self.bubble_radius[bubble]):
                points += (self.bubble_radius[bubble] + self.bubble_speed[bubble])
                self.delete_bubble(bubble)
        return points

    def print_score(self, score):
        self.canvas.itemconfig(self.score_text, text=str(score))

    def print_time(self, remaining_time):
        self.canvas.itemconfig(self.time_text, text=str(remaining_time))

    def game_loop(self):
        while time() < self.end:
            if randint(1, self.RANDOM_BUBBLE) == 1:
                self.create_bubble()
            self.move_bubbles()
            self.clear_bubbles()
            self.score += self.collision()
            print(self.score)
            if int(self.score / self.BONUS_SCORE) > self.bonus:
                self.bonus += 1
                self.end += self.TIME_LIMIT
            self.print_score(self.score)
            self.print_time(int(self.end - time()))
            self.master.update()
            sleep(0.01)

if __name__ == "__main__":
    root = Tk()
    game = SubmarineGame(root)
    root.mainloop()
