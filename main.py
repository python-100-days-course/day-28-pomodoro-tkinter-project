# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 28 - Intermediate - Tkinter, Canvas Widget, Dynamic Typing and Pomodoro GUI App
# Start day: 2024-11-26

# Dynamic Typing: changing variable type by changing the type of variable it holds, Python allows this, many other languages don't

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
reps = 0 # variable for number of repetitions
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer) # to stop the timer
    canvas.itemconfig(timer_text, text="00:00") # reset the timer
    timer_label.config(text="Timer", fg=GREEN) # change the title back to "Timer"
    checks_label.config(text="") # remove check marks
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps # note: typically it's not a good idea to make a variable global
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # # Shorten the time interval for testing
    # work_sec = 5 # WORK_MIN * 60
    # short_break_sec = 2 # SHORT_BREAK_MIN * 60
    # long_break_sec = 3 # LONG_BREAK_MIN * 60

    # print(reps) # testing

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
        # print("long_break_sec") # testing
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
        # print("short_break_sec") # testing
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        # print("work_sec") # testing

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)

    # make the seconds look better when 0 and less than 10:
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    count_text = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=count_text) # Note: label text can be changed with .config, however canvas is done this way
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1) # after 1000ms = 1sec trigger count_down function and pass to it "count - 1"
    else: # if count == 0 start timer
        start_timer()
        if reps % 2 == 0:
            number_of_checks = int(reps / 2)
            checks_text = "✔" * number_of_checks
            checks_label.config(text=checks_text)
        # # Official solution for check marks logic:
        # marks = ""
        # work_sessions = math.floor(reps / 2)
        # for _ in range(work_sessions):
        #     marks += "✔"
        # checks_label.config(text=marks)


# # Note - something like this wouldn't work, because it can't inject itself into window.mainloop() which is also a loop:
# import time
# count = 5
# while True:
#     time.sleep(1)
#     count -= 1

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# # In this example window.after() is used to call a function after 1000ms = 1sec, and a-c are passed to this function:
# def say_something(a, b, c):
#     print(a)
#     print(b)
#     print(c)
# window.after(1000, say_something, "What up!", 1, 2)

# <-----> GRID - 1st ROW <----->
# Timer text
timer_label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN) # create label component
timer_label.grid(column=1, row=0) # used to place the component into the window

# <-----> GRID - 2nd ROW <----->
# Background image and timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # "highlightthickness=0" removes the border around the canvas
tomoto_img = PhotoImage(file="tomato.png") # load the image
canvas.create_image(100, 112, image=tomoto_img) # x and y position, and specifying the image object
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# <-----> GRID - 3rd ROW <----->
# Button - start
button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=2)
# Button - reset
button_reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
button_reset.grid(column=2, row=2)

# <-----> GRID - 4th ROW <----->
# Check marks
checks_label = Label(font=(FONT_NAME, 24, "bold"), bg=YELLOW, fg=GREEN) # create label component
checks_label.grid(column=1, row=3) # text="✔"

window.mainloop()