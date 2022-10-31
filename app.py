from cgitb import text
from tkinter import *
from req import *

frame = Tk()
frame.title("Synapse")

#set window size (widthxheight)
frame.geometry("1180x820")

#set window colour
frame.config(bg='#B0B0E0')

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


#function 
#to get which requested setted at request
def got(self):
    t = clicked.get()
    print(t)
    
#status_code and text of get request
def Outget():
    inp = inputtxt.get(1.0, "end-1c")
    a,b = get(inp)
    lbl.config(text = b)

# post
def Outpost():
    link = inputtxt.get(1.0, "end-1c")
    payload = inputtxt2.get(1.0, "end-1c")
    b = post(link)
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
drop = OptionMenu( fr2 , clicked , *options, command=got)
drop.grid(row = 0, column = 0, )
# InputBox(TextBox) Creation
inputtxt = Text(fr2, height = 1, width = 76, pady = 20, padx = 20) 
inputtxt.grid(row = 0, column = 1, padx = 45)
# InputBox for params (TextBox) Creation
inputtxt2 = Text(fr2, height = 4, width = 106, pady = 20, padx = 20) 
inputtxt2.grid(row = 1, column = 1, padx = 45)
# Button Creation
sendButton = Button(fr2, text = "Send", command = Outget, padx=12, pady=10, bg="#DCDC14")
sendButton.grid(row = 0, column = 2)

button1 = Button(buttonsframe, text = "Raw", padx = 18, pady = 15, bg = "lightblue")
button1.grid(row = 0, column = 2, padx = 20)
button2 = Button(buttonsframe, text = "Preview", padx = 18, pady = 15, bg = "lightblue")
button2.grid(row = 0, column = 3, padx = 20)
button3 = Button(buttonsframe, text = "Headers", padx = 18, pady = 15, bg = "lightblue")
button3.grid(row = 0, column = 4, padx = 20)

# Label Creation
lbl = Label(responseframe, text = "Click Send to get a response", height=1150, width=1300, padx = 50, pady=50, bg = "lightcyan", fg = "black", font = "Helvetica 13")
lbl.pack(side = RIGHT)

frame.mainloop()