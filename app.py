from cgitb import text
from tkinter import *
from req import *

frame = Tk()
frame.title("Synapse")

#set window size (widthxheight)
frame.geometry("1480x920")

#set window colour
frame.config(bg='#B0B0E0')

# Function for getting Input
# from textbox and printing it 
# at label widget

fr1 = Frame(frame, borderwidth = 5, bg = "grey", relief = SUNKEN, pady = 20)
fr1.pack(fill = "x")
fr2 = Frame(fr1, borderwidth = 5, bg = "grey", pady = 20)
fr2.pack(anchor = "center")
responseframe = Frame(frame, bg = "#B0B0E0")
responseframe.pack()
buttonsframe = Frame(responseframe, padx = 30, pady = 30, bg = "lightcyan")
buttonsframe.pack(fill = "x")

# menu bar
menu1 = Menu(frame)
menu1.add_command(label = " File ")
menu1.add_command(label = " Save")
frame.config(menu = menu1)


#function for output of status_code and text of get request
def Output():
    inp = inputtxt.get(1.0, "end-1c")
    url = inp
    a,b = get(url)
    lbl.config(text = b)

options = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
]

# datatype of menu text
clicked = StringVar()
# initial menu text
clicked.set( "GET" )
# Create Dropdown menu
drop = OptionMenu( fr2 , clicked , *options)
drop.grid(row = 0, column = 0, )
# InputBox(TextBox) Creation
inputtxt = Text(fr2, height = 1, width = 36, pady = 20, padx = 20) 
inputtxt.grid(row = 0, column = 1, padx = 45)
# Button Creation
sendButton = Button(fr2, text = "Send", command = Output, padx=12, pady=10, bg="#DCDC14")
sendButton.grid(row = 0, column = 2)

button1 = Button(buttonsframe, text = "Pretty", padx = 18, pady = 15, bg = "lightblue")
button1.grid(row = 0, column = 1, padx = 20)
button2 = Button(buttonsframe, text = "Raw", padx = 18, pady = 15, bg = "lightblue")
button2.grid(row = 0, column = 2, padx = 20)
button3 = Button(buttonsframe, text = "Preview", padx = 18, pady = 15, bg = "lightblue")
button3.grid(row = 0, column = 3, padx = 20)
button4 = Button(buttonsframe, text = "Visualize", padx = 18, pady = 15, bg = "lightblue")
button4.grid(row = 0, column = 4, padx = 20)

# Label Creation
lbl = Label(responseframe, text = "Click Send to get a response", height=1150, width=1300, padx = 50, pady=50, bg = "lightcyan", fg = "black", font = "Helvetica 13")
lbl.pack(side = RIGHT)

frame.mainloop()