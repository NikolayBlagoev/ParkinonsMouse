from mouse import move
from random import randint
from time import sleep
from threading import Thread
import tkinter as tk
import tkinter.font
from sys import exit

state = [False, 1]


def buttonClick1():
    B.configure(bg="#db0209", text="STOP", command=buttonClick2)
    state[0] = True


def buttonClick2():
    B.configure(bg="#46f249", text="START", command=buttonClick1)
    state[0] = False


def jitter():
    prev_x = 0
    prev_y = 0
    direction_x = 1
    direction_y = 1
    count = 0
    while True:
        while state[0]:
            curr_x = direction_x * randint(10 * state[1], 20 * state[1])
            if count == 0:
                direction_y = 1 if randint(0, 1) % 2 == 0 else -1
            curr_y = - direction_y * randint(2 * state[1], 8 * state[1])

            move(curr_x + prev_x, curr_y + prev_y, absolute=False)
            direction_x = - direction_x
            prev_x = - curr_x
            prev_y = - curr_y
            count = (count + 1) % 2
            sleep(0.01)


def on_closing():
    root.destroy()
    state[0] = False
    exit()


def update_slider(val):
    state[1] = int(val)


tr = Thread(target=jitter)
if __name__ == '__main__':
    tr.start()
    root = tk.Tk()
    root.title("Parkinson's mouse")
    canvas = tk.Canvas(root, width=360, height=260)
    B = tk.Button(root, text="START", width=8, height=2, bg="#46f249", command=buttonClick1)
    B['font'] = tkinter.font.Font(size=50)
    canvas.place(y=0, x=0)
    B.place(y=60, x=20)
    w = tk.Scale(root, from_ =1, to=10, orient=tk.HORIZONTAL, command=update_slider, length = 300)
    w.set(1)
    w.place(y=10, x=20)
    w.pack()
    canvas.pack()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
