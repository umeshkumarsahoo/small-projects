import tkinter as tk
import math

# Constants
PINK = "#e2979c"
RED = "#e73505"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# Functions
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label.config(text="Short Break", fg=GREEN)
    else:
        countdown(work_sec)
        label.config(text="Work", fg=GREEN)

def countdown(count):
    global timer
    mins, secs = divmod(count, 60)
    time_string = f"{mins:02d}:{secs:02d}"
    canvas.itemconfig(timer_text, text=time_string)
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = "✔" * (reps // 2)
        check_mark.config(text=marks)

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer",fg="black")
    check_mark.config(text="")
    reps = 0

# UI setup
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=PINK)

label = tk.Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=PINK, fg="black")
label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
img=tk.PhotoImage(file="cat.png")
canvas.create_image(100, 90,i=img)  # Create a circle instead of using an image
timer_text = canvas.create_text(100,40, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", command=start_timer,bd=0,highlightthickness=0,pady=2)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", command=reset_timer,bd=0,highlightthickness=0,pady=2)
reset_button.grid(column=2, row=2)

check_mark = tk.Label(bg=PINK, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()
