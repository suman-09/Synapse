from cgitb import text
from tkinter import *
import requests

frame = Tk()
frame.title("Synapse")

#set window size
frame.geometry("1080x720+200+200")

#set window colour
frame.config(bg='white')

# Function for getting Input
# from textbox and printing it 
# at label widget

leftfr = Frame(frame, borderwidth = 5, bg = "white", relief = SUNKEN)
leftfr.pack(side = LEFT, fill = "y", pady = 50)

fr1 = Frame(frame, borderwidth = 5, bg = "grey", relief = SUNKEN, pady = 20)
fr1.pack(side = TOP, fill = "x")

fr2 = Frame(fr1, borderwidth = 4, bg = "black", relief = SUNKEN)
fr2.pack()

fr3 = Frame(fr1, borderwidth = 4, bg = "black", relief = SUNKEN)
fr3.pack(pady=14)

responseframe = Frame(frame, borderwidth =7, bg = "white", relief = SUNKEN)
responseframe.pack(side = RIGHT)

def Output():
    inp = inputtxt.get(1.0, "end-1c")
    url = inp
    r = requests.get(url)
    t = r.status_code
    u = r.text
    lbl.config(text = u)

def show():
    label.config( text = clicked.get() )

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
drop = OptionMenu( fr1 , clicked , *options )
drop.pack()
  
# InputBox(TextBox) Creation
inputtxt = Text(fr2, height = 3, width = 40) 
inputtxt.pack()
  
# Button Creation
sendButton = Button(fr3, text = "Send", command = Output, padx=12, pady=10, bg="#DCDC14")
sendButton.pack()
  
# Label Creation
lbl = Label(responseframe, text = "Click Send to get a response", height=50, width=93, padx = 50, pady=50, bg="#B0B0E0", fg = "white", font = "Helvetica 13")
lbl.pack(side = RIGHT)

words = Label(leftfr, text = " here it is", height = 15, width = 30)
words.pack()

frame.mainloop()