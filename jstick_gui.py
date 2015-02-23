#!/usr/bin/python
from jstick import Joystick
import tkinter as tk
import numpy as np


class StickCanvas(tk.Canvas):
    def update(self, coords):
        coords = np.copy(coords)
        norm = np.linalg.norm(coords)
        if norm > 1:
            coords = coords / norm
        coords *= 50
        self.delete("all")
        self.create_oval(0, 0, 100, 100)
        self.create_oval(coords[0] - 5 + 50, coords[1] - 5 + 50,
                         coords[0] + 5 + 50, coords[1] + 5 + 50,
                         fill='black')


class Application(tk.Frame):

    def createWidgets(self):
        self.lstick_canvas = StickCanvas(self, width=100, height=100)
        self.lstick_canvas.grid(row=0, column=0, columnspan=2, rowspan=2)
        self.rstick_canvas = StickCanvas(self, width=100, height=100)
        self.rstick_canvas.grid(row=0, column=2, columnspan=2, rowspan=2)

    def update(self):
        self.lstick_canvas.update(self.joystick.stick1.coords)
        self.rstick_canvas.update(self.joystick.stick2.coords)
        self.after(10, self.update)

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.joystick = Joystick()
        self.after(10, self.update)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
