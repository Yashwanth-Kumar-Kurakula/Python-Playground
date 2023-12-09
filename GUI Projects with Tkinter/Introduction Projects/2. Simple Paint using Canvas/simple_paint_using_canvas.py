import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, bg="white", width=800, height=800)
canvas.pack()

def draw_on_canvas(event):
    """
    Draw an oval on the canvas at the specified event coordinates.
    
    Parameters:
        - event (tk.Event): Mouse event containing information about the cursor position.
    """
    x = event.x
    y = event.y
    canvas.create_oval(x - brush_size / 2, y - brush_size, x + brush_size / 2, y + brush_size / 2, fill="black")

def brush_size_adjust(event):
    """
    Adjust the brush size based on the mouse wheel movement.
    
    Parameters:
        - event (tk.Event): Mouse wheel event containing information about the wheel movement.
    """
    global brush_size
    if event.delta > 0:
        brush_size += 2
    else:
        brush_size -= 2
    
    brush_size = max(0, min(brush_size, 50))

# Initial brush size
brush_size = 2

# Bind functions to canvas events
canvas.bind("<B1-Motion>", draw_on_canvas)
canvas.bind("<MouseWheel>", brush_size_adjust)

window.mainloop()
