from tkinter import *

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
toShow = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 


def ResetTimer():
    global timer
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global toShow
    toShow = ""
    checkmark_symbol.config(text=toShow)
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #


def StartTimer():

    global reps
    global toShow
    if reps == 8:
        timer_label.config(text="BIG BREAK", fg=RED)
        reps = 0
        toShow = ""
        counter = LONG_BREAK_MIN * 60
        StartCountDown(counter-1)
    elif reps % 2 == 1:
        counter = WORK_MIN * 60
        timer_label.config(text="WORK", fg=GREEN)
        toShow += "✔"
        checkmark_symbol.config(text=toShow)
        StartCountDown(counter-1)
    elif reps % 2 == 0:
        counter = SHORT_BREAK_MIN * 60
        timer_label.config(text="BREAK", fg=PINK)
        StartCountDown(counter-1)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def StartCountDown(count):
    if 0 <= int(count/60) <= 9:
        toDisplay = "0" + str(int(count/60)) + ":"
    else:
        toDisplay = str(int(count / 60)) + ":"

    if 0 <= count % 60 <= 9:
        toDisplay += "0" + str(count % 60)
    else:
        toDisplay += str(count % 60)

    canvas.itemconfig(timer_text, text=toDisplay)
    if count > 0:
        global timer
        timer = window.after(1000, StartCountDown, count - 1)
    else:
        StartTimer()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"), highlightthickness=0)
timer_label.grid(column=1, row=0)


start_btn = Button(text="Start", highlightthickness=0, command=StartTimer)
start_btn.grid(column=0, row=2)

checkmark_symbol = Label(text="", fg=GREEN, bg=YELLOW)
checkmark_symbol.grid(column=1, row=3)


reset_btn = Button(text="Reset", highlightthickness=0, command=ResetTimer)
reset_btn.grid(column=2, row=2)

window.mainloop()




