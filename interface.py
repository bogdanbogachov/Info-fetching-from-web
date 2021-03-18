from tkinter import *
from tkinter import filedialog
from tkinter import ttk

root = Tk()
root.geometry("400x200")
root.title("A great tool from a great guy :)")

# Insert an explanatory field
label_1 = Label(root, text = "Select a province:  ", width = 15, anchor = "e")
label_1.grid(row = 0, column = 0)

# Insert an explanatory field
label_2 = Label(root, text = "Date of Birth:  ", width = 15, anchor = "e")
label_2.grid(row = 1, column = 0)

# Insert an explanatory field
label_3 = Label(root, text = "Store:  ", width = 15, anchor = "e")
label_3.grid(row = 2, column = 0)

# Insert an explanatory field
label_4 = Label(root, text = "Product:  ", width = 15, anchor = "e")
label_4.grid(row = 3, column = 0)

# Insert an explanatory field
label_5 = Label(root, text = "Results file path:  ", width = 15, anchor = "e")
label_5.grid(row = 4, column = 0)

# Region selection
province = StringVar(root)
province.set("AB") # default value
province_choose = ttk.Combobox(
root, textvariable = province, width = 10,
values=["AB", "BC", "MB", "NB", "NL", "NS", "ON", "PE", "QC", "SK", "NT", "NU", "YT"]
)
province_choose.grid(row = 0, column = 1, sticky = "W")

def province_f():
    global province_final
    province_final = province.get()

# DOB
day = StringVar(root)
day.set("Day") # default value
day_choose = ttk.Combobox(
root, textvariable = day, width = 10,
values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
"11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
"21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
)
day_choose.grid(row = 1, column = 1, sticky = "W")

def day_f():
    global day_final
    day_final = day.get()

month = StringVar(root)
month.set("Month") # default value
month_choose = ttk.Combobox(
root, textvariable = month, width = 10,
values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
)
month_choose.grid(row = 1, column = 2, sticky = "W")

def month_f():
    global month_final
    month_final = month.get()

year = StringVar(root)
year.set("Year") # default value
year_choose = ttk.Combobox(
root, textvariable = year, width = 10,
values=list(range(1900, 2021))
)
year_choose.grid(row = 1, column = 3, sticky = "W")

def year_f():
    global year_final
    year_final = year.get()

# Store selection
store = StringVar(root)
store.set("Kelowna, British Columbia – Cannabis Store") # default value
store_choose = ttk.Combobox(
root, textvariable = store, width = 38,
values=["Kelowna, British Columbia – Cannabis Store", "West Kelowna – Cannabis Store"]
)
store_choose.grid(row = 2, column = 1, columnspan = 3, sticky = "W")

def store_f():
    global store_final
    store_final = store.get()

# Product selection
product = StringVar(root)
product.set("Flower") # default value
product_choose = ttk.Combobox(
root, textvariable = product, width = 38,
values=["Flower", "Rolls", "Vaporizers", "Concentrates", "Edibles", "Tinctures", "Topicals", "Seeds", "Accessories"]
)
product_choose.grid(row = 3, column = 1, columnspan = 3, sticky = "W")

def product_f():
    global product_final
    product_final = product.get()

# Select a folder for new files
def file_path_func():
    global path
    root.directory = filedialog.askdirectory(initialdir = "", title = "Select a folder")
    path = root.directory
    path_label = Label(root, text = "Path chosen", width = 15, anchor = "w")
    path_label.grid(row = 4, column = 2, columnspan = 2, sticky = "w")
    return

button_dots_new = Button(root, text = "...", padx = 20, pady = 5, command = file_path_func)
button_dots_new.grid(row = 4, column = 1, sticky = "W")

# A function which will trigger the main program continuation if yes == True
def yes():
    global yes
    yes = True

# Insert a submit button
button_submit = Button(
root, text = "Submit", padx = 5, pady = 5,
command = lambda: [root.destroy(), province_f(), day_f(), month_f(), year_f(), store_f(), product_f(), yes()])
button_submit.grid(row = 5, column = 1, sticky = "W")

root.mainloop()