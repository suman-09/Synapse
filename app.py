from tkinter import *
from tkinter import ttk
from tkhtmlview import HTMLLabel
from req import *
import os
from tkinter.simpledialog import askstring
from bs4 import BeautifulSoup as bs

frame = Tk()
frame.title("Synapse")

#set window size (widthxheight)
frame.geometry("1300x820")

#set window colour
frame.config(bg='#fff')

fr1 = Frame(frame, borderwidth = 0, bg = "white", relief = SUNKEN, pady = 20, highlightbackground= "#1338be", highlightthickness=3)
fr1.pack(fill = "x")
fr2 = Frame(fr1, borderwidth = 0, bg = "#fff", pady = 20,width=1000)
fr2.pack(anchor = "center")
responseframe = Frame(frame, bg = "white",highlightbackground= "#1338be", highlightthickness=3)
responseframe.pack()
buttonsframe = Frame(responseframe, padx = 30, pady = 30, bg = "white", highlightbackground= "#1338be", highlightthickness=3)
buttonsframe.pack(fill = "x")
bframe = Frame(fr1, padx = 30, pady = 30, bg = "white",highlightbackground= "#1338be", highlightthickness=3)
bframe.pack(anchor  ="center")
statusframe = Frame(buttonsframe, bg="#fff", padx=30, pady=30, )
statusframe.pack()
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
    soup = bs(txt, 'html.parser')
    prettyHTML = soup.prettify()
    lbl1.config(text = prettyHTML)
    lbl2.set_html(txt)
    lbl3.config(text = txt)
    return txt

def download():
    save = requested()
    filename = askstring('Save File', 'Enter filename') + '.html'
    myfile = open(filename, 'w')
    myfile.write(save)
    myfile.close()
    
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
drop.grid(row = 0, column = 0)
drop.config( bg="#1338be", fg="#fff")

# url box
inputtxt = Text(fr2, height = 1, width = 76, pady = 20, padx = 20 ) 
inputtxt.grid(row = 0, column = 1, padx = 45)


# tabs widget

tabControl = ttk.Notebook( fr1,  height = 100, width = 1700 )
tab1 = Text(tabControl,width=1000)
tab2 = Text(tabControl,width=1000)
tab3 = Text(tabControl,width=1000)
tab4 = Text(tabControl,width=1000)
tabControl.add(tab1, text = 'Params')
tabControl.add(tab2, text = 'Authorization')
tabControl.add(tab3, text = 'Headers')
tabControl.add(tab4, text = 'JSON')
tabControl.pack(fill = "both", padx = 400)


# Button Creation
sendButton = Button(fr2, text = "Send", command = requested, padx=18, pady=15, bg="#1338be",fg="white")
sendButton.grid(row = 0, column = 2)
saveButton = Button(fr2, text = "Save", command = download, padx=18, pady=15, bg="#1338be",fg="white")
saveButton.grid(row=0,column=4 )
tabControl= ttk.Notebook(statusframe)
statusframe.grid(row=3, column=4)
tab_4 = Label(tabControl,text ="", bg="#fff")

# tabs widget
scrollbar = Scrollbar(responseframe)
scrollbar.pack( side = RIGHT, fill = Y )
tabControl = ttk.Notebook (responseframe, height = 700, width = 1500)
tab_1 = Label(tabControl, text="",bg="#fff")
tab_2 = Label(tabControl, text="",bg="#fff")
tab_3 = Label(tabControl, text="",bg="#fff")
tabControl.add(tab_1, text = 'Raw',)
tabControl.add(tab_2, text = 'Preview')
tabControl.add(tab_3, text = 'Headers')



# tabControl= ttk.Notebook(statusframe,height=40, width=80)
# tabControl.grid(statusframe, row=3, column=4)

# tabControl = ttk.Notebook(responseframe, 
#                  yscrollcommand = scrollbar.set )
# scrollbar.config( command = tabControl.yview )
# add an output area
# tabControl1 = ttk.Notebook(responseframe, height=40,width=50)
# tab_4 = Label(tabControl1, text="", bg="#fff")
# tabControl.add(tab_4, text = 'Response')
tabControl.pack(fill = "both")

# Label Creation
lbl1 = Label(tab_1, text = "Click Send to get a response", height=1150, width=100, padx = 50, pady=50, bg = "#fff", fg = "black", font = "Helvetica 13", justify = "left")
lbl1.pack()
lbl2 = HTMLLabel(tab_2, html = "<h1>Click Send to get a response<h1/><br><h2>hello<h2/>", height=1150, width=1300, padx = 50, pady=50, bg = "#fff", fg = "black", font = "Helvetica 13")
lbl2.pack()
lbl3 = Label(tab_3, text = "Click Send to get a response", height=1150, width=1300, padx = 50, pady=50, bg = "#fff", fg = "black", font = "Helvetica 13")
lbl3.pack()
# lbl4 = Label(tab_4, text = "",height=40, width=1300, padx = 50, pady=50, bg = "#fff", fg = "black", font = "Helvetica 13")
# lbl4.pack()
frame.mainloop()