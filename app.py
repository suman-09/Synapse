from cgitb import text
from tkinter import *
from tkinter import ttk
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
responseframe = Frame(frame, bg = "lightcyan")
responseframe.pack()
buttonsframe = Frame(responseframe, padx = 30, pady = 30, bg = "lightcyan")
buttonsframe.pack(fill = "x")
bframe = Frame(fr1, padx = 30, pady = 30, bg = "grey")
bframe.pack(anchor  ="center")

# menu bar
menu1 = Menu(frame)
menu1.add_command(label = " File ")
menu1.add_command(label = " Save")
frame.config(menu = menu1)

#function 
#to get which requested setted at request

def got():
    slktd = clicked.get()
    law = slktd.lower()
    return(law)

def requested():
    url = inputtxt.get(1.0, "end-1c")
    param = tab1.get(1.0, "end-1c")
    auth = tab2.get(1.0, "end-1c")
    head = tab3.get(1.0, "end-1c")
    json = tab4.get(1.0, "end-1c")  
    t = got()
    statcode, txt, hed = request(t , url, param, auth, head, json)
    lbl1.config(text = txt)
    lbl3.config(text = hed)

options = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
]

def appear1():
    # InputBox for params (TextBox) Creation
    inputtxt1 = Text(fr2, height = 3, width = 90, pady = 20, padx = 20, bg = "red") 
    inputtxt1.grid(row = 2, column = 1, padx = 45, pady = 30)
def appear2():
    # InputBox for params (TextBox) Creation
    inputtxt2 = Text(fr2, height = 3, width = 90, pady = 20, padx = 20, bg = "pink") 
    inputtxt2.grid(row = 2, column = 1, padx = 45, pady = 30)
def appear3():
    # InputBox for params (TextBox) Creation
    inputtxt3 = Text(fr2, height = 3, width = 90, pady = 20, padx = 20, bg = "blue") 
    inputtxt3.grid(row = 2, column = 1, padx = 45, pady = 30)
def appear4():
    # InputBox for params (TextBox) Creation
    inputtxt4 = Text(fr2, height = 3, width = 90, pady = 20, padx = 20, bg = "green") 
    inputtxt4.grid(row = 2, column = 1, padx = 45, pady = 30)
# datatype of menu text
clicked = StringVar()
# initial menu text
clicked.set( "GET" )
# Create Dropdown menu
drop = OptionMenu( fr2 , clicked , *options, command=got)
drop.grid(row = 0, column = 0, )
# url box
inputtxt = Text(fr2, height = 1, width = 76, pady = 20, padx = 20) 
inputtxt.grid(row = 0, column = 1, padx = 45)
# saving url
# url = inputtxt.get(1.0, "end-1c")


# tabs widget
tabControl = ttk.Notebook(fr1, height = 100, width = 50)
tab1 = Text(tabControl)
tab2 = Text(tabControl)
tab3 = Text(tabControl)
tab4 = Text(tabControl)
tabControl.add(tab1, text = 'Params')
tabControl.add(tab2, text = 'Authorization')
tabControl.add(tab3, text = 'Headers')
tabControl.add(tab4, text = 'JSON')
tabControl.pack(fill = "both", padx = 400)

# Button Creation
sendButton = Button(fr2, text = "Send", command = requested, padx=18, pady=15, bg="#DCDC14")
sendButton.grid(row = 0, column = 2)

# tabs widget
tabControl = ttk.Notebook(responseframe, height = 700, width = 50)
tab_1 = Label(tabControl, text="response")
tab_2 = Label(tabControl, text="hjgjj")
tab_3 = Label(tabControl, text="bjghjhjh")
tabControl.add(tab_1, text = 'Raw')
tabControl.add(tab_2, text = 'Preview')
tabControl.add(tab_3, text = 'Headers')
tabControl.pack(fill = "both")

# Label Creation
lbl1 = Label(tab_1, text = "Click Send to get a response", height=1150, width=100, padx = 50, pady=50, bg = "pink", fg = "black", font = "Helvetica 13", justify = "left", wraplength = 1500)
lbl1.pack()
lbl2 = Label(tab_2, text = "Click Send to get a response", height=1150, width=1300, padx = 50, pady=50, bg = "pink", fg = "black", font = "Helvetica 13")
lbl2.pack()
lbl3 = Label(tab_3, text = "Click Send to get a response", height=1150, width=1300, padx = 50, pady=50, bg = "pink", fg = "black", font = "Helvetica 13")
lbl3.pack()

frame.mainloop()