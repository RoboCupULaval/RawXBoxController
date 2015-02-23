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
        width = self.winfo_width() * 0.95
        height = self.winfo_height() * 0.95
        self.create_oval(0, 0, width, height)
        self.create_oval(coords[0] - 5 + width/2,
                         coords[1] - 5 + width/2,
                         coords[0] + 5 + height/2,
                         coords[1] + 5 + height/2,
                         fill='black')


class ButtonCanvas(tk.Canvas):
    def update(self, value):
        if value == 1:
            color = 'red'
        else:
            color = 'black'

        self.delete("all")
        width = self.winfo_width() * 0.95
        height = self.winfo_height() * 0.95
        self.create_oval(0, 0, width, height, fill=color)


class Application(tk.Frame):

    def createWidgets(self):
        self.lstick_canvas = StickCanvas(self, width=100, height=100)
        self.lstick_canvas.grid(row=0, column=0, columnspan=2, rowspan=2)
        self.rstick_canvas = StickCanvas(self, width=100, height=100)
        self.rstick_canvas.grid(row=0, column=2, columnspan=2, rowspan=2)
        self.xbutton_canvas = ButtonCanvas(self, width=50, height=50)
        self.xbutton_canvas.grid(row=0, column=4, columnspan=1, rowspan=1)
        self.abutton_canvas = ButtonCanvas(self, width=50, height=50)
        self.abutton_canvas.grid(row=1, column=4, columnspan=1, rowspan=1)
        self.ybutton_canvas = ButtonCanvas(self, width=50, height=50)
        self.ybutton_canvas.grid(row=0, column=5, columnspan=1, rowspan=1)
        self.bbutton_canvas = ButtonCanvas(self, width=50, height=50)
        self.bbutton_canvas.grid(row=1, column=5, columnspan=1, rowspan=1)

    def update(self):
        self.lstick_canvas.update(self.joystick.buttons['stick1'].coords)
        self.rstick_canvas.update(self.joystick.buttons['stick2'].coords)
        self.xbutton_canvas.update(self.joystick.buttons['x'].value)
        self.abutton_canvas.update(self.joystick.buttons['a'].value)
        self.ybutton_canvas.update(self.joystick.buttons['y'].value)
        self.bbutton_canvas.update(self.joystick.buttons['b'].value)
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