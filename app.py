from cgitb import text
from tkinter import *
import requests

gui = Tk()
gui.title("Synapse")

#set window size
gui.geometry("1080x720+200+200")

#set window colour
gui.config(bg='white')

# Function for getting Input
# from textbox and printing it 
# at label widget
  
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    url = inp
    r = requests.get(url)
    t = r.status_code
    u = r.text
    lbl.config(text = u)
    
  
# TextBox Creation
inputtxt = Text(gui, height = 8, width = 90) 
inputtxt.pack()
  
# Button Creation
printButton = Button(gui, text = "Send", command = printInput)
printButton.pack(anchor= NE)
  
# Label Creation
lbl = Label(gui, text = "", height=50, width=500)
lbl.pack()

gui.mainloop()