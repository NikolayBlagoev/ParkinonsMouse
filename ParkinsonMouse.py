from mouse import move
from random import randint
from time import sleep
from threading import Thread
import tkinter as tk
import tkinter.font
from sys import  exit

x = [False]


def buttonClick1():
    B.configure(bg="#db0209", text="STOP", command=buttonClick2)
    x[0] = True


def buttonClick2():
    B.configure(bg="#46f249", text="START", command=buttonClick1)
    x[0] = False


def jitter():
    strength = 1
    prev_x = 0
    prev_y = 0
    direction = 1
    count = 0
    while True:
        while x[0]:
            curr_x = direction * randint(10, 20)
            curr_y = - direction * randint(2, 8)
            move(curr_x * strength + prev_x, curr_y * strength + prev_y, absolute=False)
            direction = -1 * direction
            prev_x = -(curr_x * strength)
            prev_y = -(curr_y * strength)
            count += 1
            sleep(0.003)


def on_closing():
    root.destroy()
    x[0] = False
    exit()


tr = Thread(target=jitter)
if __name__ == '__main__':
    tr.start()
    root = tk.Tk()
    root.title("Parkinson's mouse")
    canvas = tk.Canvas(root, width=360, height=220)
    B = tk.Button(root, text="START", width=8, height=2, bg="#46f249", command=buttonClick1)
    B['font'] = tkinter.font.Font(size=50)
    canvas.place(y=0, x=0)
    B.place(y=10, x=20)
    canvas.pack()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
