from CalculadoraFrontEnd import Win
from CalculadoraFunctions import mdrd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg


WIDTH = 400
HEIGHT = 1200


root = Tk()
my_win = Win(root, WIDTH, HEIGHT)
my_win.input_frame()
my_win.results_frame()


my_win.mainloop()
