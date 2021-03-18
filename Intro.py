from tkinter import *

root = Tk()
root.title("Into")

# Insert an explanatory field
label_1 = Label(root, text = """
This tool will help you to automatically fetch prices for all products in two Kelowna
Spirit Leaf stores.

Be aware, you have to follow all Canadian Cannabis laws and regulations to be able to buy/smoke/store
cannabis in Canada (please check the following link:""")

label_1.pack()

w = Text(root, height=1, width = 95)
w.insert(1.0, "https://www.canada.ca/en/health-canada/services/drugs-medication/cannabis/laws-regulations.html")
w.pack()

label_2 = Label(root, text = """
When using the tool, if you don't get any results, make sure to re-run the tool several times.
Sometimes a poor internet connection might be a problem. Also, check on the website if the
product you are looking for is actually available in that store. Not all products are always
available in every store.
""")

label_2.pack()

# A function which will trigger the main program continuation if yes == True
def yes():
    global yes
    yes = True

# Insert a submit button
button_submit = Button(root, text = "Agree", padx = 5, pady = 5, command = lambda: [root.destroy(), yes()])
button_submit.pack()

root.mainloop()