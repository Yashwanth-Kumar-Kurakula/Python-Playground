import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, bg= "white", width=800, height=800)
canvas.pack()

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval(x - brush_size / 2, y - brush_size ,x + brush_size / 2 ,y + brush_size/2, fill="black")

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 2
    else:
        brush_size -= 2
    
    brush_size = max(0,min(brush_size, 50))

brush_size = 2
canvas.bind("<B1-Motion>", draw_on_canvas)
canvas.bind("<MouseWheel>", brush_size_adjust)

window.mainloop()
