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
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(timer)
    timerLabel.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkMarkLabel.config(text="")
    global reps
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    if reps == 1:
        reps += 1
        timerLabel.config(text="Work", fg=GREEN)
        countdown(25*60)
    elif reps == 2:
        reps += 1
        timerLabel.config(text="Break", fg=PINK)
        countdown(5*60)
    elif reps == 3:
        reps += 1
        timerLabel.config(text="Work", fg=GREEN)
        countdown(25 * 60)
    elif reps == 4:
        reps += 1
        timerLabel.config(text="Break", fg=PINK)
        countdown(5*60)
    elif reps == 5:
        reps += 1
        timerLabel.config(text="Work", fg=GREEN)
        countdown(25*60)
    elif reps == 6:
        reps += 1
        timerLabel.config(text="Break", fg=PINK)
        countdown(5*60)
    elif reps == 7:
        reps += 1
        timerLabel.config(text="Work", fg=GREEN)
        countdown(25*60)
    elif reps == 8:
        reps += 1
        timerLabel.config(text="Long Break", fg=RED)
        countdown(20*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        if reps == 2 or reps == 4 or reps == 6 or reps == 8:
            checkMarkLabel.config(text="✔")
        if reps == 1 or reps == 3 or reps == 5 or reps == 7:
            checkMarkLabel.config(text="")
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100,bg="#f7f5dd")

canvas = Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Courier", 35, "bold"))
#countdown(10)
canvas.grid(column=1, row=1)

timerLabel = Label(text="Timer", fg=GREEN, font=("Courier", 30, "bold"), bg=YELLOW)
timerLabel.grid(column=1, row=0)

checkMarkLabel = Label(fg=GREEN, bg=YELLOW, font=("Courier", 15, "bold"))
checkMarkLabel.grid(column=1, row=3)

startButton = Button(text="Start", highlightthickness=0, command=start_timer)
startButton.grid(column=0, row=2)

resetButton = Button(text="Reset", highlightthickness=0, command=reset)
resetButton.grid(column=2, row=2)

window.mainloop()
