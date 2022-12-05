from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkhtmlview import HTMLLabel
from req import *
import os
from tkinter.simpledialog import askstring
from bs4 import BeautifulSoup as bs
from pywebcopy import save_website

frame = Tk()
frame.title("Synapse")

#set window size (widthxheight)
frame.geometry("1260x820")

#set window colour
frame.config(bg='#fff')

fr1 = Frame(frame, borderwidth = 0, bg = "linen", relief = SUNKEN, pady = 40)
fr1.pack(fill = "x")
fr2 = Frame(fr1, borderwidth = 0, bg = "linen", width=1000, pady = 30)
fr2.pack(anchor = "center")
responseframe = Frame(frame, bg = "white")
responseframe.pack()
sframe = Frame(responseframe, padx = 3, pady = 3, bg = "white", highlightbackground= "black", highlightthickness=3)
sframe.pack(pady = 30)
bframe = Frame(fr1, padx = 30, pady = 30, bg = "white")
bframe.pack(anchor  ="center")
statusframe = Frame(sframe, bg="white")
statusframe.pack()

#function 

#to get which requested setted at request
def got():
    slktd = clicked.get()
    law = slktd.lower()
    return(law)   

# http request function
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
    lbl1.delete("1.0", "end")
    lbl3.delete("1.0", "end")
    lbl1.insert(tk.END , prettyHTML)
    lbl3.insert(tk.END, hed)
    lbl2.set_html(txt)
    status.config(text = "Status Code : " + str(statcode))
    return url

# Download and save function
def download():
    lnk = requested()
    save_website( url=lnk, project_folder="./saved_website/")
    messagebox.showinfo("Success!", "Project folder saved.")
    
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
drop.config( bg="#1338be", fg="#fff", padx = 20, pady = 10)

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
tabControl.pack(fill = "both", padx = 400, pady = 45)


# Button Creation
sendButton = Button(fr2, text = "Send", command = requested, padx=18, pady=15, bg="#1338be",fg="white")
sendButton.grid(row = 0, column = 2)
saveButton = Button(fr2, text = "Save", command = download, padx=18, pady=15, bg="#1338be",fg="white")
saveButton.grid(row=0,column=4 )
tabControl= ttk.Notebook(statusframe)
statusframe.grid(row=4, column=4)

# tabs widget
tabControl = ttk.Notebook (responseframe, height = 700, width = 1500)
tab_1 = Label(tabControl, text="",bg="#fff")
tab_2 = Label(tabControl, text="",bg="#fff")
tab_3 = Label(tabControl, text="",bg="#fff")
tabControl.add(tab_1, text = 'Raw',)
tabControl.add(tab_2, text = 'Preview')
tabControl.add(tab_3, text = 'Headers')
tabControl.pack(fill = "both")

#status code creation
status = Label(statusframe, text = "Status Code: 000", height = 1, width = 16)
status.pack()

# Label Creation
lbl1 = Text(tab_1, height=1150, width=100, padx = 50, pady=50, bg = "#fff", fg = "black", font = "Helvetica 13")
lbl1.pack()
lbl2 = HTMLLabel(tab_2, html = "<h3>Click Send to get a response<h3/>", height=1150, width=1300, padx = 50, pady=50, bg = "#fff", fg = "black", font = "Helvetica 13")
lbl2.pack(anchor = "center")
lbl3 = Text(tab_3, height=1150, width=1300, padx = 50, pady=50, bg = "#fff", fg = "black", font = "Helvetica 13")
lbl3.pack()

frame.mainloop()