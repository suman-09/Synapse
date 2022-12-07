**[Introduction](file.md)**

- **[API](API.md)**
- **[Tkinter](Tkinter.md)**
- **[The ```Requested``` Function](Req.md)**
- **[tkhtmlview](htmlview.md)**
- **[The ```save``` Function](save.md)**
***
 **Approach for building an API Tester**

 This project will enable us to perform the following functions on API:
1. GET
1. POST
1. PUT
1. PATCH
### **GET:**
 A GET request, in simple terms, is a way for you to grab data from a data source with the help of the internet.

### **POST:**

 POST is used to send data to a server to create/update a resource.

### **PUT:**

 PUT is used to send data to a server to create/update a resource.


 The difference between POST and PUT is that PUT requests are idempotent. That is, calling the same PUT request multiple times will always produce the same result. In contrast, calling a POST request repeatedly have side effects of creating the same resource multiple times.
 <!-- ### **AUTH:** 
 Auth is used to add your auth details to the relevant parts of the request when you select or enter them, so you can preview how your data will be sent before you run the request. Your auth data will appear in the relevant parts of the request, for example in the Headers tab. -->
 ### **PATCH:**
 This method is used to update the existing 
 resource  on server and produces new version of existing resource. 
 
 
 The differnce between POST and PATCH is that  POST  updates thhe complete information while PATCH updates some parts of information.   
 ### **DELETE:**
  DELETE request deletes a resource already present in the server. 
***
## In this project we are using mainly the following python libraries:-
 1. REQUESTS
 1. TKINTER
1. TkHTMLView 
1. Tkinter.SimpleDialog 
1. BeautifulSoup from BS4 
1. PyWebCopy 
 
<!--  Once our HTTP requests are working properly and we are able to fetch data from the API, we need a proper interface to send and receive a request. And for this purpose, we have the Tkinter library in python. -->

<!-- Further next here is the way to create a Drop-down menu
```
#Create an instance of tkinter frame
root= Tk()

#Define the size of window or frame
root.geometry("715x250")

#Set the Menu initially
menu= StringVar()
menu.set("Select Any Language")

#Create a dropdown Menu
drop= OptionMenu(root, menu,"C++", "Java","Python","JavaScript","Rust","GoLang")
drop.pack()

root.mainloop()
```
If you want to create a text widget then here is the way
```
root = Tk()
 
# specify size of window.
root.geometry("250x170")
 
# Create text widget and specify size.
T = Text(root, height = 5, width = 52)
```
Tabbed Notebook  widget
```
root = tk.Tk()
root.title("Tab Widget")
title(name)
tabControl = ttk.Notebook(root)
Notebook(master=None, **options)

root.mainloop()
```
Button widget
```
# import everything from tkinter module
from tkinter import *   
 
# create a tkinter window
root = Tk()             
 
# Open window having dimension 100x100
root.geometry('100x100')
 
# Create a Button
btn = Button(root, text = 'Click me !', bd = '5')
 
# Set the position of button on the top of window.  
btn.pack(side = 'top')   
 
root.mainloop()
``` -->
<!-- [app](app.py) -->

