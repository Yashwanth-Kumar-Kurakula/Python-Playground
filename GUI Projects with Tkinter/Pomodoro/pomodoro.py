from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    """Reset the timer to its initial state."""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 40, "bold"))
    checkmark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """Start the Pomodoro timer."""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        timer_label.config(text="Break", background=YELLOW, foreground=RED, font=(FONT_NAME, 40, "bold"))
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", background=YELLOW, foreground=RED, font=(FONT_NAME, 40, "bold"))
        count_down(short_break_sec)
    else:
        timer_label.config(text="Timer", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 40, "bold"))
        count_down(work_sec)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """Countdown mechanism for the timer."""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=100, bg=YELLOW)

timer_label = Label(window, text="Timer", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

start = Button(window, text="Start", command=start_timer)
start.grid(row=2, column=0)

reset = Button(window, text="Reset", command=reset_timer)
reset.grid(row=2, column=2)

checkmark = Label(window, text="", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 22, "bold"))
checkmark.grid(row=3, column=1)

window.mainloop()
