"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../my_module')

# Imports
from classes import MyCookBook
from tkinter import *
###
###

# PYTHON SCRIPT HERE
window = Tk()
mywin = MyCookBook(window)
window.title('AnyOneCanCook')
window.resizable(width=False, height=False)
window.geometry("420x720")
window.mainloop()
