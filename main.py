from tkinter import *

counting = True
timer = None
time_for_write = 15


def start():
    global time_for_write
    time_for_write = 15
    countdown()


def callback(event):
    # char = '{k!r}'.format(k=event.char)
    global time_for_write
    time_for_write = 15


def countdown():
    global time_for_write
    print(time_for_write)

    if time_for_write > 12:
        textbox.config(fg="#ff0000")

    if 8 < time_for_write <= 12:
        textbox.config(fg="#ff6666")

    if 4 < time_for_write <= 8:
        textbox.config(fg="#ff9999")

    if 0 < time_for_write <= 4:
        textbox.config(fg="#ffcccc")

    if time_for_write > 0:
        global timer
        time_for_write -= 1
        timer = window.after(1000, countdown)
    else:
        textbox.delete("1.0", "end")
        # clean all entries in text area
        start_button.config(text="Restart")


window = Tk()
window.config(padx=50, pady=30)
canvas = Canvas(width=300, height=30, highlightthickness=0, bg='#999')
text_of_canvas = canvas.create_text(60, 15,
                                    text="You should write without pause if you pause for number of seconds text will disappear")
canvas.grid(row=0, column=0)

textbox = Text(window, bg="white", width=120, borderwidth=2, fg="#ff0000")
textbox.grid(row=1, column=0)
textbox.bind("<Key>", callback)

start_button = Button(text="Start", command=start, highlightthickness=0)
start_button.grid(column=0, row=2)
start_button.config(padx=5, pady=10)

# textbox.bind("<FocusIn>", temp_text)

window.mainloop()
