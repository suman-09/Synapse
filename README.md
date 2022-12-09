<!-- The links have to be edited -->
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)


# Quick Links


- [How to run the project](https://github.com/mayankt18/glugle#search-engine-made-using-python-and-flask)
    
    ### Documentation
    - [Introduction](https://github.com/mayankt18/glugle/blob/master/resources/1.I.search%20engine.md#search-engine-basics)
    - Setup ([Linux](https://github.com/mayankt18/glugle/blob/master/resources/1.II.setup.md#python-installation-guide) / [Windows](https://github.com/mayankt18/glugle/blob/master/resources/1.II.setup_win.md#project-setup-in-windows))
    - [Tkinter](https://github.com/suman-09/Tdoc_py/blob/main/Tkinter.md)
    - [Requests](https://github.com/mayankt18/glugle/blob/master/resources/2.II.crawler.md#web-crawler)
    - [Integration](https://github.com/mayankt18/glugle/blob/master/resources/3.flask.md#flask-guide)
    - [Response](https://github.com/mayankt18/glugle/blob/master/resources/4.web%20app.md#the-web-app)

=======
```
pyhton3 --version
```
if you don't have python preinstalled, you can install it using following command

```
sudo apt-get install python3.6
```
### **WINDOWS**
For windows, all you have to do is download python, and you are good to go and explore this language using any IDLE

Python can be downloaded from the official python website. link below
 __link__: https://www.python.org/downloads/windows/

### **MacOS**
Python can be downloaded for MacOS using the same website.
__link__ : https://www.python.org/downloads/macos/


# **API**
 API is acronym  for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other.
=======
**[Introduction](file.md)**

- **[API](API.md)**
- **[Tkinter](Tkinter.md)**
- **[The ```Requested``` Function](Req.md)**
- **[tkhtmlview](htmlview.md)**
- **[The ```save``` Function](save.md)**
***
 **Approach for building an API Tester**


# Search engine made using Python and flask

## Project Setup

1. Clone the git in a folder
2. Make a virtual environment in the folder


**For Windows**
```
pip install virtualenv
cd project_folder
virtualenv env
.\env\Scripts\activate
```

**For Linux**
```
pip install virtualenv #for version 2 and below 
pip3 install virtualenv #for version 3
cd project file
virtualenv env
source ./env/bin/activate
```

3. Install requirements
```
pip3 install -r requirements.txt
```


4. Start the application
=======
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
python app.py #for version 2 and below
python3 app.py #for version 3
```

=======
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


