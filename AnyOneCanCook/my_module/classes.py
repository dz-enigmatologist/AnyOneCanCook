"""Classes used throughout project"""
from functions import find_the_match

class MyCookBook:
    
    # recipeRepo is a dictionary containing the recipe name as the key and list of ingredients for the recipe as value
    # It is a class variable
    recipeRepo = {
        "Mango Lassi": ["Mango", "Curd"],
        "Pasta": ["Pasta", "Pasta Sauce", "Butter"],
        "BBJ": ["Butter", "Jam", "Bread"],
        "Garlic Bread": ["Garlic", "Bread"]
    }

    # recipeDetails is a dictionary containing the recipe name as the key and detailed recipe as a string as value
    # It is a class variable
    recipeDetails = {
        "Mango Lassi": "1. Chop mangoes and blend with sugar \n2. Serve Chilled.\n",
        "Pasta": "1. Boil pasta in pasta sauce with butter \n2. Serve Hot.\n",
        "BBJ": "1. Spread butter and jam on bread \n2. Serve Anyhow.\n",
        "Garlic Bread": "1. Spread garlic on bread and toast \n2. Serve Hot.\n"
    }

    def __init__(self, win):

        # The following are instance variables needed for the various window widgets like checkbox, button, text label

        self.check1 = IntVar()
        self.check2 = IntVar()
        self.check3 = IntVar()
        self.check4 = IntVar()
        self.check5 = IntVar()
        self.check6 = IntVar()
        self.check7 = IntVar()
        self.check8 = IntVar()

        self.title = Label(win, text='Any One CAN Cook', bg="#f2d1ff", fg="black")

        self.ingredient1 = Checkbutton(win, text='Mango', variable=self.check1)
        self.ingredient2 = Checkbutton(win, text='Curd', variable=self.check2)
        self.ingredient3 = Checkbutton(win, text='Pasta', variable=self.check3)
        self.ingredient4 = Checkbutton(win, text='Pasta Sauce', variable=self.check4)
        self.ingredient5 = Checkbutton(win, text='Butter', variable=self.check5)
        self.ingredient6 = Checkbutton(win, text='Jam', variable=self.check6)
        self.ingredient7 = Checkbutton(win, text='Bread', variable=self.check7)
        self.ingredient8 = Checkbutton(win, text='Garlic', variable=self.check8)

        self.recipe = Label(win, text='Recipe', fg="black", bg="#fde3ff", height=30, width=40, justify=LEFT,
                            wraplength=270)

        self.find = Button(win, text='Find Me a Recipe', command=self.find)
        self.clear = Button(win, text='Clear Selections', command=self.clear)
        self.exit = Button(win, text='Exit', command=self.exit)

        # The following code places the widgets into the right x-y coordinates in the window
        self.title.place(x=140, y=15)
        self.ingredient1.place(x=100, y=50)
        self.ingredient2.place(x=230, y=50)
        self.ingredient3.place(x=100, y=70)
        self.ingredient4.place(x=230, y=70)
        self.ingredient5.place(x=100, y=90)
        self.ingredient6.place(x=230, y=90)
        self.ingredient7.place(x=100, y=110)
        self.ingredient8.place(x=230, y=110)
        self.find.place(x=70, y=150)
        self.clear.place(x=230, y=150)
        self.recipe.place(x=25, y=180)
        self.exit.place(x=200, y=685)

    ## Methods of the class MyCookBook

    def find(self):
        
        # Adding selected ingredients into a list called ingredients.
        
        ingredients = []
        if self.check1.get():
            ingredients.append(self.ingredient1["text"])
        if self.check2.get():
            ingredients.append(self.ingredient2["text"])
        if self.check3.get():
            ingredients.append(self.ingredient3["text"])
        if self.check4.get():
            ingredients.append(self.ingredient4["text"])
        if self.check5.get():
            ingredients.append(self.ingredient5["text"])
        if self.check6.get():
            ingredients.append(self.ingredient6["text"])
        if self.check7.get():
            ingredients.append(self.ingredient7["text"])
        if self.check8.get():
            ingredients.append(self.ingredient8["text"])

        # Calling function `find_the_match` to match the ingredients to the stored recipes
        
        self.recipe['text'] = find_the_match(MyCookBook.recipeRepo, ingredients, MyCookBook.recipeDetails)

    def clear(self):
        
        # Clears input values of checkboxes for next use
        
        self.ingredient1.deselect()
        self.ingredient2.deselect()
        self.ingredient3.deselect()
        self.ingredient4.deselect()
        self.ingredient5.deselect()
        self.ingredient6.deselect()
        self.ingredient7.deselect()
        self.ingredient8.deselect()

        self.recipe['text'] = ""

    def exit(self):
        
        # Enables exit button to stop running code
        
        window.destroy()
