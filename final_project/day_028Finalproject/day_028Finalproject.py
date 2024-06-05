import tkinter as tk
import customtkinter as ctk

# ---------------------------- CONSTANTS ------------------------------- #
BLUE = "#37d3ff"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def time_reset():
    global reps
    reps = 9
    label_timer.config(text="Timer", fg=GREEN)
    label_tick.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps < 9:
        if reps in [1, 3, 5, 7]:
            label_timer.config(text="Work", fg=GREEN)
            marks = ""
            work_session = int(reps / 2)
            for _ in range(work_session):
                marks += "✔"
            label_tick.config(text=marks)
            count_down(WORK_MIN)
        elif reps == 8:
            label_timer.config(text="Break", fg=RED)
            count_down(LONG_BREAK_MIN)
        elif reps in [2, 4, 6]:
            label_timer.config(text="Break", fg=PINK)
            count_down(SHORT_BREAK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    second_before = ""
    min_before = ""

    mins = int(seconds // 60)
    secs = int(seconds % 60)

    global reps

    if reps < 9:
        if mins < 10:
            min_before = "0"
        elif mins == 0:
            min_before = "00"
        if secs < 10:
            second_before = "0"
        elif secs == 0:
            second_before = "00"
        if secs == 0 and mins == 0 and reps < 9:
            start_timer()
        if secs >= 0 and mins >= 0:
            canvas.itemconfig(timer_text, text=f"{min_before}{mins}:{second_before}{secs}")
            window.after(1000, count_down, seconds - 1)
    else:
        canvas.itemconfig(timer_text, text=f"00:00")
        reps = 0


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.geometry("400x400")
window.title("Pomodoro")
window.config(padx=30, pady=30, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 140, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=2)

label_timer = tk.Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
label_timer.grid(column=1, row=0)

label_tick = tk.Label(text="", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
label_tick.grid(column=1, row=4)

# start_button = tk.Button(text=' Start ',
#                          fg="#206aa4",
#                          bg=YELLOW,
#                          highlightthickness=4,
#                          highlightbackground=YELLOW,
#                          command=start_timer)
start_button = ctk.CTkButton(window, text="Start", width=70, command=start_timer)
start_button.grid(column=0, row=3)

# reset_button = tk.Button(text=' Reset ',
#                          fg="#206aa4",
#                          bg=YELLOW,
#                          highlightthickness=4,
#                          highlightbackground=YELLOW,
#                          command=time_reset)
reset_button = ctk.CTkButton(window, text="Reset", width=70, command=time_reset)
reset_button.grid(column=2, row=3)

window.mainloop()
