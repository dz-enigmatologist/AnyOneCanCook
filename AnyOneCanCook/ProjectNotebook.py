#!/usr/bin/env python
# coding: utf-8

# # Project Description
Write a brief description of your project here. 

The project is about finding a recipe given the ingredients. The User will choose the ingredients that they have and the application will search through recipes and give them the best matched recipes for the given ingredients.

The project files are organized as shown:

|
|--scripts
|   |
|   |------scripts.py
|           |
|           |---creates object of type MyCookBook and creates a window
|
|---my_module
    |
    |----classes.py
    |     |
    |     |---class MyCookBook
    |          |
    |          |---find()
    |          |---clear()
    |          |---exit()
    |
    |----functions.py
    |      |
    |      |----find_the_match()
    |
    |----test_functions.py
           |
           |----test_find_the_match()

MyCookBook is the main class that sets up the GUI layout for the application
along with all the methods for event handling.

find_the_match is a generic function that searches best match between a list and 
a number of lists. 

The test_find_the_match test the application and can be called from pytest
Note that projects should be self-sufficient, so make sure to provide enough information and context here for someone to understand what you are doing in your project, and why. 
# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[1]:


from my_module.classes import MyCookBook
from tkinter import *


# In[5]:


# Do a bunch of things.

##### My code displays a window using tkinter which doesn't run on a webpage, downloading the code will display it.

#window = Tk()
#mywin = MyCookBook(window)
#window.withdraw()
#window.title('AnyOneCanCook')
#window.resizable(width=False, height=False)
#window.geometry("420x720")
#window.mainloop()


# In[3]:


# test it out
get_ipython().system('pytest')


# #### Extra Credit (*optional*)
# 
# Replace all of this text with a brief explanation (~3 sentences) of: 
# 1. Your Python Background
# 2. How your project went above and beyond the requirements of the project and/or how you challenged yourself to learn something new with the final project
# 
# #### Answers
# 1. I have learnt python throughout my life from my mom while working on different projects. I have also attended few workshops. This is my first time learning it in an academic setting.
# 2. - My project is a anyone can cook app. I had this idea when I used to see my mother struggle with what to make for dinner and lunch everyday. So I thought it would be cool to have an app that would tell her what to make if you give the ingredients.
# 2. - I have challenged myself by taking on a window creating project which is one of the first I have done using python. I have learnt to navigate through tkinter and understood how to use all its functions.

# In[ ]:




